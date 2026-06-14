import json
def load_todo():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
tasks=load_todo()

    
def add_task(tasks, text):
    tasks.append({"id": len(tasks)+1, "text": text, "done": False})
    with open("tasks.json","w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)
    print("Задача добавлена")

def list_tasks(tasks):
    if tasks:   
        for i in tasks:
            print(f"{i['id']}: {i['text']} - {i['done']}")
    else:
        print("Задач еще нет")
        
def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"]= True
    with open("tasks.json","w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)
    print("Задача выполнена!!!")

def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
    with open("tasks.json","w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)
    print(f"Задача №{task['id']} удалена")


print("Добавить задачу - 1")
print("Показать задачи - 2")
print("Отметить выполнение задачи - 3")
print("Удалить задачу - 4")
print("выход - 0")

while True:
    try:
        person=int(input("Введите число:  "))
    except:
        print("Нужно ввести именно число")
        continue
    if person==1:
        add_task(tasks, input("Введите текст задачи:  "))
    if person ==2:
        list_tasks(tasks)
    if person == 3:
        complete_task(tasks, int(input("введите номер задачи:  ")))
    if person == 4:
        delete_task(tasks, int(input("Введите номер задачи которую хотите удалить")))
    if person == 0:
        break
    