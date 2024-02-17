import time
import json
import os
from classes import Record, AddressBook
from colors import *
from comands import *


# from prompt_toolkit import prompt
# from prompt_toolkit.completion import WordCompleter



class InputError(Exception):
    pass


class ContactAssistant:
    
    
    
    def __init__(self):
        self.address_book = AddressBook()
        self.file_path = "contacts.json"
       
        if os.path.exists(self.file_path):
            self.load_data()

    def save_data(self):
        with open(self.file_path, "w") as file:
            data = {
                "records": [record.__json__() for record in self.address_book.values()]
            }
            json.dump(data, file)

    def load_data(self):
        try:
            if os.path.getsize(self.file_path) > 0:  
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    records = [Record(record["name"], record.get("birthday")) for record in data.get("records", [])]
                    for i, record in enumerate(records):
                        if "phones" in data.get("records", [])[i]:
                            for phone in data["records"][i]["phones"]:
                                record.add_phone(phone)
                        self.address_book.add_record(record)
        except (OSError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading data: {e}")

    def add_contact(self, name, phone, birthday=None):
        try:
            record = Record(name, birthday)
            record.add_phone(str(phone).strip()) 
            self.address_book.add_record(record)
            self.save_data()
            return f"{YLLOW}Новий контакт успішно додано!!!{PISKAZKA_SHOW_ALL}"
        except ValueError as e:
            raise InputError(str(e))

    def change_contact(self, name, phone):
        try:
            record = self.address_book.find(name)
            if record:
                if len(phone) == 10 and phone.isdigit():
                    print(phone)
                    record.phones = []  
                    record.add_phone(phone)
                    self.save_data()  
                    return f"{YLLOW}Номер телефону успішно змінено!!!{PISKAZKA_SHOW_ALL}"
                else:
                    raise ValueError(f"{BAD_FORMAT_PHONE}")
            else:
                raise IndexError(f"{NOT_FOUND_NAME}")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def get_phone(self, name):
        try:
            record = self.address_book.find(name)
            if record:
                return (f"{YLLOW}За вказаним іменем {BIRUZA}{name}{YLLOW} знайдено номер"
                        f"{BIRUZA} {record.phones[0]}{DEFALUT}")
            else:
                raise IndexError(f"{NOT_FOUND_NAME}")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def show_all_contacts(self):
        records = list(self.address_book.values())
        if not records:
            return f"{YLLOW}Ваша телефона книга поки не містить жодного запису{DEFALUT}"
        else:
            result = f'{GREEN}{"Name":^10}  {"Phone":^12}{YLLOW}\n'
            for record in records:
                phone_numbers = ', '.join(str(phone) for phone in record.phones)
                # result += f"{f"{record.name}":<10} {phone_numbers}\n"
                result += "{:<10}: {}\n".format(record.name.value, phone_numbers)

            return result.strip()

class CommandHandler:
    
    
    def __init__(self, contact_assistant):
        self.contact_assistant = contact_assistant

    def handle_hello(self, args):
        return f"{YLLOW}How can I help you?{DEFALUT}"

    def handle_add(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_ADD)

        contact_info = args.split(" ")
        if len(contact_info) != 3:
            raise InputError(BAD_COMMAND_ADD)

        _, name, phone = args.split(" ")
        return self.contact_assistant.add_contact(name, phone)

    def handle_change(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_CHANGE)

        contact_info = args.split(" ")
        if len(contact_info) != 3:
            raise InputError(BAD_COMMAND_CHANGE)

        _, name, phone = args.split(" ")
        return self.contact_assistant.change_contact(name, phone)

    def handle_phone(self, args):
        
        args_list = args.split(" ")
        if len(args_list) == 2:
            raise InputError(BAD_COMMAND_PHONE)
        
        name = args_list[2]
        return self.contact_assistant.get_phone(name)

    def handle_show(self, args):
        return self.contact_assistant.show_all_contacts()

    def handle_bye(self, args):
        
        return f"{YLLOW}Good bye!"
    
    def handle_search(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_SEARCH)

        query = args.split(" ", 1)[1]
        matching_records = self.contact_assistant.address_book.search(query)

        if not matching_records:
            return f"{YLLOW}Нажаль нічого не знайдено  {DEFALUT}"
        else:
            result = f"{YLLOW}За Вашим запитом * {RED}{query}{YLLOW} * було знайдено наступні записи :{DEFALUT}\n"
            
            for record in matching_records:
                phone_numbers = ', '.join(str(phone) for phone in record.phones)
                result += f"{YLLOW}{record.name}: {phone_numbers}\n"
            return result.strip()

    def choice_action(self, data):
        
        ACTIONS = {
            'hello': self.handle_hello,
            'add': self.handle_add,
            "change": self.handle_change,
            "get phone": self.handle_phone,
            'search': self.handle_search,
            "show all": self.handle_show,
            "exit": self.handle_bye,
            
        }
        return ACTIONS.get(data, lambda args: f'{NOT_FOUND_COMMAND}')

    def process_input(self, user_input):
        '''Функція яка приймає один аргумент - стрічку що вів користувач.
        Аналізує її і повертає або помилку або валідну функцію яка відповідає вказаній словнику *ACTIONS команді
        '''
        try:
            if not user_input:
                raise InputError(f'{YLLOW}Ви нічого не ввели \n{DOSTUPNI_COMANDY}{DEFALUT}')

            space_index = user_input.find(' ')

            if space_index != -1:
                list_word = user_input.lower().strip().split()
                first_word= user_input[:space_index]
                
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
   
    print(f'\n{YLLOW}Вас вітає Бот для роботи з вашии контактами.')
    print(f'{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}{DEFALUT}')
    
    def run(self):
        contact_assistant = ContactAssistant()
        command_handler = CommandHandler(contact_assistant)
        # Список вариантів для автодоповнення
        words = ['hello', 'help', 'hi', 'hey', 'add', 'change', 'phone', 'show all', 'search', 'exit']

        # Створюємо комплиттер з нашими варінтами
        # completer = WordCompleter(words, ignore_case=True)
        

        while True:
            try:
# <<<<<<< HEAD
                user_input = input(f"{PURPURE}Введіть команду>>{DEFALUT}").lower().strip()
# =======
#                 time.sleep(2)
                          
                # user_input = prompt("ВВедіть команду>> ", completer=completer).lower().strip()
                
# >>>>>>> db1b7b732b5c52e9d733a58be9bcf377f7935df6
                result = command_handler.process_input(user_input)

                if result is None:
                    break
                else:
                    print(result)
                    # Добавляем паузу на 1 секунду перед возвратом к приглашению для ввода команды
                    time.sleep(1)

            except Exception as e:
                print(e)
