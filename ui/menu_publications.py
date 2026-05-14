from models.author import get_all_authors
from models.authorship import Authorship, get_authorship_by_id
from models.publication import (
    Publication,
    get_publication_by_id,
    get_publications_full_info,
    update_publication_status)
from models.references import (
    get_all_publication_types,
    get_all_publication_sources,
    get_status_id_by_name)
def print_publications():
    publications = get_publications_full_info()
    if not publications:
        print("Список публикаций пуст.")
        return
    print("\nСписок публикаций:")
    for p in publications:
        print(
            f"{p[0]}. {p[1]} | "
            f"Дата: {p[2] or '-'} | "
            f"DOI: {p[3] or '-'} | "
            f"Ссылка: {p[4] or '-'} | "
            f"Тип: {p[5] or '-'} | "
            f"Источник: {p[6] or '-'} | "
            f"Статус: {p[7] or '-'} | "
            f"Автор: {p[8] or '-'}")
def choose_author():
    authors = get_all_authors()
    if not authors:
        print("Список авторов пуст. Ответственный должен добавить автора.")
        return None
    print("\nДоступные авторы:")
    for a in authors:
        print(f"{a.id}. {a.surname} {a.name} {a.middle_name or ''}")
    return int(input("Введите ID автора: "))
def choose_type():
    types = get_all_publication_types()
    if not types:
        print("Список типов публикаций пуст.")
        return None
    print("\nДоступные типы публикаций:")
    for t in types:
        print(f"{t[0]}. {t[1]}")
    return int(input("Введите ID типа публикации: "))
def choose_source():
    sources = get_all_publication_sources()
    if not sources:
        print("Список источников публикаций пуст.")
        return None
    print("\nДоступные источники публикаций:")
    for s in sources:
        print(f"{s[0]}. {s[1]}")
    return int(input("Введите ID источника публикации: "))
def add_publication():
    print("\n=== Добавление публикации ===")
    title = input("Название публикации: ")
    date = input("Дата публикации: ")
    doi = input("DOI: ")
    link = input("Ссылка: ")
    author_id = choose_author()
    if author_id is None:
        return
    type_id = choose_type()
    if type_id is None:
        return
    source_id = choose_source()
    if source_id is None:
        return
    status_id = get_status_id_by_name("На проверке")
    if status_id is None:
        print("Статус 'На проверке' не найден. Добавьте его в справочник статусов.")
        return
    authorship = Authorship(author_id=author_id)
    authorship.save()
    publication = Publication(
        title=title,
        date=date,
        doi=doi,
        link=link,
        type_id=type_id,
        source_id=source_id,
        status_id=status_id,
        authorship_id=authorship.id)
    publication.save()
    print("Публикация добавлена со статусом 'На проверке'.")
def delete_publication():
    publication_id = int(input("Введите ID публикации для удаления: "))
    publication = get_publication_by_id(publication_id)
    if not publication:
        print("Публикация не найдена.")
        return
    publication.delete()
    print("Публикация удалена.")
def edit_publication_main_data():
    publication_id = int(input("Введите ID публикации: "))
    publication = get_publication_by_id(publication_id)
    if not publication:
        print("Публикация не найдена.")
        return
    print("Оставьте поле пустым, чтобы не изменять значение.")
    title = input(f"Название ({publication.title}): ")
    date = input(f"Дата ({publication.date or '-'}): ")
    doi = input(f"DOI ({publication.doi or '-'}): ")
    link = input(f"Ссылка ({publication.link or '-'}): ")
    publication.title = title if title else publication.title
    publication.date = date if date else publication.date
    publication.doi = doi if doi else publication.doi
    publication.link = link if link else publication.link
    print("\nИзменить автора? 1 - да, 0 - нет")
    if input("Выберите действие: ") == "1":
        author_id = choose_author()
        if author_id is not None:
            authorship = get_authorship_by_id(publication.authorship_id)
            if authorship:
                authorship.author_id = author_id
                authorship.save()
    print("\nИзменить тип публикации? 1 - да, 0 - нет")
    if input("Выберите действие: ") == "1":
        type_id = choose_type()
        if type_id is not None:
            publication.type_id = type_id
    print("\nИзменить источник публикации? 1 - да, 0 - нет")
    if input("Выберите действие: ") == "1":
        source_id = choose_source()
        if source_id is not None:
            publication.source_id = source_id
    publication.save()
    print("Данные публикации обновлены.")
def change_publication_status(status_name):
    publication_id = int(input("Введите ID публикации: "))
    status_id = get_status_id_by_name(status_name)
    if status_id is None:
        print(f"Статус '{status_name}' не найден.")
        return
    update_publication_status(publication_id, status_id)
    print(f"Статус публикации изменен на '{status_name}'.")
def menu_publications(role):
    while True:
        print("\n=== Управление публикациями ===")
        if role == "Сотрудник":
            print("1. Показать все публикации")
            print("2. Добавить публикацию")
            print("3. Изменить публикацию")
            print("0. Назад")
            choice = input("Выберите действие: ")
            if choice == "1":
                print_publications()
            elif choice == "2":
                add_publication()
            elif choice == "3":
                edit_publication_main_data()
            elif choice == "0":
                break
            else:
                print("Неверный ввод.")
        elif role == "Ответственный за учет публикаций":
            print("1. Показать все публикации")
            print("2. Одобрить публикацию")
            print("3. Отправить публикацию на доработку")
            print("4. Удалить публикацию")
            print("0. Назад")
            choice = input("Выберите действие: ")
            if choice == "1":
                print_publications()
            elif choice == "2":
                change_publication_status("Одобрена")
            elif choice == "3":
                change_publication_status("На доработке")
            elif choice == "4":
                delete_publication()
            elif choice == "0":
                break
            else:
                print("Неверный ввод.")
