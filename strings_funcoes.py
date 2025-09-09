# f-string (informações em texto)
email = "carol_mantovane@hotmail.com"

faturamento = 1000
custo = 700
lucro = faturamento-custo
print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email_cliente = "carol_mantovane@hotmail.com"

# maiúscula
email_cliente = email_cliente.upper () 
#print(email_cliente)
# minúscula
email_cliente = email_cliente.lower ()
print(email_cliente)

# @
print(email_cliente.find("@"))

# tamanho do texto
nome_cliente = "Carolina"
print(len(email_cliente)) # len é contagem de caracteres
print(len(nome_cliente))

#pegar um caracter - solicitar entre colchetes []
print(email_cliente [26])
print(nome_cliente [3])
print(nome_cliente[-3]) # solicitar caracter de trás para frente (final para o início
print(nome_cliente[:5]) # solicitar informações a partir de um ponto
print(nome_cliente[0:7]) # solicitar informações a partir de um ponto até um outro ponto


# replace = substitui uma informação dentro da string
novo_email = email_cliente.replace("hotmail.com", "gmail.com",) 
print(novo_email)


novo_nome = nome_cliente.replace("Carolina", "Carol")
print(novo_nome)

#Maiusculo e minusculo
nome = "carolina mantovane"
print(nome.capitalize())
print(nome.title())

                                 
#Extrair informações de variáveis diferentes
#Pegar servidor de email
posicao_arroba = email_cliente.find("@") 
servidor = email_cliente[posicao_arroba:]
print(servidor)

#Pegar primeiro nome e sobrenome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco:]
sobrenome = nome[posicao_espaco + 1 :]
print(primeiro_nome)
print(sobrenome)
                

