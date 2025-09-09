#Cenário 1
vendas = 1500
meta = 1300

# == igaul
# != diferente

# para a condição de if e else funcionar, tem que sempre ter o espaço (TAB)

if vendas > meta:
    print("Vendedor ganha bônus")
    print("Bateu a  meta de vendas")
    bônus = 0.1* vendas
    print("Bônus do vendedor", bônus)
else:
    print("Vendedor nao ganha bônus")
    print("Não bateu a meta de vendas")

#Cenário 2
vendas = int (input("Digite o valor das "))
vendas_empresa = 20000
meta_empresa = 18000
meta1 = 1300 # ganhar 10%
meta2 = 1500 # ganhar 13%
meta3 = 2500 # ganhar 15%

if vendas >= 1300:
    bonus = 0.1 * vendas
else:
    if vendas >= 1300:
        bonus = 0.1 * vendas
    else:
        bonus = 0     

        #OU USAR ASSIM (FORMA SIMPLIFICADA):

if vendas >= 2500 and vendas_empresa >= meta_empresa:
    bonus = 0.15 * vendas
elif vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif vendas >= 1300 and vendas_empresa >= meta_empresa:
    bonus = 0.1 * vendas    
else:
    bonus = 0  

print("Bônus:", bonus)      

lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
produto_procurado = input("Procure um produto:")
produto_procurado = produto_procurado.lower ()

if produto_procurado in lista_produtos:
    print("Produto em estoque")
else:
    print("Não temos este produto")    





