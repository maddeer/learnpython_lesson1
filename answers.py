#!/usr/bin/python3

def get_answers(question):
    answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answers.get(str(question).lower(),'No Answer')

print(get_answers('привет'))
print(get_answers('как дела'))
print(get_answers('пока'))
print(get_answers('2'))


