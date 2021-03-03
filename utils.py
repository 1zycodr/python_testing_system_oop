from exceptions import UserInputOptionException


def option_input(string):
    result = input(string)
    if not result.isdigit():
        raise UserInputOptionException
    return result


def get_option_input():
    try:
        input_function = option_input
    except NameError:
        input_function = input
    
    return input_function


def raise_exeption(ex):
    raise ex
    