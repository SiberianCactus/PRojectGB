import json

def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    note = {"title": title, "content": content}
    return note

def save_note(note):
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write("\n")

def read_notes():
    with open("notes.json", "r") as file:
        lines = file.readlines()
        for line in lines:
            note = json.loads(line)
            print("Заголовок:", note["title"])
            print("Содержимое:", note["content"])
            print()

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
            json.dump(note, file)
            file.write("\n")
        file.truncate()

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
# def create_note():
#     title = input("Введите заголовок заметки: ")
#     content = input("Введите текст заметки: ")
#     note = f"Заголовок: {title}\n\n{content}\n"
#     return note

# def save_note(note):
#     filename = input("Введите имя файла для сохранения заметки: ")
#     with open(filename, "w") as file:
#         file.write(note)
#     print(f"Заметка сохранена в файле {filename}")

# def read_notes():
#     files = os.listdir()
#     note_files = [file for file in files if file.endswith(".txt")]
#     if not note_files:
#         print("Нет доступных заметок.")
#         return
#     print("Список доступных заметок:")
#     for index, file in enumerate(note_files):
#         print(f"{index + 1}. {file}")
#     choice = int(input("Введите номер заметки для просмотра: "))
#     if choice < 1 or choice > len(note_files):
#         print("Некорректный выбор.")
#         return
#     with open(note_files[choice - 1], "r") as file:
#         note = file.read()
#     print("Содержимое заметки:")
#     print(note)

# def edit_note():
#     files = os.listdir()
#     note_files = [file for file in files if file.endswith(".txt")]
#     if not note_files:
#         print("Нет доступных заметок.")
#         return
#     print("Список доступных заметок:")
#     for index, file in enumerate(note_files):
#         print(f"{index + 1}. {file}")
#     choice = int(input("Введите номер заметки для редактирования: "))
#     if choice < 1 or choice > len(note_files):
#         print("Некорректный выбор.")
#         return
#     with open(note_files[choice - 1], "r") as file:
#         note = file.read()
#     print("Содержимое заметки:")
#     print(note)
#     new_note = create_note()
#     with open(note_files[choice - 1], "w") as file:
#         file.write(new_note)
#     print("Заметка успешно отредактирована.")

# def delete_note():
#     files = os.listdir()
#     note_files = [file for file in files if file.endswith(".txt")]
#     if not note_files:
#         print("Нет доступных заметок.")
#         return
#     print("Список доступных заметок:")
#     for index, file in enumerate(note_files):
#         print(f"{index + 1}. {file}")
#     choice = int(input("Введите номер заметки для удаления: "))
#     if choice < 1 or choice > len(note_files):
#         print("Некорректный выбор.")
#         return
#     os.remove(note_files[choice - 1])
#     print("Заметка успешно удалена.")

# def main():
#     while True:
#         print("\nМеню:")
#         print("1. Создать заметку")
#         print("2. Сохранить заметку")
#         print("3. Просмотреть список заметок")
#         print("4. Редактировать заметку")
#         print("5. Удалить заметку")
#         print("6. Выйти из программы")
#         choice = input("Выберите действие: ")
#         if choice == "1":
#             note = create_note()
#             print(note)
#         elif choice == "2":
#             note = create_note()
#             save_note(note)
#         elif choice == "3":
#             read_notes()
#         elif choice == "4":
#             edit_note()
#         elif choice == "5":
#             delete_note()
#         elif choice == "6":
#             print("Программа завершена.")
#             break
#         else:
#             print("Некорректный выбор.")

# if __name__ == "__main__":
#     main()