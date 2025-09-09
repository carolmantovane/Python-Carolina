try: 
   numero1 = int(input("Digite o primeiro numero:"))
   numero2 = int(input("Digite o segundo numero:"))
   numero3 = int(input("Digite o terceiro numero:"))
   print(f"Os numeros digitado foram: \n{numero1} \n{numero2} \n{numero3}")
except ValueError:
     #codigo que será executado se der erro 
     print("Entrada inválida! Por favor, digite apenas numeros.")
          