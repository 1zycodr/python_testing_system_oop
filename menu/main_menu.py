from menu.base_menu import BaseMenu
from menu.test_menu import TestMenu
from menu.edit_menu import EditMenu
from utils import get_option_input, raise_exeption
from exceptions import UserInputOptionException


class MainMenu(BaseMenu):
    header = '---------- Main Menu ----------'
    options = '[1] - Start test\n[2] - Edit questions\n[3] - Exit'
    next_menus = {
        '1': TestMenu,
        '2': EditMenu,
        '3': lambda: raise_exeption(KeyboardInterrupt)
    }

    def show(self):
        input_func = get_option_input()
            
        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.header)
            print(self.options)
            
            selected_option = self.input_secure_wrap(get_input)

            next_menu = self.next_menus[selected_option]()
            next_menu.show()
