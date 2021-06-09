import os


print('Введите назнание для ротора')
rotor_name = input()
charaters = 26
print('Введите положение коммутароров')
com = str(input())
path = os.getcwd() + '/rotors/' + rotor_name + '.txt'
file = open(path, 'w')
default_set_of_keys = {'A': '001', 'B': '002', 'C': '003', 'D': '004', 'E': '005', 'F': '006', 'G': '007',
                       'H': '008', 'I': '009', 'J': '010', 'K': '011', 'L': '012', 'M': '013', 'N': '014',
                       'O': '015', 'P': '016', 'Q': '017', 'R': '018', 'S': '019', 'T': '020', 'U': '021',
                       'V': '022', 'W': '023', 'X': '024', 'Y': '025', 'Z': '026', ' ': '   '}
for i in range(0, charaters, 1):
    file.write(str(i + 1) + ' ' + str(int(default_set_of_keys[com[i]])) + '\n')
    print(str(i + 1) + ' ' + com[i])
file.close()