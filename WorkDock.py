from Algoritm import *
import re

def write(text):
    with open("data.txt","a", encoding ="utf-8") as f:
        f.writelines(text)
        f.writelines('\n')
        print('Успешно')

def read_all():
    with open("data.txt","r", encoding ="utf-8") as f:
        for line in f:
            print(line[:-1])

def get_by_name(name):
    with open("data.txt","r", encoding ="utf-8") as f:
        for line in f:
            if name in line:
                print(line)

def delete(name):
    #Подключил функцию 're', которую мы не изучали, 
    #по другому не догадался как 
    with open("data.txt","r", encoding ="utf-8") as f:
        data = f.readlines()
    pat = re.compile(re.escape(name))
    with open('data.txt','w',encoding = 'utf-8') as f:
        for line in data:
            result = pat.search(line)
            if result is None:
                f.write(line)
    return print('Данные удалены!')                           

def change(name):
    name = str(name)
    new_name = str(input('Введите новое имя: '))
    with open('data.txt','r',encoding = 'utf-8') as f:
        for line in f:
            if name in line:
                old_data =str(line)
                next_data = old_data.replace('\\n','').split()
                
                for i in range(len(next_data)):
                    if next_data[i] == name:
                        next_data[i] = new_name
                        # print(next_data)
    data_string =''
    for el in next_data:
        data_string +=el 
        data_string += ' '
    # print(data_string)                         
    delete(name)  
    write(data_string)            





