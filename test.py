
def summon_enigma_machine():
    """
    Эта функция должна спрашивать параметры, для запуска "машины".
    В свою очередь машина состоит из нескольких функций.
    """
    print('Введите текст для машины:')
    initial_text, y, output_text, set_of_keys, i = input(), '', '', '', 1  # тут я присвоил нужные типы обьектам
    y, set_of_keys = text_ripper(initial_text) # тут я бызвал потрошителя и получил от него "потроха" с набором символов
    backward_set_of_keys = {} # название говорит само за себя
    for i in set_of_keys:
        backward_set_of_keys[set_of_keys[i]] = i
    print(backward_set_of_keys)
    for i in range(0, int(len(y) / 3)):
        if y[i * 3: i * 3 + 3] != '   ':  # тут я гарантирую себе, что скормлю роторам цифры, а не пробелы
            # тут я вызываю роторы, запихиваю в них кусок текста, возвращаю результат и превращаю его из чисел в буквы
            output_text += str(rotor_a(int(y[i * 3: i * 3 + 3]), len(set_of_keys) - 1))
        else:
            output_text += ' '  # три пробела были нужны для кратности
    print(output_text)


def text_ripper(text, set_of_keys = ''):
    """
    Эта функция будет "свежевать" заданый текст, превращать его в цифры и выбрасывать лишнее (чего не будет с словаре
    :param text: исходный текст
    :return:
    """
    default_set_of_keys = {'a': '001', 'b': '002', 'c': '003', 'd': '004', 'e': '005', 'f': '006', 'j': '007',
                           'h': '008', 'i': '009', 'k': '011', 'l': '012', 'm': '013', 'n': '014',
                           'o': '015', 'p': '016', 'r': '018', 's': '019', 't': '020', 'u': '021',
                           'v': '022', 'q': '023', 'x': '024', 'y': '025', 'z': '026', ' ': '   '}
    if set_of_keys == '':
        set_of_keys = default_set_of_keys
    miss_counter, return_text = 0, ''  # тут я присвоил нужные типы обьектам
    for i in text:
        if i in set_of_keys:  # тут я проверяю каждый символ в исходной строке, на наличие в списке
            return_text += set_of_keys[i]  # если такой найдется, то он добавляется в "очередь" на обработку
        else:
            miss_counter += 1
    print(return_text, ' ,Miss counter = ', miss_counter)
    return return_text, set_of_keys


def rotor_stage(y, set_of_keys):
    print('Задайте параметры для ротора: ')

# Здесь находятся сами роторы
def rotor_a(key_id, len_of_keys):
    if 1 == (key_id % 4):
        key_id = key_id + 2
    elif 2 == (key_id % 4):
        key_id = key_id - 1
    elif 3 == (key_id % 4):
        key_id = key_id + 1
    elif 0 == (key_id % 4):
        key_id = key_id - 2
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


summon_enigma_machine()
