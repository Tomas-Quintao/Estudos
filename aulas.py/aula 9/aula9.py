try:
    a = int(input("numerador"))
    b = int(input("denominador"))
    d = a/b
except ZeroDivisionError: 
    print("não é possivel dividir por zero")
else:
    print(f"o resultado é:{d}")
finally:
    print("programa executado com sucesso") 
 
