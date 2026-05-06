from models.author import get_all_authors
from models.authorship import Authorship
from models.publication import (
    Publication,
    get_publication_by_id,
    get_publications_full_info,
    update_publication_status)
from models.references import (
    get_all_publication_types,
    get_all_publication_sources,
    get_all_publication_statuses,
    get_status_id_by_name)


def print_publications():
    publications = get_publications_full_info()
    if not publications:
        print("Список публикаций пуст.")
        return
    print("\nСписок публикаций:")
    for publication in publications:
        print(
            f"{publication[0]}. {publication[1]} | "
            f"Дата: {publication[2] or '-'} | "
            f"DOI: {publication[3] or '-'} | "
            f"Ссылка: {publication[4] or '-'} | "
            f"Тип: {publication[5] or '-'} | "
            f"Источник: {publication[6] or '-'} | "
            f"Статус: {publication[7] or '-'} | "
            f"Автор: {publication[8] or '-'}"
        )


def choose_author():
    authors = get_all_authors()
    if not authors:
        print("Сначала необходимо добавить автора.")
        return None
    print("\nДоступные авторы:")
    for author in authors:
        print(f"{author.id}. {author.surname} {author.name} {author.middle_name or ''}")
    return int(input("Введите ID автора: "))


def choose_type():
    types = get_all_publication_types()
    if not types:
        print("Сначала необходимо добавить тип публикации.")
        return None
    print("\nДоступные типы публикаций:")
    for item in types:
        print(f"{item[0]}. {item[1]}")
    return int(input("Введите ID типа публикации: "))


def choose_source():
    sources = get_all_publication_sources()
    if not sources:
        print("Сначала необходимо добавить источник публикации.")
        return None
    print("\nДоступные источники публикаций:")
    for source in sources:
        print(f"{source[0]}. {source[1]}")
    return int(input("Введите ID источника публикации: "))


def choose_status():
    statuses = get_all_publication_statuses()
    if not statuses:
        print("Сначала необходимо добавить статус публикации.")
        return None
    print("\nДоступные статусы публикаций:")
    for status in statuses:
        print(f"{status[0]}. {status[1]}")
    return int(input("Введите ID статуса публикации: "))


def menu_publications():
    while True:
        print("\n=== Управление публикациями ===")
        print("1. Показать все публикации")
        print("2. Добавить публикацию")
        print("3. Изменить публикацию")
        print("4. Удалить публикацию")
        print("5. Отправить публикацию на проверку")
        print("6. Одобрить публикацию")
        print("7. Отправить публикацию на доработку")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == "1":
            print_publications()
        elif choice == "2":
            print("\n=== Добавление публикации ===")
            title = input("Название публикации: ")
            date = input("Дата публикации: ")
            doi = input("DOI: ")
            link = input("Ссылка: ")
            author_id = choose_author()
            if author_id is None:
                continue
            type_id = choose_type()
            if type_id is None:
                continue
            source_id = choose_source()
            if source_id is None:
                continue
            status_id = get_status_id_by_name("На проверке")
            if status_id is None:
                print("Статус 'На проверке' не найден.")
                print("Выберите статус вручную.")
                status_id = choose_status()
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
            print("Публикация добавлена и отправлена на проверку.")
        elif choice == "3":
            publication_id = int(input("Введите ID публикации для редактирования: "))
            publication = get_publication_by_id(publication_id)
            if not publication:
                print("Публикация не найдена.")
                continue
            print("Оставьте поле пустым, чтобы не изменять значение.")
            title = input(f"Название ({publication.title}): ")
            date = input(f"Дата ({publication.date or '-'}): ")
            doi = input(f"DOI ({publication.doi or '-'}): ")
            link = input(f"Ссылка ({publication.link or '-'}): ")
            publication.title = title if title else publication.title
            publication.date = date if date else publication.date
            publication.doi = doi if doi else publication.doi
            publication.link = link if link else publication.link
            publication.save()
            print("Публикация обновлена.")
        elif choice == "4":
            publication_id = int(input("Введите ID публикации для удаления: "))
            publication = get_publication_by_id(publication_id)
            if not publication:
                print("Публикация не найдена.")
                continue
            publication.delete()
            print("Публикация удалена.")
        elif choice == "5":
            publication_id = int(input("Введите ID публикации: "))
            status_id = get_status_id_by_name("На проверке")
            if status_id is None:
                print("Статус 'На проверке' не найден.")
                continue
            update_publication_status(publication_id, status_id)
            print("Публикация отправлена на проверку.")
        elif choice == "6":
            publication_id = int(input("Введите ID публикации: "))
            status_id = get_status_id_by_name("Одобрена")
            if status_id is None:
                print("Статус 'Одобрена' не найден.")
                continue
            update_publication_status(publication_id, status_id)
            print("Публикация одобрена.")
        elif choice == "7":
            publication_id = int(input("Введите ID публикации: "))
            status_id = get_status_id_by_name("На доработке")
            if status_id is None:
                print("Статус 'На доработке' не найден.")
                continue
            update_publication_status(publication_id, status_id)
            print("Публикация отправлена на доработку.")
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")
