programa { 
real valor,valor2,sub1,total
cadeia produto,produto2
real quantidade,quantidade2,sub2

  funcao inicio() {
   escreva ("supermercado preço bão\n") 
   escreva ("Vamos registrar sua compra")
     escreva("---PRODUTO 1---")
     escreva ("Digite o nome do protudo: ")
     leia(produto)
     escreva ("Digite a quantidade: ")
     leia (quantidade)
     escreva ("Digite o preço unitario(ex:5.50): ")
     leia (valor)
       escreva ("---produto 2---")
       escreva ("Digite o nome do produto: ")
       leia(produto2)
       escreva ("digite a quantidade:")
       leia(quantidade2)
       escreva ("digite o preço unitario:")
       leia(valor2)
       sub1 = valor * quantidade
       sub2 = valor2 * quantidade2
       total = sub1 + sub2
         escreva ("---RECIBO DA COMPRA---")
  
         escreva("\nItem:",produto)

         escreva("\nQtde:",quantidade,"|","Preço Unit:",valor,"|"," subtotal:R$",sub1)

         escreva("\nItem:",produto2)

         escreva("\nQtde:",quantidade2,"|","Preço Unit:",valor2,"|"," subtotal:R$",sub2)
         escreva ("\nVALOR TOTAL DA COMPRA: R$:",total)   



    
  
  }
}
