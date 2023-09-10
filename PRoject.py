import json
from datetime import datetime


def save_note(note):
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write("\n")

def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"title": title, "content": content, "created_at": created_at, "updated_at": None}
    return note

def edit_note():
    title = input("Введите заголовок заметки, которую хотите отредактировать: ")
    with open("notes.json", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            note = json.loads(line)
            if note["title"] == title:
                content = input("Введите новое содержимое заметки: ")
                note["content"] = content
                note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            json.dump(note, file)
            file.write("\n")
        file.truncate()

def read_notes():
    with open("notes.json", "r") as file:
        lines = file.readlines()
        for line in lines:
            note = json.loads(line)
            print("Заголовок:", note["title"])
            print("Содержимое:", note["content"])
            print()


def delete_note():
    title = input("Введите заголовок заметки, которую хотите удалить: ")
    with open("notes.json", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            note = json.loads(line)
            if note["title"] != title:
                json.dump(note, file)
                file.write("\n")
        file.truncate()

def menu():
    print("1. Создать заметку")
    print("2. Сохранить заметку")
    print("3. Просмотреть список заметок")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("6. Выйти")

menu()
while True:
    choice = input("Выберите пункт меню: ")
    if choice == "1":
        note = create_note()
    elif choice == "2":
        save_note(note)
    elif choice == "3":
        read_notes()
    elif choice == "4":
        edit_note()
    elif choice == "5":
        delete_note()
    elif choice == "6":
        break
    else:
        print("Неверный пункт меню. Попробуйте еще раз.")