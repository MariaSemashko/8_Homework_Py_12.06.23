from logger import input_data, print_data, change_data, delete_data, search_data


def interface():
    command = -1
    while command != 6:
        print('Здравствуйте! Для выбора действия надо ввести номер операции\n'
              '1. Записать данные\n'
              '2. Удалить данные\n'
              '3. Изменить данные\n'
              '4. Вывести данные\n'
              '5. Найти данные\n'
              '6. Выход')
        command = int(input('Введите номер операции: \n'))

        while command < 1 or command > 6:
            print('Некорректный номер операции')
            command = int(input('Введите номер операции: \n'))

        if command == 1:
            input_data()
        elif command == 2:
            delete_data()
        elif command == 3:
            change_data()
        elif command == 4:
            print_data()
        elif command == 5:
            search_data()
        elif command == 6:
            print('Спасибо, что воспользовались нашими услугами. Всего доброго!')

