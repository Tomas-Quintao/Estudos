programa {
 real data, idade

  funcao inicio() {
    escreva("qual é o ano de seu nascimento:")
    leia(data)
    idade = 2025 - data 
    escreva ("A sua idade é ",idade)
    se (idade >= 16) {
      escreva (". Você pode votar")

    }
    senao{
      escreva(". Você ainda não pode votar ") 

    }

    

    




    
  }
}
