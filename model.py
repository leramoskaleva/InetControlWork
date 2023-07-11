import json
import datetime

# Функция для сохранения данных в json файл
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

# Функция для чтения данных из json файла
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Функция для вывода на экран списка заметок
def display_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['body']}")
        print(f"Дата/время: {note['timestamp']}")
        print('---')

# Функция для добавления новой заметки
def add_note():
    notes = load_notes()
    id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена!")

# Функция для выборки заметок по дате
def get_notes_by_date():
    notes = load_notes()
    date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    filtered_notes = [note for note in notes if note['timestamp'].startswith(date)]
    if filtered_notes:
        display_notes(filtered_notes)
    else:
        print("Заметок на указанную дату не найдено")

# Функция для вывода одной заметки по ID
def get_note_by_id():
    notes = load_notes()
    id = int(input("Введите ID заметки: "))
    note = next((note for note in notes if note['id'] == id), None)
    if note:
        print("Заметка найдена:")
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['body']}")
        print(f"Дата/время: {note['timestamp']}")
    else:
        print("Заметка с указанным ID не найдена")

# Функция для редактирования заметки
def edit_note():
    notes = load_notes()
    id = int(input("Введите ID заметки для редактирования: "))
    note = next((note for note in notes if note['id'] == id), None)
    if note:
        print("Редактирование заметки:")
        print(f"Старый заголовок: {note['title']}")
        new_title = input("Введите новый заголовок заметки: ")
        print(f"Старое тело: {note['body']}")
        new_body = input("Введите новое тело заметки: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note['title'] = new_title
        note['body'] = new_body
        note['timestamp'] = timestamp

        save_notes(notes)
        print("Заметка успешно отредактирована!")
    else:
        print("Заметка с указанным ID не найдена")

# Функция для удаления заметки
def delete_note():
    notes = load_notes()
    id = int(input("Введите ID заметки для удаления: "))
    note = next((note for note in notes if note['id'] == id), None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("Заметка успешно удалена!")
    else:
        print("Заметка с указанным ID не найдена")
