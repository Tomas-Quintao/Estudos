programa {
cadeia nome
real peso,peso2
inteiro posse 


  funcao inicio() {
    //entrada de dados 
    escreva ("nome do item:")
    leia (nome)
    escreva ("peso unitario(Oz):")
    leia(peso)
    escreva ("quantidade em posse:")
    leia (posse)
    escreva ("---detalhes do item---")
    escreva ("\nItem: ",nome)
    escreva ("\nQuantidade ",posse)
    escreva ("\nPeso unitario: ",peso," Oz")
    // calculo do peso total 
     peso2 = posse * peso
     // saida de dados 
    escreva ("\nPeso total: ",peso2," Oz")
    




    
  }
}
