from collections import OrderedDict

class PhoneBook:
    _phone_book: OrderedDict[str, str]

    def __init__(self):
        self._phone_book = OrderedDict()


    def find_by_name(self, name: str):
        if not self._phone_book.get(name):
                print("Contact not found")
        else:
            print(self._phone_book.get(name))

    def add_user(self, name: str, phone: str):
        self._phone_book[name] = phone

    def add_user_batch(self, phone_book_dict: OrderedDict[str, str]):
        self._phone_book = phone_book_dict