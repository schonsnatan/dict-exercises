'''

https://wiki.python.org.br/EstruturaDeRepeticao

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

        

print("\nEx 1:\n")
print("\nEx 1:\n")
print("\nEx 1:\n")
print("\nEx 1:\n")
print("\nEx 1:\n")
print("\nEx 1:\n")
