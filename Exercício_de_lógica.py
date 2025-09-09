estoque_loja = {"monitor": 15, "teclado": 25, "mouse": 30}
print(estoque_loja)

precos_produtos = {"monitor": 850.50, "teclado": 120.00, "mouse": 85.00}
print(precos_produtos)

def calcular_imposto(preco_total):
      return preco_total * 0.15

produto_cliente = input("Qual produto você deseja comprar?")
produto_cliente = produto_cliente.lower()
if produto_cliente in estoque_loja and estoque_loja[produto_cliente] > 0:
    print("Produto disponível")

else:
    print("Produto não localizado em estoque")

try:
   quantidade_desejada = int(input("Quantos produtos você deseja?"))
   if quantidade_desejada <= estoque_loja[produto_cliente]:
      estoque_loja[produto_cliente] <= quantidade_desejada       

      valor_venda = precos_produtos[produto_cliente] * quantidade_desejada
            
      imposto_total = calcular_imposto(valor_venda)
      print("Venda realizada com sucesso!")
      print(f"Total de vendas: R$ {valor_venda:.2f}")  
      print(f"Imposto a ser pago: R$ {imposto_total:.2f}") 
   else:
      print("Quantidade do produto indisponível")

except ValueError:
       print("Entrada inválida. Por favor digite um número")

if "valor_venda" in locals():
    lucro_total = valor_venda - imposto_total
    print(f"Lucro total com a última venda: R$ {lucro_total:.2f}")


