import db_manager
from models.user import register_user, login_user
from models.menu import show_main_menu
from models.menu_authors import menu_authors
from ui.menu_publications import menu_publications
from ui.menu_references import menu_references
from ui.menu_reports import menu_reports
def auth_menu():
    while True:
        print("\n=== Вход в систему ===")
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            login = input("Логин: ")
            password = input("Пароль: ")
            user = login_user(login, password)
            if user:
                main_menu(user)
            else:
                print("Неверный логин или пароль.")
        elif choice == "2":
            login = input("Логин: ")
            password = input("Пароль: ")
            print("1. Сотрудник")
            print("2. Ответственный за учет публикаций")
            role_choice = input("Выберите роль: ")
            if role_choice == "1":
                role = "Сотрудник"
            elif role_choice == "2":
                role = "Ответственный за учет публикаций"
            else:
                print("Неверный выбор роли.")
                continue
            register_user(login, password, role)
            print("Пользователь зарегистрирован.")
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод.")
def main_menu(user):
    while True:
        choice = show_main_menu(user.role)
        if user.role == "Сотрудник":
            if choice == "1":
                menu_publications(user.role)
            elif choice == "0":
                break
            else:
                print("Неверный ввод.")
        elif user.role == "Ответственный за учет публикаций":
            if choice == "1":
                menu_publications(user.role)
            elif choice == "2":
                menu_authors()
            elif choice == "3":
                menu_references()
            elif choice == "4":
                menu_reports()
            elif choice == "0":
                break
            else:
                print("Неверный ввод.")
auth_menu()
