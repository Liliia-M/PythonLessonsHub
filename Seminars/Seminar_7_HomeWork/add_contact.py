def add_contact(list_dict_contacts):
    new_dict = dict.fromkeys(["fio", "phone"])
    new_dict["fio"] = input('Введите ФИО: ')
    new_dict["phone"] = input('Введите номер телефона (пять цифр): ')
    list_dict_contacts.append(new_dict)
    return list_dict_contacts