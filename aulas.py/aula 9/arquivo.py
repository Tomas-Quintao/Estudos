
#with open("dados.txt","r") as arquivo:
#    conteudo = arquivo.read()
#
    #print(conteudo)
 # arquivo.write("golias")
#with open("dados.txt","a") as arquivo:
 #   arquivo.write("Supre")
with open("nomede.txt","w") as arquivo:
    a = (input("escreva seu nome:"))
    b = (input("escreva sua idade:"))
    arquivo.write(a)
with open ("nomede.txt","a") as arquivo:
    arquivo.write(b)
    
