import json
from datetime import datetime

FILE = "tasks.json"

def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save(items):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def add_item():
    name = input("Название задачи: ")
    status = input("Статус задачи (new, in_progress, done): ")
    
    items = load()
    items.append({
        "name": name,
        "status": status,
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    save(items)
    print("Задача добавлена!")

def report():
    items = load()
    if not items:
        print("Список пуст")
        return

    print("\nТвои задачи:")
    for i, task in enumerate(items, start=1):
        status_icon = "✅" if task["status"] == "done" else "⏳" if task["status"] == "in_progress" else "🆕"
        print(f"{i}. {status_icon} {task['name']} | {task['status']} | {task['date']}")

def delete_item():
    report()  
    try:
        idx = int(input("Введи номер задачи для удаления: ")) - 1
        items = load()
        
        if 0 <= idx < len(items):
            removed = items.pop(idx)
            save(items)
            print(f"Задача удалена: {removed['name']}")
        else:
            print("Такого номера нет.")
    except ValueError:
        print("Вводи только число.")

while True:
    print("\n1. Добавить задачу\n2. Показать задачи\n3. Удалить задачу\n4. Выход")
    choice = input("Выбери: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        report()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        print("До встречи!")
        break
    else:
        print("Неверный выбор, попробуй ещё раз.")
