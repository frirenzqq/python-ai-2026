expenses = []

def add_expense(expenses, value):
    expenses.append(value)
    print("Расход добавлен")

def total_expenses(expenses):
    if expenses:
        print("сумма расходов:", sum(expenses))
    else:
        print("Расходов пока нет")
    
    
def show_expenses(expenses):
    if expenses:
        print("Ваши расходы:")
        for number, expense in enumerate(expenses, start=1):
            print(number, expense)
    else:
        print("Расходов пока нет")
        
print("Добавить расход - 1")
print("Показать сумму расходов - 2")
print("Показать все расходы - 3")
print("Выход - 0")


while True:
    try:
        person=int(input(" Введите число:  "))
    except:
        print("Нужно ввести число  ")
        continue

    if person==1:
        try:
            value=int(input("Введите расход:  "))
        except:
            print("Нужно ввести число")
            continue
        add_expense(expenses, value)
        
    elif person==2:
        total_expenses(expenses)
        
    elif person==3:
        show_expenses(expenses)
    elif person ==0:
        print("Вы вышли")
        break
    else:
        print("Ошибка")