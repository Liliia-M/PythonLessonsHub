import json

def record_new_contacts(contacts):
    with open("contact_list.json", "w", encoding = "utf-8") as f:
        json.dump(contacts, f, ensure_ascii = False, indent = 4)

