#Inputs
email = input("Escreva seu e-mail:")
nome = input("Escvreva seu nome")
print(nome, email)
print(f"{nome} verifique se este email está correto {email} para confirmação da conta")

faturamento = float(input("Escreva o faturamento da empresa:"))

print(faturamento)
imposto = faturamento * 0.1
print("O imposto é de R$", imposto)

#Listas
vendas = [10, 50, 15, 20, 30, 500]
print(vendas)

total_vendas = sum(vendas)
print(total_vendas)

#Tamanho da lista
quantiddade_vendas = len(vendas) # len define quantos itens tem na lista
print(quantiddade_vendas)

# # Máximo e mínimo
print(max(vendas))
print(min(vendas))

# #Pegar uma posição da lista
print(vendas[-1])

# #Verificar um elemento da lista
lista_produtos = ["iphone", "airpods", "ipad", "macbook"]
print(lista_produtos)
print("aplle watch" in lista_produtos) # resultado boleano

produto_procurado = input("Psquise o nome do produto:")
print(produto_procurado in lista_produtos)

#Adicionar um produto na lista
lista_produtos.append("apple watch")
print(lista_produtos)

# #Remover um produto na lista
lista_produtos.remove("apple watch")
print(lista_produtos)

#Editar um item  da lista
precos_produtos = [100, 500, 2500, 1500]
precos_produtos [0] = precos_produtos [0] * 1.5
print(precos_produtos)

# Contar quantas vezes um item aparece na lista
lista_produtos = ["iphone", "airpoods", "ipaad", "macbook", "iphone", "iphone"]
print(lista_produtos.count("iphone"))

# Ordenar uma lista
lista_produtos.sort() # ordem alfabética
lista_produtos.sort(reverse=True) # ordem alfabética invertida
print(lista_produtos)


