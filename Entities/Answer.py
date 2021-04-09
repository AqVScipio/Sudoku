import json

class Answer:
    def __init__(self):
        self.setAnswers([])
        self.setValid(False)

    def getAnswer(self, index = -1):
        if index >= 0: return self.__answers[index]
        return self.__answers

    def setAnswer(self, value):
        if value in self.__answers:
            self.__answers.remove(value)
        else:
            self.__answers.append(value)
            # Whenever an answer is set, the valid property is set to False
            self.setValid(False)

    def getValid(self):
        return self.__valid
    
    def setValid(self, value):
        self.__valid = value

    def setAnswers(self, answers):
        self.__answers = answers