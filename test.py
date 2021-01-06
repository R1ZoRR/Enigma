def summon_enigma_machine():
    """
    Эта функция должна спрашивать параметры, для запуска "машины".
    В свою очередь машина состоит из нескольких функций.
    """
    print('Введите текст для машины:')
    x = input()
    return text_ripper(x)


def text_ripper(x):
    """
    Эта функция будет "свежевать" заданый текст, превращать его в цифры и выбрасывать лишнее (чего не будет с словаре
    :param x: исходный текст
    :return:
    """
    default_set_of_keys = {'a': '001', 'b': '002', 'c': '003', 'd': '004', 'e': '005', 'f': '006', 'j': '007',
                           'h': '008', 'i': '009', 'k': '011', 'l': '012', 'm': '013', 'n': '014',
                           'o': '015', 'p': '016', 'r': '018', 's': '019', 't': '020', 'u': '021',
                           'v': '022', 'q': '023', 'x': '024', 'y': '025', 'z': '026', ' ': '   '}
    miss_counter, y = 0, ''
    for i in x:
        if i in default_set_of_keys:
            y += default_set_of_keys[i]
        else:
            miss_counter += 1
    print(y, ' ,Miss counter = ', miss_counter)
    return rotor_stage(y)


def rotor_stage(y):
    """
    здесь я разбиваю строку с цифрами на числа, чтобы по очереди скормить их роторам
    :param y: текст, преобразованный в набор цифор
    :return:
    """
    z = ''
    for i in range(0, int(len(y) / 3)):
        if y[i * 3: i * 3 + 3] == '   ':
            z += ' '
        else:
            z += str(int(y[i * 3: i * 3 + 3]))
    print(z)


summon_enigma_machine()
