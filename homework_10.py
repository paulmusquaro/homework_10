from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if isinstance(phone, Phone):
            self.phones.append(phone)
        else:
            raise ValueError("Invalid phone type")

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError("phone not found")

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)
        else:
            raise ValueError("phone not found")

class AddressBook(UserDict):
    def add_record(self, name, phones=None):
        record = Record(name)
        if phones:
            for phone in phones:
                record.add_phone(phone)
        self.data[name] = record

    def delete_record(self, name):
        del self.data[name]

    def edit_record(self, name, new_name=None, new_phones=None):
        if name not in self.data:
            print(f"{name} not found in the address book.")
            return

        record = self.data[name]
        if new_name:
            record.name.value = new_name

        if new_phones:
            for old_phone, new_phone in new_phones:
                record.edit_phone(old_phone, new_phone)

    def find_records_by_name(self, name):
        results = []
        for record in self.data.values():
            if record.name.value == name:
                results.append(record)
        return results

    def find_records_by_phone(self, phone_value):
        results = []
        for record in self.data.values():
            for phone in record.phones:
                if phone.value == phone_value:
                    results.append(record)
                    break
        return results

if __name__ == "__main__":
    address_book = AddressBook()