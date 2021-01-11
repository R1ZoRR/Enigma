
def summon_enigma_machine():
    """
    Эта функция должна спрашивать параметры, для запуска "машины".
    В свою очередь машина состоит из нескольких функций.
    """
    print('Введите текст для машины:')
    # тут я присвоил нужные типы обьектам
    initial_text, rewritten_text, output_text, set_of_keys, i = input(), '', '', '', 1
    # тут я вызвал потрошителя и получил от него "потроха" с набором символов
    rewritten_text, set_of_keys = text_ripper(initial_text)
    backward_set_of_keys = {}  # название говорит само за себя
    for i in set_of_keys:
        if i != ' ':  # тут пришлось добавить исколючение, т к выполнение останавливалось
            backward_set_of_keys[int(set_of_keys[i])] = i
    print(backward_set_of_keys)
    for i in range(0, int(len(rewritten_text) / 3)):
        if rewritten_text[i * 3: i * 3 + 3] != '   ':  # тут я гарантирую себе, что скормлю роторам цифры, а не пробелы
            # тут я вызываю роторы, запихиваю в них кусок текста, возвращаю результат и превращаю его из чисел в буквы
            s = int(rotor_a(int(rewritten_text[i * 3: i * 3 + 3]), len(set_of_keys) - 1)) # добавил для красоты кода
            if s in backward_set_of_keys:
                output_text += backward_set_of_keys[s]
            else:
                print('error: ',s)
        else:
            output_text += ' '  # три пробела были нужны для кратности
    print(output_text)


def text_ripper(text, set_of_keys = ''):
    """
    Эта функция будет "свежевать" заданый текст, превращать его в цифры и выбрасывать лишнее (чего не будет с словаре
    :param text: исходный текст
    :return:
    """
    default_set_of_keys = {'a': '001', 'b': '002', 'c': '003', 'd': '004', 'e': '005', 'f': '006', 'g': '007', 'h': '008',
                           'i': '009', 'j': '010', 'k': '011', 'l': '012', 'm': '013', 'n': '014',
                           'o': '015', 'p': '016', 'q': '017', 'r': '018', 's': '019', 't': '020', 'u': '021',
                           'v': '022','w': '023', 'x': '024', 'y': '025', 'z': '026', ' ': '   '}
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
