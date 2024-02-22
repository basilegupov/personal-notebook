from virtual_assistant_v007.classes import Record, AddressBook
from datetime import datetime
from virtual_assistant_v007.colors import *
from virtual_assistant_v007.comands import *
import json
import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from virtual_assistant_v007.sorted import *
from virtual_assistant_v007.notes import run_notes


class InputError(Exception):
    pass


class ContactAssistant:

    def __init__(self):
        self.address_book = AddressBook()
        self.file_path = "contacts.json"

        if os.path.exists(self.file_path):
            self.load_data()

    def birthdays_in_days(self, days):
        upcoming_birthdays = []

        today = datetime.now().date()

        for record in self.address_book.values():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%Y-%m-%d").date()
                next_birthday = datetime(today.year, birthday_date.month, birthday_date.day).date()

                if today > next_birthday:
                    next_birthday = datetime(today.year + 1, birthday_date.month, birthday_date.day).date()

                days_left = (next_birthday - today).days
                if 0 < days_left <= days:
                    upcoming_birthdays.append((record.name.value, days_left))

        return upcoming_birthdays

    def save_data(self):
        with open(self.file_path, "w") as file:
            data = {
                "records": [record.__json__() for record in self.address_book.values()]
            }
            json.dump(data, file, indent=2)

    def load_data(self):
        try:
            if os.path.getsize(self.file_path) > 0:
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    for record_data in data.get("records", []):
                        name = record_data.get("name")
                        birthday = record_data.get("birthday")
                        address = record_data.get("address")
                        record = Record(name, birthday=birthday, address=address)
                        
                        phones = record_data.get("phones", [])
                        for phone in phones:
                            record.add_phone(phone)
                        
                        emails = record_data.get("emails", [])
                        for email in emails:
                            record.add_email(email)
                        
                        self.address_book.add_record(record)
        except (OSError, json.JSONDecodeError, KeyError) as e:
            print(f"Помилка завантаження даних: {e}")

    def add_contact(self, name, **args):
        try:
            record = Record(name)
            for arg, val in args.items():
                if arg.lower() == 'phone':
                    record.add_phone(val)
                elif arg.lower() == 'email':
                    record.add_email(val)
                elif arg.lower() == 'birthday':
                    record.set_birthday(val)
                elif arg.lower() == 'address':
                    record.set_address(val)
            self.address_book.add_record(record)
            self.save_data()
            return f"{YLLOW}Новий контакт успішно доданий!!!{PISKAZKA_SHOW_ALL}"
        except ValueError as e:
            raise InputError(str(e))

    def change_contact(self, name, newname=None, phone=None, email=None, address=None, birthday=None):
        try:
            record = self.address_book.find(name)
            if record:
                if phone:
                    record.phones = []
                    record.add_phone(phone)
                if email:
                    record.emails = []
                    record.add_email(email)
                if address:
                    record.set_address(address)
                if birthday:
                    record.set_birthday(birthday)
                if newname:
                    self.address_book.rename_contact(name, newname)
                self.save_data()
                return f"{YLLOW}Дані успішно змінені!!!{PISKAZKA_SHOW_ALL}"
            else:
                raise IndexError(f"{YLLOW}Не знайдено контакт {BIRUZA}{name}{DEFALUT}! {PISKAZKA_SHOW_ALL}")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def get_email(self, name):
        try:
            record = self.address_book.find(name)
            if record and record.emails:
                emails = ', '.join(str(email) for email in record.emails)
                return f"{YLLOW}За вказаним іменем {BIRUZA}{name}{YLLOW} знайдено email{BIRUZA} {emails}{DEFALUT}"
            else:
                raise IndexError(f"{YLLOW}Такого імені або email не знайдено у вашій телефоній книзі !!!"
                                 f"{DEFALUT}{PISKAZKA_SHOW_ALL} ")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def add_email_to_contact(self, name, email):
        try:
            record = self.address_book.find_case_insensitive(name)
            if record:
                record.add_email(email)
                self.save_data()
                print(f"DEBUG: Email успішно добавлений для контакта {record.name.value} - {email}")
                return f"{YLLOW}Email успішно добавлений для контакта {BIRUZA}{record.name.value}{DEFALUT}"
            else:
                raise IndexError(NOT_FOUND_NAME)
        except (ValueError, IndexError) as e:
            raise InputError(str(e))
        
    def get_email_by_email(self, email):
        try:
            return self.get_email(email)
        except InputError:
            raise InputError(f"{YLLOW}Такого імені або email не знайдено у вашій телефоній книзі !!!"
                             f"{DEFALUT}{PISKAZKA_SHOW_ALL}")

    def get_phone(self, name):
        try:
            record = self.address_book.find(name)
            if record:
                return (f"{YLLOW}За вказаним іменем {BIRUZA}{name}{YLLOW} знайдено номер"
                        f"{BIRUZA} {record.phones[0]}{DEFALUT}")
            else:
                raise IndexError(NOT_FOUND_NAME)
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def show_all_contacts(self):
        records = list(self.address_book.values())
        if not records:
            return f"{YLLOW}Ваша телефонна книга поки не містить жодного конткту{DEFALUT}"
        else:
            result = f'{GREEN}{"Name":<10} {"Birthday":^12} {"Phone":<12} {"Email":<20} {"Address":<20} {YLLOW}\n'
            for record in records:
                phone_numbers = ', '.join(str(phone) for phone in record.phones)
                emails = ', '.join(map(str, [email.value for email in record.emails if email.value]))
                result += (f"{record.name.value:<10} {str(record.birthday):^12} {phone_numbers:<12}"
                           f" {emails:<20} {str(record.address):<20}\n")

            return result.strip()

    def delete_contact(self, name):
        try:
            self.address_book.delete(name)

        except (ValueError, IndexError) as e:
            raise InputError(str(e))

