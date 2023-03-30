phone_book = []
path = "phone.txt"

def open_file():
    with open(path, "r", encoding="UTF-8") as f:
        data = f.readlines()
    for fields in data:
        fields = fields.strip().split(";")
        contact = {"name": fields[0],
                   "phone": fields[1],
                   "comment": fields[2]}
        phone_book.append(contact)

def get_phone_book():
    return phone_book

def add_contact(contact: dict):
    phone_book.append(contact)


def change_contact(contact: dict, index: int):
    phone_book.pop(index-1)
    phone_book.insert(index-1, contact)

def save_phone_book():
    data = []
    for contact in phone_book:
        data.append(contact["name"] + ";" + contact["phone"] + ";" + contact["comment"] + "\n")
        with open(path, "w", encoding="UTF-8") as f:
            f.writelines(data)

def find_contact(search: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for field in contact.values():
            if search.lower() in field.lower():
                result.append(contact)
    return result

def delete_contact (index: int):
    del_contact = phone_book[index-1]["name"]
    phone_book.pop(index - 1)
    return del_contact