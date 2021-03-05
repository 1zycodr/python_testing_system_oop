from menu.base_menu import BaseMenu
from models.storage import Storage
from models.question import Question
from utils import get_option_input, raise_exeption, get_id_input, get_confirm_input, get_test_questions_number
from exceptions import UserInputOptionException, ExitFromMenuException, InvalidInputIdException, InvalidInputTestQuestionsNumberException


class EditMenu(BaseMenu):
    header = '\n---------- Edit Menu ----------\n'
    options = '[1] - Create question\n[2] - Edit question\n[3] - Delete question\n[4] - Edit test questions number\n[5] - Back'


    def __init__(self):
        self.next_menus = {
            '1' : self.create_question,
            '2' : self.edit_question,
            '3' : self.delete_question, 
            '4' : self.edit_test_questions_number,
            '5' : lambda *_: raise_exeption(ExitFromMenuException)
        }


    @classmethod 
    def edit_test_questions_number(cls, storage):
        print('Current test questions number:', storage.test_questions_number)
        input_func = get_test_questions_number()

        def get_new_val():
            new_val = input_func('Enter new value (# - cancel): ')

            valid_questions = [
                question
                for question in storage.questions
                if len(question.answers) != 0
            ]

            if new_val.isdigit():
                if int(new_val) > len(valid_questions):
                    raise InvalidInputTestQuestionsNumberException
            else:
                if new_val != '#':
                    raise InvalidInputTestQuestionsNumberException
                
            return new_val

        new_val = cls.input_secure_wrap(get_new_val)

        if new_val == '#':
            input('Canceled!')
        else:
            storage.test_questions_number = int(new_val)
            storage.fill_json()
            input('Test questions number changed!')

    
    @staticmethod
    def list_questions(storage):
        for question in storage.questions:
            print(question)


    @staticmethod
    def create_question(storage):
        text = input('Enter question text: ')
        answers = []

        print('Enter correct answers (# - stop): ')

        while True:
            curr_answer = input('- ')

            if curr_answer in ('#', ''):
                break

            answers.append(curr_answer.lower())

        storage.max_id += 1

        storage.questions.append(
            Question(storage.max_id, text, answers)
        )

        storage.fill_json()

        input('Question created!')

    
    @classmethod
    def edit_question(cls, storage):
        id_input_func = get_id_input()

        def get_id():
            selected_id = id_input_func('Enter question id: ')

            ids = [
                question.id 
                for question in storage.questions
            ] 

            if selected_id not in ids:
                raise InvalidInputIdException

            return selected_id

        selected_id = cls.input_secure_wrap(get_id)
        
        edit_question_menu = EditQuestion(selected_id, storage)
        edit_question_menu.show()



    @classmethod
    def delete_question(cls, storage):
        id_input_func = get_id_input()
        confirm_input_func = get_confirm_input()


        def get_id():
            selected_id = id_input_func('Enter question id: ')

            ids = [
                question.id 
                for question in storage.questions
            ] 

            if selected_id not in ids:
                raise InvalidInputIdException

            return selected_id

        def confirm():
            return confirm_input_func("Are you sure? ('y' or 'n'): ")


            
        selected_id = cls.input_secure_wrap(get_id)
        conf = cls.input_secure_wrap(confirm)

        if conf == 'y':
            del_question = None

            for question in storage.questions:
                if question.id == selected_id:
                    del_question = question

            storage.questions.remove(del_question)

            storage.fill_json()

            input('Question deleted!')
        else:
            input('Delete canceled!')


    def show(self):
        storage = Storage()
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.header)
            self.list_questions(storage)
            print(self.options)

            selected_option = self.input_secure_wrap(get_input)

            try:
                self.next_menus[selected_option](storage)
            except ExitFromMenuException:
                return


class EditQuestion(BaseMenu):
    header = '\n---------- Question Edit Menu ----------\n'
    options = "[1] - New text\n[2] - New answers\n[3] - Reset statistics\n[4] - Exit"
     

    def __init__(self, question_id, storage=None):
        if storage is None:
            self.storage = Storage()
        else:
            self.storage = storage

        self.question = None

        for question in storage.questions:
            if question.id == question_id:
                self.question = question

        self.next_menus = {
            '1': self.new_text,
            '2': self.new_answers,
            '3': self.reset_statistics,
            '4': lambda *_: raise_exeption(ExitFromMenuException)
        }


    def show_question(self):
        print(self.question)       


    def new_text(self):
        new_text = input('Enter new text: ')
        self.question.text = new_text
        
        self.storage.fill_json()
        input('New text saved!')


    def new_answers(self):
        answers = []

        print('Enter new correct answers (# - stop): ')

        while True:
            curr_answer = input('- ')

            if curr_answer in ('#', ''):
                break

            answers.append(curr_answer.lower())
        
        self.question.answers = answers
        self.storage.fill_json()
        input('New answers saved!')


    def reset_statistics(self):
        self.question.stat_cor = 0
        self.question.stat_wrg = 0
        self.storage.fill_json()

        input('Statistics reset!')


    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.next_menus.keys():
                raise UserInputOptionException
            return selected_option
        
        while True:
            print(self.header)
            self.show_question()
            print(self.options)

            selected_option = self.input_secure_wrap(get_input)

            try:
                self.next_menus[selected_option]()
            except ExitFromMenuException:
                return