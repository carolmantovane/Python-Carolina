# vendedor = "João"

# vendas = 400
# meta = 500

# if vendas >= meta:
#     print("bateu a meta")
# else:
#     print("Não bateu a meta")

from vendedor import Vendedor   

vendedor1 = Vendedor("João")
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)



vendedor2 = Vendedor("Pedro")
vendedor2.vendeu(300)
vendedor2.bateu_meta(600)