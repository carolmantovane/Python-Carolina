# vendas = 1000
# custo = 300
# impostos = 100

# print("O lucro foi de R$", vendas - custo - impostos)

faturamento = 1500 #variavel tipo int
custo = 700 #variavel tipo float (casa decimal)
novas_vendas = 100
imposto = faturamento*0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro/faturamento
faturamento = faturamento * novas_vendas
imposto = faturamento * 0,14


nome = "Carolina" #variavel tipo string
teve_lucro = True #variavel tipo boolano




print("O faturamento foi de R$", faturamento)
print("Os custos foram de R$", custo)
print("O lucro final foi de R$", lucro)
print("A carga tributária foi de R$", imposto)
print("A margem de lucro foi de R$", round(margem_lucro, 1))


tempo_contrato = 170
tempo_anos = 170/12
print("Tempo em anos", tempo_anos)
tempo_meses = 170 % 12
print ("Tempo em meses", tempo_meses)
