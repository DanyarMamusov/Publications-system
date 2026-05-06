from models.references import (
    get_all_publication_types,
    add_publication_type,
    delete_publication_type,
    get_all_publication_sources,
    add_publication_source,
    delete_publication_source,
    get_all_publication_statuses,
    add_publication_status,
    delete_publication_status
)


def menu_references():
    while True:
        print("\n=== Управление справочниками ===")
        print("1. Типы публикаций")
        print("2. Источники публикаций")
        print("3. Статусы публикаций")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == "1":
            menu_publication_types()
        elif choice == "2":
            menu_publication_sources()
        elif choice == "3":
            menu_publication_statuses()
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")


def menu_publication_types():
    while True:
        print("\n=== Типы публикаций ===")
        print("1. Показать типы публикаций")
        print("2. Добавить тип публикации")
        print("3. Удалить тип публикации")
        print("0. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            types = get_all_publication_types()
            if not types:
                print("Список типов публикаций пуст.")
            else:
                for item in types:
                    print(f"{item[0]}. {item[1]}")
        elif choice == "2":
            type_name = input("Введите название типа публикации: ")
            add_publication_type(type_name)
            print("Тип публикации добавлен.")
        elif choice == "3":
            type_id = int(input("Введите ID типа публикации для удаления: "))
            delete_publication_type(type_id)
            print("Тип публикации удален.")
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")


def menu_publication_sources():
    while True:
        print("\n=== Источники публикаций ===")
        print("1. Показать источники публикаций")
        print("2. Добавить источник публикации")
        print("3. Удалить источник публикации")
        print("0. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            sources = get_all_publication_sources()
            if not sources:
                print("Список источников публикаций пуст.")
            else:
                for source in sources:
                    print(
                        f"{source[0]}. {source[1]} | "
                        f"Издатель: {source[2] or '-'} | "
                        f"Место публикации: {source[3] or '-'} | "
                        f"ISSN/ISBN: {source[4] or '-'}"
                    )
        elif choice == "2":
            source_title = input("Название источника: ")
            publisher = input("Издатель: ")
            publication_place = input("Место публикации: ")
            issn_isbn = input("ISSN/ISBN: ")
            add_publication_source(
                source_title,
                publisher,
                publication_place,
                issn_isbn
            )
            print("Источник публикации добавлен.")
        elif choice == "3":
            source_id = int(input("Введите ID источника для удаления: "))
            delete_publication_source(source_id)
            print("Источник публикации удален.")
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")


def menu_publication_statuses():
    while True:
        print("\n=== Статусы публикаций ===")
        print("1. Показать статусы")
        print("2. Добавить статус")
        print("3. Удалить статус")
        print("0. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            statuses = get_all_publication_statuses()
            if not statuses:
                print("Список статусов пуст.")
            else:
                for status in statuses:
                    print(f"{status[0]}. {status[1]}")
        elif choice == "2":
            status_name = input("Введите название статуса: ")
            add_publication_status(status_name)
            print("Статус добавлен.")
        elif choice == "3":
            status_id = int(input("Введите ID статуса для удаления: "))
            delete_publication_status(status_id)
            print("Статус удален.")
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")
