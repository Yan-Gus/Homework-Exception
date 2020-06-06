# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "prava", "number": "1333"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people(document):
    doc_number = input("Введите номер документа: ")
    user_name = ""

    for code_of_doc in document:
        if code_of_doc["number"] == doc_number:
            user_name = code_of_doc["name"]
            break

    if user_name != "":
        print(f"Этот код принадлежит: {user_name}")
    else:
        print("Документ не найден")


def shelfsearch(directory):
    number_of_doc = input("Введите номер документа: ")
    number_of_shelf = ""
    for num_of_shelf, code_of_doc in directory.items():
        if number_of_doc in code_of_doc:
            number_of_shelf = num_of_shelf
            break
    if number_of_shelf != "":
        print(f"Полка №{number_of_shelf}")
    else:
        print("Документ не найден")


def docs_list(documents_list):
    for doc in documents_list:
        print(f"{doc['type']} \"{doc['number']}\" \"{doc['name']}\"")


def doc_add():
    global documents
    global directories
    doc_type = input("Введите тип документа: ")
    doc_number = input("Введите номер документа: ")
    doc_name = input("Введите имя и фамилию: ")

    while 1:
        doc_shelf = input("Введите номер полки: ")
        if doc_shelf in directories.keys():
            break
        else:
            print("Такой полки не существует")

    documents.append({"type": doc_type, "number": doc_number, "name": doc_name})
    directories[doc_shelf].append(doc_number)
    print("Документ добавлен")


def main():
    while 1:
        command = input("Введите команду: ")

        if command == "p":
            print("Поиск имени по номеру документа")
            people(documents)

        elif command == "s":
            print("Поиск номера полки по номеру документа")
            shelfsearch(directories)

        elif command == "l":
            print("Вывод всех документов")
            docs_list(documents)

        elif command == "a":
            print("Добавление нового документа")
            doc_add()

        elif command == "d":
            print("Удаление документа")
            delete_doc()

        elif command == "m":
            print("Перемещение документа на другую полку")
            move_doc(directories)

        elif command == "as":
            print("Создание новой полки")
            add_shelf(directories)

        elif command == "on":
            print("Вывод всех имен владельцев документов:")
            output_name(documents)

        elif command == "q":
            print("До свидания!")
            break

        else:
            print("Несуществующая команда")


def delete_doc():
    global documents
    global directories
    doc_found = False
    doc_num = input("Введите номер документа: ")
    for doc_code in documents:
        if doc_code["number"] == doc_num:
            documents.remove(doc_code)
            doc_found = True
            break

    if doc_found == True:
        for num_shelf, shelf_contents in directories.items():
            if doc_num in shelf_contents:
                shelf_contents.remove(doc_num)
        print("Документ удален")
    else:
        print("Документ не найден")


def move_doc(directory):
    doc_num = input(" Введите номер документа: ")
    current_shelf = 0
    for shelf_num, code_doc in directory.items():
        if doc_num in code_doc:
            current_shelf = shelf_num
            print(f"Документ №{doc_num} расположен на полке №{current_shelf}")
            break
    if current_shelf:
        target_shelf = input("Введите целевую полку: ")
    else:
        print("Документ не найден")
        return

    if target_shelf in directory.keys():
        directory[current_shelf].remove(doc_num)
        directory[target_shelf].append(doc_num)
        print(f"Документ №{doc_num} перемещен на {target_shelf} полку")
    else:
        print("Такой полки не существует")


def add_shelf(directory):
    new_shelf = input("Введите номер новой полки: ")
    if new_shelf in directory.keys():
        print("Такая полка существует")
        return
    else:
        directory[new_shelf] = list()
        print(f"Полка {new_shelf} добавлена")


def output_name(documents):
    for document in documents:
        try:
            assert document['name'] != '', "Не заполнено поле \"Имя\" документа"
            print(f"Имя: \"{document['name']}\"")
        except KeyError:
            print(f"Отсутствует поле \"Имя\" у документа {document['number']}.")
        except AssertionError as ex:
            print(f"Документ {document['number']}: {ex}.")


main()
