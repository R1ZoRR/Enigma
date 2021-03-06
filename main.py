import os


def summon_enigma_machine(initial_text=''):
    """
    Эта функция должна спрашивать параметры, для запуска "машины".
    В свою очередь машина состоит из нескольких функций.
    """
    # Тут я присвоил нужные типы обьектам
    rewritten_text, output_text, set_of_keys = '', '', ''
    # Тут скормил полученный текст потрошителю и получил от него очищеный текст и набор ключей (букв)
    rewritten_text, set_of_keys = text_ripper(initial_text)
    # Тут я создаю "обратный" словарь. ВНИМАНИЕ!, если ключ в оригинальном словаре не интуется - программа остановится.
    backward_set_of_keys, rotor_pos = {}, {}
    # Название говорит само за себя. Добавлен, для легкого исключение знаков препинания из словоря.
    cursed_words = [" ", ",", "."]
    for i in set_of_keys:
        if i not in cursed_words:
            backward_set_of_keys[int(set_of_keys[i])] = i
    rotor = ''
    while rotor != 0:  # всегда не =
        print('Укажите параметры для роторов следующим образом:\nВведите назнание ротора (без расширения .txt). '
              'Для остановки введите пробел.')
        rotor = str(input())
        if rotor != ' ':
            print('Введите позицию для ротора:')
            pos = int(input())
            if rotor + '_0' in rotor_pos:
                i = 0
                while rotor + '_' + str(i) in rotor_pos:
                    i += 1
                rotor_pos[rotor + '_' + str(i)] = pos
            else:
                if os.path.exists(rotor + '.txt'):
                    rotor_pos[rotor + '_0'] = pos
                else:
                    print('Такого ротора - нет!')
        else:
            if rotor_pos != {}:
                break
            else:
                print('Должен быть хотя бы 1 ротор!')
    for i in range(0, int(len(rewritten_text) / 3)):
        if rewritten_text[i * 3: i * 3 + 3] != '   ':  # Тут я гарантирую себе, что скормлю роторам цифры, а не пробелы
            # на этом моменте мы получили заветное число, и готовы скормить его роторам
            key_id = int(rewritten_text[i * 3: i * 3 + 3])
            # Тут я вызываю роторы, запихиваю в них кусок текста, возвращаю результат и превращаю его из чисел в буквы
            rotor_stage(key_id, rotor_pos, len(backward_set_of_keys))
            output_text += str(key_id) + ' '
        else:
            output_text += ' '  # Три пробела были нужны для кратности
    print('Результат шифрования:')
    print(output_text)


def rotor_stage(id, rotor_pos, len):
    for i in rotor_pos:
        shift = int(rotor_pos[i])
        while shift > len:
            shift -= len
        id += shift
        while id > len:
            id -= len
        i = i.split('_')
        with open(i[0] + '.txt') as file:
            lines = file.readlines()
        lines = (''.join(lines[id - 1: id])).split()
        id = int(lines[1])
    return id


def text_ripper(text_sample, set_of_keys=''):
    """
    Эта функция будет "свежевать" заданый текст, превращать его в цифры и выбрасывать лишнее (чего не будет с словаре
    :param text_sample: исходный текст
    :param set_of_keys: Словарь. Нужен для импорта словаря в функцию. Если импорта не происходит берется деф. словарь.
    Словарь всегда можно заменить, вызвав нужный словарь в качестве второго аргумента
    :return:
    """
    default_set_of_keys = {'a': '001', 'b': '002', 'c': '003', 'd': '004', 'e': '005', 'f': '006', 'g': '007',
                           'h': '008', 'i': '009', 'j': '010', 'k': '011', 'l': '012', 'm': '013', 'n': '014',
                           'o': '015', 'p': '016', 'q': '017', 'r': '018', 's': '019', 't': '020', 'u': '021',
                           'v': '022', 'w': '023', 'x': '024', 'y': '025', 'z': '026', ' ': '   '}
    if set_of_keys == '':
        set_of_keys = default_set_of_keys
    miss_counter, return_text = 0, ''  # Тут я присвоил нужные типы обьектам
    for i in text_sample:
        if i in set_of_keys:  # Тут я проверяю каждый символ в исходной строке, на наличие в списке
            return_text += set_of_keys[i]  # Если такой найдется, то он добавляется в "очередь" на обработку
        else:
            miss_counter += 1
    print(return_text, ' ,Miss counter = ', miss_counter)
    return return_text, set_of_keys


print('Введите текст для машины:')
text = str(input())
summon_enigma_machine(text)
