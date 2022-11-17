'''
Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. (Применить MVC)

ТЗ:
Операции с телефонным справочником:
1. Вывод контактов
2. Добавление контакта ФИО и телефон
3. Удаление контакта
4. Поиск контакта по имени и вывести список найденных контактов с заданным именем
5. Выгрызка в формате CSV, txt или JSON (экспорт)
6. Загрузка списка контактов из файлика выбранного формата
7. Редактирование контакта

Пример структутры:

contacts = [
{ "fio": "ivan petrov", "phone": "12345 },
{ "fio": "max petrov", "phone": "12333345 },
....
]
'''
import controller as c
import add_contact as ac
import view
import record_new_list_contact as rn
import delete_contact as dc
import find_contact as fc

c.pin_output() # вывод контактов


contacts_lst = ac.add_contact(view.get_list_dict_contacts()) # добавление контакта
print(contacts_lst)

rn.record_new_contacts(contacts_lst) # обновление файла с контактами после добавления контакта


contacts_lst = dc.pop_contact(view.get_list_dict_contacts()) # удаление контакта
print(contacts_lst)

rn.record_new_contacts(contacts_lst) # обновление файла с контактами после удаления контакта


fc.find_contacts(view.get_list_dict_contacts(), 'max petrov') # нахождение контакта по ФИО
