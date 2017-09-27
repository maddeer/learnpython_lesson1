#!/usr/bin/python3

def get_answers(question):
    answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    answer="""Q:{} 
A:{}""".format(question,answers.get(str(question).lower(),'No Answer'))
    return answer
print(__name__)
if __name__ == '__main__':
    print(get_answers('привет'))
    print(get_answers('как дела'))
    print(get_answers('пока'))
    print(get_answers('2'))


