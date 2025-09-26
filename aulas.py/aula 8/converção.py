import operação 
print("==converção==")
print("1-metro -> cm")
print("2-  cm -> metro")
print("3- km -> metro")

opcao= int(input("escolha a converção"))

a= float(input("digite o primeiro numero  "))

if opcao == 1:
 print("resultado:",operação.mcm(a))

elif opcao ==2 :
 print("resultado:  ",operação.cmm(a))
 
elif opcao ==2 :
 print("resultado:  ",operação.kmm(a))
else:
 print("opcao invalida")


