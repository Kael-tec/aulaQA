# Definindo a tupla
minha_tupla = (10, 20, 30, 40, 50)

# Convertendo a tupla para uma lista
minha_lista = list(minha_tupla)

# Exibindo a lista
print(minha_lista)
print("-"*30)
print(type(minha_tupla))
print("-"*30)
print(type(minha_lista))
print("-"*30)

# Adicionando dois novos elementos à lista
minha_lista.append(60)
minha_lista.append(70)

# Exibindo a lista
print(minha_lista)

# Removendo o primeiro elemento usando pop
minha_lista.pop(0)

# Exibindo a lista após a remoção
print(minha_lista)

# Removendo o último elemento usando pop
minha_lista.pop()

# Exibindo a lista após a remoção
print(minha_lista) 
print("-"*30)

# Imprimindo o primeiro elemento da lista
print("Primeiro elemento da lista:", minha_lista[0])
print("-"*30)

# Imprimindo a quantidade de elementos na lista\len() é usada para retornar o número de itens (ou o comprimento)
print("Quantidade de elementos na lista:", len(minha_lista))
print("-"*30)

# Criando o dicionário
pessoa = {
    "Nome": "Kael",
    "Idade": 22,
    "Profissão": "Limpador de vidro"
}

# Imprimindo o valor da chave "Nome"
print(pessoa["Nome"])
