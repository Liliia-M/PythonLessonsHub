import json
# contacts = [
#     { "fio": "ivan petrov", "phone": "12345" },
#     { "fio": "max petrov", "phone": "33345" },
#     { "fio": "nikolay terehov", "phone": "52345" },
#     { "fio": "ludmila famusova", "phone": "31245" }
# ]

# with open("contact_list.json", "w", encoding = "utf-8") as f:
#     json.dump(contacts, f, ensure_ascii = False, indent = 4)

def get_list_dict_contacts():
    with open("contact_list.json", encoding = "utf-8") as f:
        json_data = json.load(f)
    return json_data

def print_list_dict_contacts(lst):
    print(lst)

def view_contacts(list_dict_contacts):
    list_contact = []
    for i in list_dict_contacts:
        j = i.values()
        for j in i.values():
            list_contact.append(j)
    print(list_contact)

