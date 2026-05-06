import db_manager
from menu import show_main_menu
from menu_authors import menu_authors
from menu_publications import menu_publications
from menu_references import menu_references
from menu_reports import menu_reports
def main():
    while True:
        user_choice = show_main_menu()
        if user_choice == "1":
            menu_authors()
        elif user_choice == "2":
          menu_publications()
        elif user_choice == "3":
            menu_references()
        elif user_choice == "4":
            menu_reports()
        elif user_choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод.")
main()
