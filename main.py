import sys
import json
import datetime


# Текущее време без миллисекунд
def getTime():
    return str(datetime.datetime.now()).split(".")[0]


# Класс элемента строки
class Entry:
    def __init__(self, title, body):
        self.id = 0
        self.title = title
        self.body = body
        self.changes = getTime()
        self.creation = getTime()


# Запись данных из файла в переменную
def openFile():
    with open("list.json", "r", encoding="utf-8") as file:
        return json.load(file)


data = openFile()


# Перезапись данных в файл
def rewrite(data):
    with open("list.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# Определение id последнего добавленного элемента
try:
    lastId = data["objects"][-1]["id"]
except IndexError:
    lastId = -1


# Вывод содержимого файла в консоль
def read():
    for item in data["objects"]:
        print(item)


# Вывод заданной записи в консоль
def find(obj):
    try:
        id = int(obj)
    except ValueError:
        id = str(obj)
    for i, item in enumerate(data["objects"]):
        if item["id"] == id or item["title"] == id:
            print(item)


# Добавление строки в файл
def add(title, body):
    obj = Entry(title, body)
    obj.id = lastId + 1
    data["objects"].append(obj.__dict__)
    rewrite(data)


# Перезапись объекта
def edit(obj, newBody):
    try:
        id = int(obj)
    except ValueError:
        id = str(obj)
    for i, item in enumerate(data["objects"]):
        if item["id"] == id or item["title"] == id:
            data["objects"][i]["body"] = newBody
            data["objects"][i]["changes"] = getTime()
    rewrite(data)


# Удаление объекта
def delete(obj):
    try:
        id = int(obj)
    except ValueError:
        id = str(obj)
    for i, item in enumerate(data["objects"]):
        if item["id"] == id or item["title"] == id:
            data["objects"].pop(i)
            break
    rewrite(data)


args = sys.argv

if len(args) == 1:
    read()
if "-find" in args:
    try:
        find(args[args.index("-find") + 1])
    except IndexError:
        pass
if "-add" in args:
    try:
        add(args[args.index("-add") + 1], args[args.index("-add") + 2])
    except IndexError:
        pass
if "-edit" in args:
    try:
        edit(args[args.index("-edit") + 1], args[args.index("-edit") + 2])
    except IndexError:
        pass
if "-d" in args:
    try:
        delete(args[args.index("-d") + 1])
    except IndexError:
        pass




