import operação 
print("==calculadora")
print("1- somar")
print("2- subtrair")
print("3- multiplicar")
print("4- dividir")

opcao= int(input("escolha a operação"))
a= float(input("digite o primeiro numero"))
b= float(input("digite o segundo numero"))

if opcao == 1:
 print("resultado:",operação.soma(a, b)) 
elif opcao == 2:
 print ("resultado",operação.subtração(a, b))
elif opcao == 3:
  print("resultado",operação.multiplicação(a, b))
elif opcao == 4:
  print("resultado",operação.divisão(a, b))
else:
  print("opção invalida")
  