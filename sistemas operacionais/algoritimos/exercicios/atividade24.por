programa {
 real distan, preco, num


  // Faça um algoritmo que pergunte a distância que um passageiro deseja
 //percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
 //viagens até 200Km e R$0.45 para viagens mais longas.

  funcao inicio() {
    escreva("escreva a distancia que você deseja percorrer (em Km):")
    leia(distan)
    se (distan <= 200) {
      escreva ("o valor a pagar é ",distan * 0.50)
    }
    senao {
      escreva("o valor a pagar é ",distan * 0.45)
    }

    




    
  }
}
