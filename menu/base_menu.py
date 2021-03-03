from exceptions import UserInputOptionException
from utils import get_option_input

class BaseMenu:
    header = None
    options = None
    next_menus = None

    @staticmethod
    def input_secure_wrap(input_func, *args, **kwargs):
        while True:
            try:
                return input_func(*args, **kwargs)
            except UserInputOptionException:
                print('Incorrect option.')
            except Exception as ex:
                print('Something wrong!')
                print(ex)

    def show(self):
        raise NotImplementedError
        
