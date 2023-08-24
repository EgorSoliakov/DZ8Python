from WorkDock import *
from WorkChange import *
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')


def print_instructions():
    print ('Выберите действие: \n 1 - Записать данные в файл \n 2 - Печать всех данных \n 3 - Поиск по фамилии  \n 4 - Изменить данные \n 5 - Удалить данные \n -1 - Выйти')

# def change_data(name):
#     clear()
#     get_by_name(name)
#     n = print (' Выберите действие: \n 1 - Изменить Фамилию \n 2 - Изменить Имя \n 3 - Изменить отчество \n 4 - Изменить номер ')           
#     menu_change_data(n,name)

def choose(choice):
    if choice == '1': return write(input('Введите ваши данные: '))  
    if choice == '2': return read_all() 
    if choice == '3': return get_by_name(input('Введите имя, фамилию или Номер телефона: '))
    if choice == '4': return change(input('Введите имя, которое хотите изменить: '),input (' Выберите действие: \n 1 - Изменить Фамилию \n 2 - Изменить Имя \n 3 - Изменить отчество \n 4 - Изменить номер \n '), input('Введите новое имя: '))
    if choice == '5': return delete(input('Введите данные, которые хотите удалить: '))
    if choice == '-1': exit()

# def menu_change_data(num,name):
#     if num == '1': return change(name)
#     # if num == '2': return change(name)
#     # if num == '3': return change(name)
#     # if num == '4': return change(name)
#     if num == '5': return print_instructions()






