def summon_enigma_machine(initial_text=''):
    """
    Эта функция должна спрашивать параметры, для запуска "машины".
    В свою очередь машина состоит из нескольких функций.
    """
    # Тут я присвоил нужные типы обьектам
    rewritten_text, output_text, set_of_keys, reforged_rotor_pos = '', '', '', {}
    # Тут я вызвал потрошителя и получил от него "потроха" с набором символов
    rewritten_text, set_of_keys = text_ripper(initial_text)
    # Тут я создаю "обратный" словарь. Внимание, если ключ в оригинальном словаре не интуется - программа остановится
    backward_set_of_keys = {}
    for i in set_of_keys:
        if i != ' ':  # тут пришлось добавить исколючение, т к выполнение останавливалось
            backward_set_of_keys[int(set_of_keys[i])] = i
    print(backward_set_of_keys)
    print('Укажите параметры для роторов следующим образом: '
          'Название ротора(7 символов. Далее, без разделителей)позиция ротора. Повторить *количество роторов* раз.'
          'На данный момент существует только 1 ротор: rotor_a')
    rotor_pos = input()
    for i in range(0, int(len(rotor_pos) / 10)):
        print(rotor_pos[i * 10: i * 10 + 10])
        reforged_rotor_pos[rotor_pos[i * 10: i * 10 + 7]] = rotor_pos[i * 10 + 7: i * 10 + 10]
        print(reforged_rotor_pos)
    for i in range(0, int(len(rewritten_text) / 3)):
        if rewritten_text[i * 3: i * 3 + 3] != '   ':  # Тут я гарантирую себе, что скормлю роторам цифры, а не пробелы
            key_id = int(rewritten_text[i * 3: i * 3 + 3])
            # Тут я вызываю роторы, запихиваю в них кусок текста, возвращаю результат и превращаю его из чисел в буквы
            if key_id in backward_set_of_keys:
                output_text += backward_set_of_keys[key_id]
            else:
                print('error: ', key_id)
        else:
            output_text += ' '  # Три пробела были нужны для кратности
    print(output_text)


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


def rotor_stage(id, set_of_key, poz):
    len_of_keys = len(set_of_key) - 1
    rotor_list = {'rotor_a': rotor_a(id, poz['rotor_a'], len_of_keys)}
    for rotor in poz:
        if rotor in rotor_list:
            key_id = rotor_list[rotor]
            if int(poz[rotor]) > len_of_keys:
                poz[rotor] > int(poz[rotor]) + 1

    return key_id, poz

# Здесь находятся сами роторы
# При добавлении ротора обязательно нужно добавить его в контейнер роторов
def rotor_a(key_id, shift, len_of_keys, mode='forward'):
    if 1 == (key_id % 4):
        if mode == 'forward':
            key_id = key_id - 1 + shift
        else:
            key_id = key_id + 2 + shift
    elif 2 == (key_id % 4):
        if mode == 'forward':
            key_id = key_id + 1 + shift
        else:
            key_id = key_id - 2 + shift
    elif 3 == (key_id % 4):
        if mode == 'forward':
            key_id = key_id - 2 + shift
        else:
            key_id = key_id - 1 + shift
    elif 0 == (key_id % 4):
        if mode == 'forward':
            key_id = key_id + 2 + shift
        else:
            key_id = key_id + 1 + shift
    if key_id > len_of_keys - 1:
        key_id -= len_of_keys
    elif key_id < 1:
        key_id += len_of_keys
    return key_id


def rotor_caesar(key_id, len_of_keys, shift):
    key_id += shift
    if key_id > len_of_keys - 1:
        key_id -= len_of_keys
    elif key_id < 1:
        key_id += len_of_keys
    return key_id


print('Введите текст для машины:')
text = 'а б В Г'
summon_enigma_machine(text)
