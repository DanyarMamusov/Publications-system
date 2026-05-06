from models.author import Author, get_all_authors, get_author_by_id
def menu_authors():
    while True:
        print("\n=== Управление авторами ===")
        print("1. Показать всех авторов")
        print("2. Добавить автора")
        print("3. Изменить автора")
        print("4. Удалить автора")
        print("0. Назад в главное меню")
        choice = input("Выберите действие:")
        
        if choice == "1":
            authors = get_all_authors()
            if not authors:
                print("Список авторов пуст")
            else:
                print("\nСписок авторов:")
                for author in authors:
                    print(f"{author.id}. {author.surname} {author.name} {author.middle_name or ''} | Должность: {author.position} Подразделение: {authors.department} Email: {author.email or '-'} ")
        elif choice == "2":
            print("\nДобавление автора")
            surname = input("Фамилия: ")
            name = input("Имя: ")
            middle_name = input("Отчество: ")
            position = input("Должность: ")
            department = input("Подразделение: ")
            email = input("Электронная почта: ")
            author = Author(name = name, surname = surname, middle_name = middle_name, position = position, department = department, email = email)
            author.save()
            print("Автор добавлен")
        elif choice == "3":
            author_id = int(input("Введите ID автора для редактирования: "))
            author = get_author_by_id(author_id)
            if not author:
                print("Автор не найден.")
                continue
            print("Оставьте поле пустым, если изменение не требуется.")
            surname = input(f"Фамилия ({author.surname}): ")
            name = input(f"Имя ({author.name}): ")
            middle_name = input(f"Отчество ({author.middle_name or '-'}): ")
            position = input(f"Должность ({author.position or '-'}): ")
            department = input(f"Подразделение ({author.department or '-'}): ")
            email = input(f"Email ({author.email or '-'}): ")
            author.surname = surname if surname else author.surname
            author.name = name if name else author.name
            author.middle_name = middle_name if middle_name else author.middle_name
            author.position = position if position else author.position
            author.department = department if department else author.department
            author.email = email if email else author.email
            author.save()
            print("Данные обновлены")
        elif choice == "4":
            author_id = int(input("Введите ID автора для удаления: "))
            author = get_author_by_id(author_id)
            if not author:
                print("Автор не найден.")
                continue
            author.delete()
            print("Автор удален.")
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")