class CommandHandler:
    
    def __init__(self, contact_assistant):
        self.contact_assistant = contact_assistant

    def handle_hello(self, args):
        return f"{YLLOW}How can I help you?{DEFALUT}"

    def handle_add(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_ADD)
        contact_info = args.split(" ")
        if len(contact_info) < 3:
            raise InputError(BAD_COMMAND_ADD)

        _, name, *contact_values = contact_info
        
        phone = None
        email = None
        address = None
        birthday = None

        for contact_value in contact_values:
            parameter, val = contact_value.split('=')
            if parameter.strip().lower() == 'email':
                email = val.strip()
            elif parameter.strip().lower() == 'phone':
                phone = val.strip()
            elif parameter.strip().lower() == 'address':
                address = val.strip()
            elif parameter.strip().lower() == 'birthday':
                birthday = val.strip()
            else:
                raise InputError(BAD_COMMAND_ADD)

        try:
            return self.contact_assistant.add_contact(name=name, phone=phone, email=email,
                                                      address=address, birthday=birthday)
        except InputError as e:
            raise InputError(str(e))

    def handle_change(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_CHANGE)

        contact_info = args.split(" ")
        if len(contact_info) != 3:
            raise InputError(BAD_COMMAND_CHANGE)

        _, name, contact_value = args.split(" ")
        parameter, val = contact_value.split('=')
        if parameter.strip().lower() == 'email':
            return self.contact_assistant.change_contact(name, email=val.strip())
        elif parameter.strip().lower() == 'phone':
            return self.contact_assistant.change_contact(name, phone=val.strip())
        elif parameter.strip().lower() == 'address':
            return self.contact_assistant.change_contact(name, address=val.strip())
        elif parameter.strip().lower() == 'birthday':
            return self.contact_assistant.change_contact(name, birthday=val.strip())
        elif parameter.strip().lower() == 'name':
            return self.contact_assistant.change_contact(name, newname=val.strip())

        else:
            raise InputError(BAD_COMMAND_CHANGE)

    def handle_email(self, args):
        if len(args.split()) < 2:
            raise InputError(BAD_COMMAND_EMAIL)

        name_or_email, *emails = args.split(" ", 1)[1].strip().split(",")
        
        if '@' in name_or_email:
            
            return self.contact_assistant.get_email(name_or_email.strip())
        return self.contact_assistant.get_email(name_or_email)

    def handle_phone(self, args):
        args_list = args.split(" ")
        if len(args_list) <= 2:
            raise InputError(BAD_COMMAND_PHONE)
        
        name = args_list[2]
        return self.contact_assistant.get_phone(name)

    def handle_show(self, args):
        return self.contact_assistant.show_all_contacts()

    def handle_delete(self, args):
        args_list = args.split(" ")
        if len(args_list) < 2:
            raise InputError(BAD_COMMAND_DELETE)
        name = args_list[1]
        self.contact_assistant.delete_contact(name)
        return f"Контакт {name} видалений вдало.\n" + self.contact_assistant.show_all_contacts()
    
    def handle_bye(self, args):
        print("До побачення!")
        return None

    def handle_birthdays(self, args):
        try:
            if len(args.split()) < 2:
                raise InputError(BAD_COMMAND_BIRTHDAYS)

            _, days = args.split(" ", 1)
            days = int(days)

            result = self.contact_assistant.birthdays_in_days(days)
            if not result:
                return f"{YLLOW}Немає жодних днів народження наступні - {RED}{days}{YLLOW} днів.{DEFALUT}"
            else:
                output = f"{YLLOW}Найближчі дні народження протягом наступних{RED} - {days}{YLLOW} днів:{DEFALUT}\n"
                for name, days_until_birthday in result:
                    output += f"{BIRUZA}{name:<10}{DEFALUT} - {RED}{days_until_birthday:^12}{YLLOW} днів\n"
                    
                return output.strip()

        except (IndexError, ValueError):
            raise InputError(BAD_COMMAND_BIRTHDAYS)

    def handle_search(self, args):
        if len(args.split()) < 2:
            raise InputError(BAD_COMMAND_SEARCH)

        query = args.split(" ", 1)[1]

        matching_records = self.contact_assistant.address_book.search(query)

        if not matching_records:
            return f"{YLLOW}Нажаль нічого не знайдено  {DEFALUT}"
        else:
            result = f"{YLLOW}За Вашим запитом = {RED}{query}{YLLOW} було знайдено наступні записи :{DEFALUT}\n"
            result += f'{GREEN}{"Name":<10} {"Birthday":^12} {"Phone":<12} {"Email":<20} {"Address":<20} {YLLOW}\n'
            for record in matching_records:
                phone_numbers = ', '.join(str(phone) for phone in record.phones)
                emails = ', '.join(map(str, [email.value for email in record.emails if email.value]))
                result += (f"{record.name.value:<10} {str(record.birthday):^12} {phone_numbers:<12}"
                           f" {emails:<20} {str(record.address):<20}\n")
            return result.strip()    
    
    def handle_sorted(self, args):
        try:
            if len(args.split()) < 2:
                raise InputError(BAD_COMMAND_SORTED)

            folder_path = args.split(" ")[1]
            result = main(folder_path)
            return result
        except InputError as e:
            raise e 
    
    def handle_notes(self, args):
        run_notes()
        return f"{YLLOW}Роботу з нотатками завершено!!!\n{PURPURE}Готовий до наступних команд!!!{DEFALUT}"

    def handle_help(self, args):
        return HELP

    def choice_action(self, data):
        actions = {
            'hello': self.handle_hello,
            'add': self.handle_add,
            "change": self.handle_change,
            "get phone": self.handle_phone,
            'search': self.handle_search,
            'email': self.handle_email,
            "show all": self.handle_show,
            "birthday": self.handle_birthdays,
            "delete": self.handle_delete,
            "exit": self.handle_bye,
            'sorted': self.handle_sorted,
            'notes': self.handle_notes,
            'help': self.handle_help,
        }
        return actions.get(data, lambda args: NOT_FOUND_COMMAND)

    def process_input(self, user_input):
        try:
            if not user_input:
                raise InputError(f'{YLLOW}Ви нічого не ввели \n{DOSTUPNI_COMANDY}')

            space_index = user_input.find(' ')

            if space_index != -1:
                list_word = user_input.lower().strip().split()
                first_word = user_input[:space_index]
                
                if list_word[0] == "show" and list_word[1] == "all":
                    first_word = "show all"
                elif list_word[0] == "get" and list_word[1] == "phone":
                    first_word = "get phone"
                
            else:
                first_word = user_input

            func = self.choice_action(first_word)
            result = func(user_input)

            if result is None:
                return None
            else:
                return result
        except InputError as e:
            return str(e)


class Bot:

    def run(self):

        print(f'\n{YLLOW}Вас вітає Бот для роботи з Вашими контактами.')
        print(f'{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}')
        contact_assistant = ContactAssistant()
        command_handler = CommandHandler(contact_assistant)

        completer = WordCompleter(LIST_COMANDS_BOT, ignore_case=True)

        while True:
            try:
                user_input = prompt("Введіть команду>> ", completer=completer).strip()
                result = command_handler.process_input(user_input)

                if result is None:
                    break
                else:
                    print(result)

            except Exception as e:
                print(e)
