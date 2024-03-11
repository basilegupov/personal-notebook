import json
from textwrap import wrap
from virtual_assistant_v007.colors import *
from datetime import datetime


def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=2)


def wrap_text(text, width):
    return '\n'.join(wrap(text, width))


def add_note():
    title = input("Введіть заголовок нотатки: ")
    content = input("Введіть текст нотатки: ")
    tags = input("Введіть теги (через пробіл): ").split()
    
    notes = load_notes()
    modified = datetime.strftime(datetime.now(), "%d/%m/%Y, %H:%M")
    notes.append({'title': title, 'content': content, 'tags': tags, 'modified': modified})
    save_notes(notes)
    print("Нотатка додана успішно!")


def search_notes(query):
    notes = load_notes()
    found_notes = [
        note for note in notes if query.lower() in note['title'].lower()
        or query.lower() in note['content'].lower()
    ]
    
    if found_notes:
        display_notes_in_table(found_notes)
    else:
        print("Нотаток не знайдено.")


def filter_by_tag(tag):
    notes = load_notes()
    filtered_notes = [note for note in notes if tag in note['tags']]

    if filtered_notes:
        display_notes_in_table(filtered_notes)
    else:
        print(f"Нотаток з тегом '{tag}' не знайдено.")


def display_all_notes():
    notes = load_notes()
    display_notes_in_table(notes)


def display_notes_by_tag(tag):
    notes = load_notes()
    filtered_notes = [note for note in notes if tag in note['tags']]
    display_notes_in_table(filtered_notes)


def display_notes_by_tags_in_table(tags):
    notes = load_notes()
    filtered_notes = [note for note in notes if all(tag in note['tags'] for tag in tags)]
    display_notes_in_table(filtered_notes)


def display_note_by_title(title):
    notes = load_notes()
    for note in notes:
        if note['title'].lower() == title.lower():
            display_notes_in_table([note])
            return
    print(f"Нотатка з заголовком '{title}' не знайдена.")


def edit_note():
    notes = load_notes()
    title_to_edit = input("Введіть заголовок нотатки, яку ви хочете відредагувати: ")

    for note in notes:
        if note['title'] == title_to_edit:
            print(f"Знайдено нотатку з заголовком '{title_to_edit}'.")
            new_title = input("Введіть новий заголовок (або залиште порожнім, щоб залишити без змін): ")
            new_content = input("Введіть новий текст (або залиште порожнім, щоб залишити без змін): ")
            new_tags = input("Введіть нові теги (через пробіл, або залиште порожнім, щоб залишити без змін): ").split()

            note['title'] = new_title if new_title else note['title']
            note['content'] = new_content if new_content else note['content']
            note['tags'] = new_tags if new_tags else note['tags']
            note['modified'] = datetime.strftime(datetime.now(), "%d/%m/%Y, %H:%M")

            save_notes(notes)
            print("Нотатка відредагована успішно!")
            return

    print(f"Нотатка з заголовком '{title_to_edit}' не знайдена.")


def delete_note():
    notes = load_notes()
    title_to_delete = input("Введіть заголовок нотатки, яку ви хочете видалити: ")

    for note in notes:
        if note['title'] == title_to_delete:
            notes.remove(note)
            save_notes(notes)
            print(f"Нотатка з заголовком '{title_to_delete}' видалена успішно!")
            return

    print(f"Нотатка з заголовком '{title_to_delete}' не знайдена.")


def display_note(title):
    notes = load_notes()

    for note in notes:
        if note['title'] == title:
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['content']}")
            print(f"Теги: {', '.join(note['tags'])}")
            print(f"Змінено: {note['modified']}")
            return

    print(f"Нотатка з заголовком '{title}' не знайдена.")


def display_notes_in_table(notes):
    if not notes:
        print("Список нотаток порожній.")
        return

    column_widths = {
        'title': max(len(note['title']) for note in notes),
        'content': max(len(note['content']) for note in notes),
        'tags': max(len(', '.join(note['tags'])) for note in notes),
        'modified': max(len(note['modified']) for note in notes),
    }

    print("\nНотатки:")
    print('-' * (sum(column_widths.values()) + len(column_widths) * 5 - 1))
    print(
        f"| {'Заголовок': <{column_widths['title'] + 5}} | "
        f"{'Текст': <{column_widths['content']}} | "
        f"{'Теги': <{column_widths['tags']}} | "
        f"{'Змінено': <{column_widths['modified']}} |"
    )
    print('-' * (sum(column_widths.values()) + len(column_widths) * 5 - 1))
    
    for note in notes:
        print(
            f"| {note['title']: <{column_widths['title'] + 5}} | "
            f"{note['content']: <{column_widths['content']}} | "
            f"{', '.join(note['tags']): <{column_widths['tags']}} | "
            f"{note['modified']: <{column_widths['modified']}} |"
        )

    print('-' * (sum(column_widths.values()) + len(column_widths) * 5 - 1))


def run_notes():
    while True:
        print(f"{GREEN}\n1. Додати нотатку")
        print(f"2. Пошук нотаток")
        print(f"3. Редагувати нотатку")
        print(f"{RED}4. Видалити нотатку{DEFALUT}")
        print(f"{GREEN}5. Вивести всі нотатки в консоль")
        print(f"6. Вивести одну нотатку за заголовком")
        print(f"7. Вивести нотатку(-и) за тегом")
        print(f"8. Вивести нотатку за тегами в таблиці")
        print(f"{RED}9. Вийти{DEFALUT}")

        choice = input("Введіть номер опції: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            query = input("Введіть запит для пошуку: ")
            search_notes(query)
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            display_all_notes()
        elif choice == '6':
            title_to_display = input("Введіть заголовок нотатки для виведення в консоль: ")
            display_note_by_title(title_to_display)
        elif choice == '7':
            tag_to_display = input("Введіть тег для виведення нотаток: ")
            display_notes_by_tag(tag_to_display)
        elif choice == '8':
            tags_to_display = input("Введіть теги через пробіл для виведення нотаток в таблице: ").split()
            display_notes_by_tags_in_table(tags_to_display)
        elif choice == '9':
            return
        else:
            print("Невірний вибір. Спробуйте ще раз.")


def main():
    run_notes()


if __name__ == "__main__":
    main()
