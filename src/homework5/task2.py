# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)
import datetime


def call_time():
    result = []
    try:
        with open('result_storage.txt', 'a') as fh:
            calltime = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
            fh.write('function was called at: ' + calltime + '\n')
            result.append(calltime)
    except IOError:
        with open('result_storage.txt', 'w') as fh:
            calltime = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
            fh.write('function was called at: ' + calltime + '\n')
            result.append(calltime)


call_time()
