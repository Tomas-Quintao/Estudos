programa {
 const real per_de_desconto = 0.15 //valor fixo do desconto : 15%
cadeia prod
real preco, prefinal,des

  funcao inicio() {
    // entrada de dados 
    escreva("Nome do produto:")
    leia (prod)
    escreva("preço original:")
    leia (preco)
    //calculo da porcentagem 
    des = preco * per_de_desconto // desconto = preço vezes percentual de desconto 
    prefinal =   preco - des //preço final = preço menos desconto
    //saida de dados 
    escreva("-+-preço promocional-+-")
    escreva("\nproduto:",prod)
    escreva("\npreço original",preco)
    escreva("\ndesconto(15%):",des)
    escreva("\npreço final:R$",prefinal)


    
  }
}
