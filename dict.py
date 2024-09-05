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

#5. Remova um item do dicionário, como o número de telefone, e imprima o dicionário atualizado.
print("\nEx: 5\n")
dicionario.pop('numero')
print(dicionario)

#6. Use um loop para iterar pelos itens do dicionário e imprimir os nomes e idades dos amigos.
print("\nEx: 6\n")
amigos = {
    "João": 25,
    "Ana": 30,
    "Carlos": 28
}

for i in amigos:
    print(f'{i}: {amigos[i]}')
    
'''
for nome, idade in amigos.items():
    print(f"{nome}: {idade}")
'''

#7. Peça ao usuário para inserir o nome de um amigo e verifique se esse nome existe no dicionário de amigos. Imprima uma mensagem informando se o amigo está ou não na lista.
print("\nEx: 7\n")

amigo = input("Digite o nome de um amigo: ")
if amigo in amigos:
    print("esta no dict")
else:
    print("nao esta no dict")
    
#8.  Conte quantos amigos existem no dicionário e imprima o resultado.
print("\nEx: 8\n")

count = 0
for i in amigos:
   count+=1
print(f'há {count} amigos')

#9. Crie um dicionário de tradução que mapeie palavras de um idioma para outro (por exemplo, inglês para espanhol).
print("\nEx: 9\n")
traducao = {
    "hello": "hola",
    "goodbye": "adiós",
    "thank you": "gracias"
}
word = input("what do you want do translate: ")

if word in traducao:
    print(traducao[word])
else:
    print('this word is not in the dict')

#10. Crie um dicionário que represente o estoque de uma loja, com produtos como chaves e quantidades em estoque como valores.
print("\nEx: 10\n")

estoque = {
    "calca":20,
    "camiseta":15,
    "casaco":12
}

new_product = input("Verifique um produto: ")

if new_product in estoque:
    print(f'O produto {new_product} tem {estoque[new_product]} unidades disponíveis.')
else:
    print("Produto não disponível")

#11. Mesclar Dicionários
print("\nEx: 11\n")

new_dict = dicionario.copy()
new_dict.update(amigos)
print(f'{new_dict}\n')

dicionario1 = {"d": 1, "a": 2}
dicionario2 = {"b": 3, "c": 4}
dicionario_mesclado = {**dicionario1, **dicionario2}
print("Dicionário mesclado:", dicionario_mesclado)

#12.  Crie um dicionário não ordenado e ordene-o por chave ou valor. Imprima o dicionário ordenado.
print("\nEx: 12\n")

ordered_dict = dict(sorted(dicionario_mesclado.items()))
print(ordered_dict)

#13. Seja um contador de palavras.
print("\nEx: 13\n")

texto = input("Digite um texto: ")
palavras = texto.split()
contagem_palavras = {}

for i in palavras:
    if i in contagem_palavras:
        contagem_palavras[i] +=1
    else:
        contagem_palavras[i]=1
        
print(contagem_palavras)

#14. Converta o dicionário de amigos (exercício 6) em uma lista de tuplas, onde cada tupla contém o nome e a idade de um amigo.
print("\nEx: 14\n")

list_new = [(k,v) for k,v in amigos.items()]
print(list_new)

#15. Crie um dicionário com pares chave-valor duplicados e remova todas as duplicatas, deixando apenas uma ocorrência de cada chave no dicionário. Imprima o dicionário resultante. 
print("\nEx: 15\n")

dicionario_duplicado = {"a": 1, "b": 2, "a": 3, "c": 4}
result = {}
for key,value in dicionario_duplicado.items():
    if key not in result.keys():
        result[key] = value
        
print(result)


