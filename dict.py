# https://acadianschool.com.br/dominando-dicionarios-em-python-15-exercicios-para-aperfeicoar-suas-habilidades-de-programacao/

#1. Crie um dicionário que represente informações sobre uma pessoa, como nome, idade, cidade natal e profissão.
print("\nEx: 1\n")
dicionario = {
    "name":"Natan",
    "age":20,
    "job":"IT",
    "city":"Ivoti"
}

#2. Vamos explorar os dados. Acesse e imprima valores específicos do dicionário que você criou no exercício anterior, como o nome e a idade da pessoa.

print("\nEx: 2\n")
print(dicionario.items())

#3. Modifique o valor de um item no dicionário que você criou e, em seguida, imprima o dicionário atualizado.

print("\nEx: 3\n")
dicionario.update(name='Natan Schons')
print(dicionario)

#4. Adicione informações adicionais à pessoa no dicionário, como seu endereço de e-mail e número de telefone.

print("\nEx: 4\n")
dicionario['email'] = 'email@gmail.com'
dicionario['numero'] = '519999999'
print(dicionario)
