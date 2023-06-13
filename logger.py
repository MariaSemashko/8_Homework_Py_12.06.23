from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    print(f"Записываю данные: \n"
            f"{name} {surname} {phone} {address}\n")
            
        
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {phone} {address}\n')


def print_data():
    print('Вывожу данные: \n')
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        data_first = list(file.readlines())
        for i in range(len(data_first)):
            print(f'{i + 1}: {data_first[i]}')
    
    return data_first


def change_data():
    data_first = print_data()
    print("Какую именно запись по счету Вы хотите изменить?")
    number_journal = int(input('Введите номер записи: \n'))
    while number_journal < 1 or number_journal > len(data_first):
        print('Некорректный ввод')
        number_journal = int(input('Введите номер записи: \n'))
    new_data = data_first[number_journal - 1]
    new_data = new_data.split(' ')
    
    print(f'Изменить данную запись\n{data_first[number_journal -1]}')
    print('Изменить имя?')
    if input("Да/Нет\n").lower() == "да":
        name = name_data()
        new_data[0] = name
    print('Изменить фамилию?')
    if input("Да/Нет\n").lower() == "да":
        surname = surname_data()
        new_data[1] = surname
    print('Изменить телефон??')
    if input("Да/Нет\n").lower() == "да":
        phone = phone_data()
        new_data[2] = phone
    print('Изменить адрес?')
    if input("Да/Нет\n").lower() == "да":
        address = address_data()
        new_data[3] = f'{address}\n'
    else:
        print("Вы не выбрали данные, которые надо изменить")

    new_data = ' '.join(new_data)           
    data_first[number_journal - 1] = new_data
    
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(data_first))
    print("Изменения успешно сохранены: \n"
        f"{data_first[number_journal-1]}")
    


def delete_data():
    data_first = print_data()
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: \n'))
    while number_journal < 1 or number_journal > len(data_first):
        print('Некорректный ввод')
        number_journal = int(input('Введите номер записи: \n'))
        
    print(f'Удалить данную запись полностью?\n{data_first[number_journal - 1]}')
    if input("Да/Нет\n").lower() == "да":
        data_first = data_first[:number_journal-1] + data_first[number_journal:]
    else:
        print(f'Удалить отдельные элементы записи?\n{data_first[number_journal -1]}')
        if input("Да/Нет\n").lower() == "да":
            new_data = data_first[number_journal - 1]
            new_data = new_data.split(' ')
    
            print('Удалить имя?')
        if input("Да/Нет\n").lower() == "да":
            name = "Неизвестно"
            new_data[0] = name
        print('Удалить фамилию?')
        if input("Да/Нет\n").lower() == "да":
            surname =  "Неизвестно"
            new_data[1] = surname
        print('Удалить телефон??')
        if input("Да/Нет\n").lower() == "да":
            phone = "Неизвестно"
            new_data[2] = phone
        print('Удалить адрес?')
        if input("Да/Нет\n").lower() == "да":
            address = "Неизвестно"
            new_data[3] = f'{address}\n'
        else:
            print("Вы не выбрали данные, которые надо удалить")

        new_data = ' '.join(new_data)           
        data_first[number_journal - 1] = new_data
    

    with open('phonebook.txt', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
    print('Изменения успешно сохранены!')

def search_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        word = input('Введите ключевое слово для поиска: ')
        data_first = list(file.readlines())
        
        
        for i in data_first:
            separate_data = i.split(' ')
            for j in separate_data:
                if word.lower() in j.lower():
                    print(i)



   