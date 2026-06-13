import json
contacts = {}
def add_contact(contacts, name):
    if name:
        if name in contacts:
            print("Такой контакт уже создан")
            print("Хотите обновить данные?")
            q=(input("Да/Нет"))
            if q=="Да":
                contacts[name]=input("Введите номер")
        else:
            contacts[name]= input("Введите номер телефона")
    else:
        print("Вы не ввели имя")
def find_contact(contacts, name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Контакт не найден")
def show_contacts(contacts):
    if contacts:    
        for key, valye in contacts.items():
            print(f"{key}: {valye}")
    else:
        print("Контактов еще нет")
def load_contacts():
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def save_contacts(contacts):
    with open("contacts.json","w",encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)



        
    
contacts=load_contacts()       
    
print("Добавить контакт - 1")
print("Найти конакт - 2")
print("Показать все контакты - 3")
print("Выход - 0")
while True:
    try:
        person=int(input("Введите число:  "))
    except:
        print("Нужно ввести именно число")
        continue


    if person == 1:
        add_contact(contacts, input("Введите имя. "))
        save_contacts(contacts)
    if person == 2:
        find_contact(contacts, input("Введите имя. "))
    if person == 3:
        show_contacts(contacts)
    if person==0:
        break
