from collections import OrderedDict
from phone_book import PhoneBook

# Создайте LinkedHashMap и добавьте в него 5 элементов. Выведите их в порядке добавления.

phone_book: OrderedDict[str, str] = OrderedDict()


phone_book["tanya"] = "79223334422"
phone_book["john"] = "79222277422"
phone_book["ilon"] = "79224634634"
phone_book["mikhail"] = "79225545434"
phone_book["vasily"] = "79223545345"

print(phone_book)

for k, v in phone_book.items():
    print(k, v)

# Реализуйте телефонную книгу с LinkedHashMap. Добавьте и найдите контакт.

my_phone_book = PhoneBook()

my_phone_book.add_user_batch(phone_book)

my_phone_book.find_by_name("tany1a")

contact_from_keyboard = input()

my_phone_book.find_by_name(contact_from_keyboard)

# Создайте LinkedHashMap, который хранит историю просмотров пользователя (максимум 10 элементов).

user_history: OrderedDict[str, str] = OrderedDict()


def add_element(page_id: str, page_name: str):
    if len(user_history) < 10:
        user_history[page_id] = page_name
    else:
        user_history.popitem(last=False)
        user_history[page_id] = page_name


def show_history(history: OrderedDict[str, str]):
    for idx, (page_id, name) in enumerate(history.items(), start=1):
        print(f"{idx}. id:{page_id}. name:{name}")
    print("\n")


# user_history['1'] = 'index1'
# user_history['2'] = 'index2'
# user_history['3'] = 'index3'
# user_history['4'] = 'index4'
# user_history['5'] = 'index5'
# user_history['6'] = 'index6'
# user_history['7'] = 'index7'
# user_history['8'] = 'index8'
# user_history['9'] = 'index9'
# user_history['10'] = 'index10'


add_element('1', 'index1')
add_element('2', 'index2')
add_element('3', 'index3')
add_element('4', 'index4')
add_element('5', 'index5')
add_element('6', 'index6')
add_element('7', 'index7')
add_element('8', 'index8')
add_element('9', 'index9')
add_element('10', 'index10')


show_history(user_history)


add_element('11', 'index11')


show_history(user_history)
