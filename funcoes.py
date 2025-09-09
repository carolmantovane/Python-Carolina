lista_precos = [2100, 1000, 800, 3000]

# imposto
# aliquota 1 - IR - 0.2
# aliquota 2 - ISS - 0.15
# aliquota 3 - CSLL - 0.05

def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco           
    #imposto_ir = 0.2 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total  

for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f"O valor total do imposto sobre o produto de R$ {preco} é de R$ {imposto_total}")


# nova_lista_produtos = [3000, 5000, 6000, 7000]
# for preco in nova_lista_produtos:
#     if preco <= 2000:
#         imposto_ir = 0.2 * preco
#     else:
#         imposto_ir = 0.3 * preco           
#     #imposto_ir = 0.2 * preco
#     imposto_iss = 0.15 * preco
#     imposto_csll = 0.05 * preco
#     imposto_total = imposto_ir + imposto_iss + imposto_csll
#     print(f"O valor total do imposto sobre o produto de R$ {preco} é de R$ {imposto_total}")
                       
               
           