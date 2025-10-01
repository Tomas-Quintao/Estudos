# NUMERO 1
num = int(input("escreva o primeiro numero:"))
num2 = int(input("escreva o segundo numero:"))
if num < num2:
    print ("o primeiro numero é menor que o segundo")
else:
    print ("o primeiro numero é maior que o segundo")
# NUMERO 2 

def saudacao(nome="visitante"):
   saudacao("bem vindo {nome}")



# NUMERO 3
num1 = int(input("escreva um numero:"))
num2 = int(input("escreva outro numero:"))
resut = num1 + num2 
print (resut,"é o resultado da soma")
# NUMERO 4
with open("alunos.txt","w") as arquivo:
    a = (input("\nescreva seu nome:"))
    b = (input("\nescreva mais um nome:"))
    c = (input("\nescreva outro nome:"))
    arquivo.write(a)
with open ("alunos.txt","a") as arquivo:
    arquivo.write(b)
    arquivo.write(c)
# NUMERO 5
try:
    num1 = int(input("escreva o primeiro numero:"))
    num2 = int(input("escreva o segundo numero:"))
    result = num1 / num2 
except ZeroDivisionError:
    print("impossivel dividir por zero")
else:
    print(f"o resultado é {result}")
finally:
    print("fim do programa ")
    
  

