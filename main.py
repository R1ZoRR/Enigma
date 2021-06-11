import os


def summon_enigma_machine(mode=1, initial_text='', initial_rotor=''):
    """
    Эта функция должна спрашивать параметры, для запуска "машины". В свою очередь машина состоит из нескольких
    функций. param :mode: определяет режим работы вывода текста. 0 - неизместные символы остаются на месте. 1 -
    пропуск неизвестных символов (в том числе знаков препинания). param :initial_text: текст на вход. Если текст не
    был передан функции, то она спросит его сама. param :initial_rotor: роторы на вход. Тут я даю возможность
    определить положение роторов заранее (пока не реализовано)
    """
    # Тут я присвоил нужные типы обьектам
    rewritten_text, output_text, set_of_keys = '', '', ''
    backward_set_of_keys, temp_rotor_pos, rotor_pos = {}, [], []

    if initial_text == '':
        print('Введите текст для ротора:')
        initial_text = str(input())

    # Тут скормил полученный текст потрошителю и получил от него очищенный текст и набор ключей (букв)
    rewritten_text, set_of_keys, other_symbols = text_ripper(initial_text)

    # Тут я создаю "обратный" словарь. ВНИМАНИЕ! Если ключ в оригинальном словаре нельзя => int - программа остановится
    for i in set_of_keys:
        backward_set_of_keys[int(set_of_keys[i])] = i

    # Название говорит само за себя. Добавлен, для легкого исключение знаков препинания из словаря.
    rotor = ''
    i = 0
    while rotor != 0:  # всегда не =
        print('Введите название ротора (без расширения .txt, для остановки отправьте пробел):')
        rotor = str(input())
        if rotor != ' ':
            print('Введите позицию для ротора (позиция это число):')
            pos = 'n'
            while not pos.isdigit():
                pos = input()
                if pos.isdigit() == 0:
                    print('Плохие данные для положения. Позиция - это целое, неотрицательное число.')
            if os.path.exists(os.getcwd() + '/rotors/' + rotor + '.txt'):
                temp_rotor_pos.append([])
                temp_rotor_pos[i] = [rotor, int(pos)]
                i += 1
            else:
                print('Такого ротора - нет!')
        else:
            if temp_rotor_pos != {}:
                break
            else:
                print('Должен быть хотя бы 1 ротор!')

    # размечаем место для массива
    for rotor in range(len(temp_rotor_pos)):  # кол-во роторов
        a1 = []
        for k in range(2):  # кол-во элементов для хранения роторов и их положения
            a2 = []
            for j in range(26):  # кол-во строк в роторе
                a2.append(0)
            a1.append(a2)
        rotor_pos.append(a1)

    # заполняем массив с роторами
    for i in range(len(temp_rotor_pos)):
        # открываем ротор
        with open(os.getcwd() + '/rotors/' + str(temp_rotor_pos[i][0]) + '.txt') as file:
            lines = file.readlines()

        # заносим ротор из файла в псевдо-массив
        line_count = 0
        for line in lines:
            rotor_pos[i][0][line_count] = ([int(x) for x in line.split()])
            line_count += 1

        # заносим сдвиг из старого массива
        rotor_pos[i][1] = temp_rotor_pos[i][1]

        file.close()

    # Запуск основной части
    j = 0
    for i in range(0, int(len(rewritten_text) / 3)):
        if rewritten_text[i * 3: i * 3 + 3] != '   ':  # Тут я гарантирую себе, что скормлю роторам цифры, а не пробелы
            # на этом моменте мы получили заветное число, и готовы скормить его роторам
            key_id = int(rewritten_text[i * 3: i * 3 + 3])

            # Тут я вызываю роторы, запихиваю в них кусок текста, возвращаю результат и превращаю его из чисел в буквы
            output_text += backward_set_of_keys[rotor_stage(key_id, rotor_pos, len(backward_set_of_keys))]
        else:
            if mode == 0:
                output_text += other_symbols[j]  # Три пробела были нужны для кратности
                j += 1
    print('Результат шифрования:')
    print(output_text)

    print('Использованные роторы и их положение:')
    for i in range(len(temp_rotor_pos)):
        print(temp_rotor_pos[i][0], ':', temp_rotor_pos[i][1], '(', backward_set_of_keys[temp_rotor_pos[i][1]], ')')


def rotor_stage(key_id, rotor_pos, leng=26):
    """
    Эта функция вызывает роторы.
    param :key_id: номер буквы на вход
    param :rotor_pos: rotor_pos[номер ротора][0 - кортеж со всеми коммутаторами, 1 - кортеж с обратными коммутаторами,
    2 - поворот ротора][кортеж с входом и выходом коммутатора][0 - вход коммутатора, 1 - выход коммутатора]
    param :leng: длинна словаря (по умолчанию 26)
    """

    #  сдвиг и проверка положения ротора
    rotor_pos[0][1] += 1
    for i in range(len(rotor_pos)):
        while rotor_pos[i][1] > leng:
            rotor_pos[i][1] -= leng
            if i < (len(rotor_pos) - 1):
                rotor_pos[i + 1][1] += 1

    #  через роторы, до рефлектора
    for i in range(len(rotor_pos)):
        j = 0
        key_id += rotor_pos[i][1]
        while key_id > leng:
            key_id -= leng
        while rotor_pos[i][0][j][0] != key_id:
            j += 1
        key_id = rotor_pos[i][0][j][1]

    # Рефлектор
    key_id = leng - key_id + 1

    # от рефлектора, через роторы
    for i in range(len(rotor_pos)):
        # отражаем i т. к. мы идем в обратную сторону
        i = len(rotor_pos) - 1 - i
        j = 0
        while rotor_pos[i][0][j][1] != key_id:
            j += 1
        key_id = rotor_pos[i][0][j][0]
        key_id -= rotor_pos[i][1]
        while key_id <= 0:
            key_id += leng
    return key_id


def text_ripper(text_sample, set_of_keys=''):
    """
    Эта функция будет "свежевать" заданный текст, превращать его в цифры и выбрасывать лишнее (чего не будет с словаре
    param :text_sample: исходный текст
    param :set_of_keys: Словарь. Нужен для импорта словаря в функцию. Если импорта не происходит берется деф. словарь.
    Словарь всегда можно заменить, вызвав нужный словарь в качестве второго аргумента
    param :return_text: текст готовый для обработки роторами
    param :return_symbols: символы, не подходящие для обработки
    """
    default_set_of_keys = {'A': '001', 'B': '002', 'C': '003', 'D': '004', 'E': '005', 'F': '006', 'G': '007',
                           'H': '008', 'I': '009', 'J': '010', 'K': '011', 'L': '012', 'M': '013', 'N': '014',
                           'O': '015', 'P': '016', 'Q': '017', 'R': '018', 'S': '019', 'T': '020', 'U': '021',
                           'V': '022', 'W': '023', 'X': '024', 'Y': '025', 'Z': '026'}
    if set_of_keys == '':
        set_of_keys = default_set_of_keys

    miss_counter, return_text, return_symbols = 0, '', ''  # Тут я присвоил нужные типы обьектам

    for i in text_sample:
        if i.upper() in set_of_keys:  # Тут я проверяю каждый символ в исходной строке, на наличие в списке
            return_text += set_of_keys[i.upper()]  # Если такой найдется, то он добавляется в "очередь" на обработку
        else:
            return_text += '   '
            return_symbols += i
            miss_counter += 1
    print('Текст на вход:', return_text, ' ,не определены: ', miss_counter, ' символа(ов).')

    return return_text, set_of_keys, return_symbols


summon_enigma_machine(0)
