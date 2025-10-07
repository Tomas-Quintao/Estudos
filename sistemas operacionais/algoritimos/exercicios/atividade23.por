programa {
  real descf,descm,valor
  cadeia nome
  caracter sexu
  

  funcao inicio() {
    escreva ("escreva seu nome")
    leia (nome)
    escreva ("é homem ou mulher: (m para homem e f para Mulher)")
    leia (sexu)
    escreva ("valor da compra:")
    leia (valor)
    descf = valor * 13 / 100
    descm = valor * 5 / 100
    se (sexu == "f") {
      escreva ("com o desconto especial de dia das mulheres o valor da compra é: ",valor - descf)
    } 
    senao {escreva("Valor da compra",valor - descm)
    }




    
  }
}
