programa {
 real metro

  funcao inicio() {
    escreva("digite uma distancia em metros:")
    leia(metro)
    escreva("a distancia de ",metro, "M corresponde a:")
    //saida de dados e calculo para transformar as medidas:
    escreva("\n",metro / 1000 ," Km")
    escreva("\n",metro / 100," Hm")
    escreva("\n",metro /10," Dam")
    escreva("\n",metro * 10 , " dm")
    escreva("\n",metro * 100 , " cm")
    escreva("\n" ,metro * 1000 , " mm")



    
  }
}
