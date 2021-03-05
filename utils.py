from exceptions import UserInputOptionException, InvalidInputIdException, InvalidInputConfirmException


def option_input(string):
    result = input(string)
    if not result.isdigit():
        raise UserInputOptionException
    return result


def confirm_input(string):
    result = input(string)
    if result not in ('y', 'n'):
        raise InvalidInputConfirmException
    return result


def id_input(string):
    try:
        result = int(input(string))
        if result <= 0:
            raise InvalidInputIdException
    except ValueError:
        raise InvalidInputIdException
    
    return result

def test_questions_number(string):
    return input(string)
    

def get_option_input():
    try:
        input_function = option_input
    except NameError:
        input_function = input
    
    return input_function


def get_id_input():
    try:
        input_function = id_input
    except NameError:
        input_function = input
    
    return input_function


def get_confirm_input():
    try:
        input_function = confirm_input
    except NameError:
        input_function = input
    
    return input_function

    
def get_test_questions_number():
    try:
        input_function = test_questions_number
    except NameError:
        input_function = input
    
    return input_function


def raise_exeption(ex):
    raise ex
    

