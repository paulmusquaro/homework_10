# AddressBookManager

**AddressBookManager** is a Python project designed to manage and maintain an address book. It allows users to store, add, edit, and delete contacts, along with their associated phone numbers. The address book is stored in memory and can be interacted with using simple Python objects.

## Features

- **Add Contacts**: Create new contacts with a name and one or more phone numbers.
- **Edit Contacts**: Modify existing contact details, including changing the name or adding/editing/removing phone numbers.
- **Search Contacts**: Find contacts by name or phone number.
- **Delete Contacts**: Remove contacts from the address book.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/paulmusquaro/AddressBookManager.git
   ```

2. Navigate into the project directory:
   ```bash
   cd AddressBookManager
   ```

3. The project doesn't have external dependencies, so no installation is necessary.

## Usage

Here's an example of how to use the `AddressBookManager`:

```python
from AddressBookManager import Name, Phone, Record, AddressBook

# Create a contact with a name and a phone number
name = Name('Bill')
phone = Phone('1234567890')
record = Record(name, phone)

# Create an address book and add the contact
address_book = AddressBook()
address_book.add_record(record)

# Accessing the contact
contact = address_book['Bill']
print(contact.name.value)  # Output: Bill
print(contact.phones[0].value)  # Output: 1234567890

# Editing the contact's phone number
new_phone = Phone('0987654321')
address_book.edit_record('Bill', new_phones=[(phone, new_phone)])

# Find contact by name
found_contacts = address_book.find_records_by_name('Bill')
print(found_contacts[0].phones[0].value)  # Output: 0987654321
```

## Classes

- **Field**: A base class representing a field in a record, such as a name or phone number.
- **Name**: A subclass of `Field`, used to store a person's name.
- **Phone**: A subclass of `Field`, used to store a phone number.
- **Record**: A class that stores a contact's name and phone numbers.
- **AddressBook**: A class that manages a collection of `Record` objects.

## Methods *(AddressBook)*

- **add_record(record)**: Adds a contact record to the address book.
- **delete_record(name)**: Deletes a contact by name.
- **edit_record(name, new_name=None, new_phones=None)**: Edits a contact's name and/or phone numbers.
- **find_records_by_name(name)**: Finds all contacts with a specific name.
- **find_records_by_phone(phone_value)**: Finds all contacts with a specific phone number.

## Contributing

If you'd like to contribute to the project, feel free to open an issue or a pull request. Please ensure that your code follows PEP 8 standards and includes relevant test cases.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
