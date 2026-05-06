import db_manager
from ui.menu import show_main_menu
from ui.menu_authors import menu_authors
from ui.menu_publications import menu_publications
from ui.menu_references import menu_references
from ui.menu_reports import menu_reports
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
