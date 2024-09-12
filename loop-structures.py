'''
https://wiki.python.org.br/EstruturaDeRepeticao
'''
'''
print("\nEx 1:\n")

grade = int(input('grade between 1 and 10: '))

while grade < 1 or grade > 10:
    print('Invalid number!')
    grade = int(input('grade between 1 and 10: '))

print("\nEx 2:\n")

name = input('Type your name: ')
password = input('Provide a password: ')

while password==name:
    print('Your password cannot be equal to your name.')
    password = input('Provide a password: ')

print("\nEx 3:\n")

name = input('Type your name: ')
age = int(input('Type your age: '))
salary = float(input('Your salary: '))
sex = input('f or m: ')
estado_civil = input('s, c, v, d: ')

valid = False

while not valid:
    if len(name) > 3:
        print('Must be max 3 char!')
        name = input('Type your name: ')
    elif age < 0 or age > 150:
        print('Must be between 0 and 150')
        age = int(input('Type your age: '))
    elif salary < 0:
        print('Bigger than 0.')
        salary = float(input('Your salary: '))
    elif sex not in ['f','m']:
        print('please f or m.')
        sex = input('f or m: ')
    elif estado_civil not in ['s','c','v','d']:
        print('please s,c,v or d: ')
        estado_civil = input('s, c, v, d: ')
    else:
        valid = True
        
print(f'Thank you {name} for the information.')

print("\nEx 4:\n")

a = 80000
b = 200000
pc1 = 0.03
pc2 = 0.015
count = 0

while a < b:
    a += a*pc1
    b += b*pc2
    count+=1
    print(f'No ano {count} a: {a:.2f} e b: {b:.2f}')
    
print(f"\nIt took {count} years to a: {a:.2f} pass b: {b:.2f}")

print("\nEx 5:\n")

while True:
    a = int(input('Inform the population of a: '))
    while a <= 0:
        print('Inform a population greater than 0.')
        a = int(input('Inform the population of a: '))
    b = int(input('Inform the population of b: '))
    while b <= 0:
        print('Inform a population greater than 0.')
        b = int(input('Inform the population of a: '))
    pc1 = float(input('Inform the growth rate of a: '))
    while pc1 <= 0:
        print('Inform valid growth rate.')
        pc1 = float(input('Inform the growth rate of a: '))
    pc2 = float(input('Inform the growth rate of b: '))
    while pc2 <= 0:
        print('Inform valid growth rate.')
        pc2 = float(input('Inform the growth rate of b: '))
    count = 0
    
    while a < b:
        a += a*pc1
        b += b*pc2
        count+=1
        print(f'No ano {count} a: {a:.2f} e b: {b:.2f}')
        
    print(f"\nIt took {count} years to a: {a:.2f} pass b: {b:.2f}")
    check = input('Do you want to continue? Y or N: ')
    if check=='Y':
        continue
    elif check=='N':
        break
    else:
        print('Saindo...')

print("\nEx 6:\n")

for i in range(0,21):
    print(i)

for i in range(0,21):
    print(i, end=' ')

print("\nEx 7:\n")

numbers = input('5 numbers separated by comma: ')
list_numbers = numbers.split(',')

res = [eval(i) for i in list_numbers]
print(max(res))

for i in range(0, len(list_numbers)):
    list_numbers[i] = int(list_numbers[i])
print(max(res))
    

print("\nEx 8:\n")

numbers = input('5 numbers separated by comma: ')
list_numbers = numbers.split(',')

res = [eval(i) for i in list_numbers]
total = sum(res)
mean = total/len(res)

print(total)
print(mean)

print("\nEx 9:\n")

for i in range(50):
    if i % 2!=0:
        print(i)

print("\nEx 10 e 11:\n")

count=0
int1 = int(input('num 1: '))
int2 = int(input('num 2: '))
for i in range(int1+1,int2):
    print(i)
    count+=i
print(f'A soma é: {count}')


print("\nEx 12:\n")

tabuada = int(input('Numero tabuada: '))
print(f"Tabuada de {tabuada}")
for i in range(11):
    print(f'{tabuada} X {i} = {tabuada*i}')

print("\nEx 13:\n")
base = int(input('Base: '))
exp = int(input('Expoente: '))

print(f'Resultado: {base**exp}')
'''
print("\nEx 14:\n")

num = input('lista de 10 numeros: ')