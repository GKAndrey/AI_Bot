try:
    from work_db.db import *
    from modules.imprt_prog import *

except ModuleNotFoundError:
    from Engine.work_db.db import *
    from Engine.modules.imprt_prog import *


def go_programm():
    index = 1
    print("Приветствую, вы общаетесь с тестовой версией разговорного искуственного интелекта.",
          "Предупреждение! Все сказанное вами будет записасано.",
          "Соблюдайте нормальные нормы и помните, что бот учится на ваших ответах. \n")
    answer = input('Ваше сообщение первое. Чтоб закончить разговор, закончите сообщение символами "пока." \n')

    while "пока." not in answer:
        mess_list.append(Mess(msg=answer, index=index))
        index += 1
        answer = input()
        answer.lower()
