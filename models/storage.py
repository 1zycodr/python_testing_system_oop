from models.question import Question
import json 

class Storage:
    inst = None
    questions = None
    test_questions_number = None
    max_id = None


    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.inst is None:
            cls.inst = object.__new__(cls)
            cls.questions = []
            cls.test_questions_number = 0
            cls.max_id = 0
        return cls.inst


    def fill_storage(self):
        try: 
            with open('questions.json', 'r') as datafile:
                data = json.load(datafile)

            self.test_questions_number = data["test_questions_number"]   
            self.questions = [
                Question.from_dict(question_json) 
                for question_json in data["questions"]
            ]
            self.max_id = data["max_id"]
        except FileNotFoundError:
            print("No requested file 'questions.json'!")
        except KeyError:
            print('Invalid json. Requested format: { "questions": [], "test_questions_number" : <val>, "max_id" : <val> }')
        
        
    def fill_json(self):
        try: 
            data = {
                "questions": [
                    Question.to_dict(question)
                    for question in self.questions
                ],
                "test_questions_number": self.test_questions_number,
                "max_id": self.max_id
            }

            with open('questions.json', 'w') as datafile:
                json.dump(
                    data, 
                    datafile, 
                    indent=4, 
                    sort_keys=False, 
                    ensure_ascii=False
                )

        except FileNotFoundError:
            print("No requested file 'questions.json'!")
