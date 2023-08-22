
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