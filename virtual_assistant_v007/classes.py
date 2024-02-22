import re
from virtual_assistant_v007.comands import *
from virtual_assistant_v007.colors import *
from datetime import datetime
from collections import UserDict


class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not self.is_valid(new_value):
            raise ValueError
        self.__value = new_value

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        return True

    def __json__(self):
        return self.value


class Name(Field):
    def is_valid(self, value):
        return isinstance(value, str) and value


class Phone(Field):
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError(f"{BAD_FORMAT_PHONE}")

        super().__init__(value)

    def is_valid(self, value):
        if not value:
            return True
        return isinstance(value, str) and value.isdigit() and len(value) == 10


class Email(Field):

    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError(BAD_FORMAT_EMAIL)
        super().__init__(value)

    def is_valid(self, value):
        if not value:
            return True
        return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', value)

    def __json__(self):
        return str(self.value) if self.value else None


class Address(Field):

    def __json__(self):
        return str(self.value) if self.value else None


class Birthday(Field):
    def __init__(self, value=None):
        if not self.is_valid(value):
            raise ValueError(BAD_FORMAT_BIRTHDAY)
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not self.is_valid(new_value):
            raise ValueError(BAD_FORMAT_BIRTHDAY)
        if new_value:
            datetime.strptime(new_value, "%Y-%m-%d")
        self.__value = new_value

    def is_valid(self, value):
        if not value:
            return True
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            return False
        else:
            return True

    def __json__(self):
        return str(self.value) if self.value else None


class Record:
    def __init__(self, name, birthday=None, address=None):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.birthday = Birthday(birthday) if birthday else None
        self.address = Address(address) if address else None

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def add_email(self, email):
        email_obj = Email(email)
        self.emails.append(email_obj)

    def set_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def set_address(self, address):
        self.address = Address(address)

    def remove_phone(self, phone):
        initial_len = len(self.phones)
        self.phones = [p for p in self.phones if p.value != phone]
        if len(self.phones) == initial_len:
            raise ValueError(f"{YLLOW}Такого номера телефона <--'{RED}{phone}"
                             f"{YLLOW}-->' немає нажаль у вашій телефонній книжці")

    def edit_phone(self, old_phone, new_phone):
        if not Phone(new_phone).is_valid(new_phone):
            raise ValueError(f"\n {YLLOW}-- <'{RED}{new_phone}{YLLOW}'> -- {BAD_FORMAT_PHONE}")
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError(f"{YLLOW}Такого номера телефона <--'{RED}{old_phone}"
                         f"{YLLOW}-->' немає нажаль у вашій телефонній книжці")

    def find_phone(self, phone):
        found_numbers = [p for p in self.phones if p.value == phone]
        return found_numbers[0] if found_numbers else None

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            birthday_date = datetime.strptime(self.birthday.value, "%Y-%m-%d").date()

            next_birthday = datetime(today.year, birthday_date.month, birthday_date.day).date()
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, birthday_date.month, birthday_date.day).date()

            days_left = (next_birthday - today).days
            return days_left
        else:
            return None

    def __json__(self):
        record_data = {
            "name": self.name.__json__(),
            "phones": [phone.__json__() for phone in self.phones],
            "emails": [email.__json__() for email in self.emails],
            "birthday": self.birthday.__json__() if self.birthday else None,
            "address": self.address.__json__() if self.address else None
        }
        return record_data

    def __str__(self):

        return (f"{str(self.name.value)}, {str(self.address)}, {str(self.birthday)},"
                f" {'; '.join(str(p.value) for p in self.phones)},"
                f" {'; '.join(str(p.value) for p in self.emails)}")


class AddressBook(UserDict):
    def search(self, query):
        matching_records = []

        def is_present(arg):
            result = False
            for item in arg:
                if item:
                    result = True
            return result

        for record in self.data.values():

            if ((query.lower() in str(record.name).lower())
                    or is_present([query in str(phone.value) for phone in record.phones])
                    or is_present([query.lower() in str(email).lower() for email in record.emails])
                    or (query.lower() in str(record.address).lower())):
                matching_records.append(record)

            # if query.lower() in str(record.name).lower():
            #     matching_records.append(record)
            #     continue
            # for phone in record.phones:
            #     if query in str(phone.value):
            #         matching_records.append(record)
            #         break
            # for email in record.emails:
            #     if query.lower() in str(email).lower():
            #         matching_records.append(record)
            #         break
            # if query.lower() in str(record.address).lower():

        return matching_records

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_case_insensitive(self, name):
        for record in self.data.values():
            if record.name.value.lower() == name.lower():
                return record
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return 'Ok'
        else:
            raise ValueError(NOT_FOUND_NAME)

    def iterator(self, page_size=10):
        keys = list(self.data.keys())
        for i in range(0, len(keys), page_size):
            yield [self.data[key] for key in keys[i:i + page_size]]

    def find(self, name):
        return self.data.get(name)

    def rename_contact(self, old_name: str, new_name: str):
        record = self.find(old_name)
        if record:
            record.name.value = new_name
            self.data[new_name] = record
            self.delete(old_name)
        else:
            raise ValueError(NOT_FOUND_NAME)
        return 'Ok'
