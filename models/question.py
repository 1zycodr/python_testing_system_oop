class Question:
    __slots__ = ('id', 'text', 'answers', 'stat_cor', 'stat_wrg')

    def __init__(
        self, 
        id, 
        text, 
        answers=None, 
        stat_cor=0,
        stat_wrg=0
    ):
        self.id = id
        self.text = text
        self.stat_cor = stat_cor
        self.stat_wrg = stat_wrg

        if answers is None:
            self.answers = []
        else:
            self.answers = answers

    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)


    @staticmethod 
    def to_dict(inst):
        return {
            "id" : inst.id,
            "text": inst.text, 
            "answers": inst.answers,
            "stat_cor": inst.stat_cor,
            "stat_wrg": inst.stat_wrg
        }