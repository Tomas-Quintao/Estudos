programa {
  real preco, cons, dist, total
  funcao inicio() {
    // entrada de dados 
    escreva ("preço do combustivel(R$/l)")
    leia(preco)
    escreva ("consumo do carro(km/l)")
    leia(cons)
    escreva ("distancia da viagem(km)")
    leia(dist)
    // aqui calculei distancia percorrida / consumo do carro * preço da gasolina
    total = (dist / cons) * preco  
    // saida de dados 
    escreva ("O custo total da viagem será de R$:",total)
  }
}
