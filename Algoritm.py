from WorkDock import *

def print_instructions():
    print ('Выберите действие: \n 1 - Записать данные в файл \n 2 - Печать всех данных \n 3 - Поиск по фамилии  \n -1 - Выйти')

            


def choose(choice):
    if choice == '1': return write(input('Введите ваши данные:'))  
    if choice == '2': return read_all() 
    if choice == '3': return get_by_name(input('Введите имя, фамилию или Номер телефона: '))
    if choice == '-1': exit()



