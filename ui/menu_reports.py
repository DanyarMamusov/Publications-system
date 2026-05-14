from models.reports import (
    get_publication_count_by_author,
    get_publication_count_by_type,
    get_publication_count_by_status)
from models.publication import get_publications_full_info
def menu_reports():
    while True:
        print("\n=== Отчеты и статистика ===")
        print("1. Общий реестр публикаций")
        print("2. Количество публикаций по авторам")
        print("3. Количество публикаций по типам")
        print("4. Количество публикаций по статусам")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == "1":
            publications = get_publications_full_info()
            if not publications:
                print("Реестр публикаций пуст.")
            else:
                print("\n=== Общий реестр научных публикаций ===")
                for publication in publications:
                    print(
                        f"{publication[0]}. {publication[1]} | "
                        f"Дата: {publication[2] or '-'} | "
                        f"Тип: {publication[5] or '-'} | "
                        f"Источник: {publication[6] or '-'} | "
                        f"Статус: {publication[7] or '-'} | "
                        f"Автор: {publication[8] or '-'}")
        elif choice == "2":
            rows = get_publication_count_by_author()
            print("\n=== Количество публикаций по авторам ===")
            for row in rows:
                print(f"{row[0]} — {row[1]}")
        elif choice == "3":
            rows = get_publication_count_by_type()
            print("\n=== Количество публикаций по типам ===")
            for row in rows:
                print(f"{row[0]} — {row[1]}")
        elif choice == "4":
            rows = get_publication_count_by_status()
            print("\n=== Количество публикаций по статусам ===")
            for row in rows:
                print(f"{row[0]} — {row[1]}")
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")
