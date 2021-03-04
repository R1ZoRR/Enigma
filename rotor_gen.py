import random


random.random()
switches = {}
print('Введите назнание и количество символов для ротора')
rotor_name = input()
charaters = int(input())
file = open(rotor_name+'.txt', 'w')
mas1 = range(1, charaters + 1)
mas2 = random.sample(range(1, charaters + 1), charaters)
for i in range(charaters):
    switches[mas1[i]] = mas2[i]
print(mas1, mas2, switches)
for i in switches:
    file.write(str(i)+' '+str(switches[i])+'\n')
file.close()