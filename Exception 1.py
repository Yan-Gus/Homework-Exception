def polish_notation():
    input_data = input("Введите через пробел: знак оператора, число №1, число №2: ")
    symbols = input_data.split()

    try:
        assert len(symbols) == 3, "Введено неверное количество аргументов"
        operator = str(symbols[0])
        number_1 = int(symbols[1])
        number_2 = int(symbols[2])
        assert operator in ("+", "-", "*", "/"), "Некорректный оператор (+, -, *, /)."

        print(
            f"Результат вычисления {number_1} {operator} {number_2} = {eval(str(number_1) + operator + str(number_2))}")

    except ValueError as ex:
        print(f"Введена строка вместо числа. Ошибка: {ex}")
        return

    except ZeroDivisionError as ex:
        print(f"Деление на ноль запрещено. Ошибка: {ex}")
        return

    except Exception as ex:
        print(f"Ошибка: {ex}")
        return


polish_notation()
