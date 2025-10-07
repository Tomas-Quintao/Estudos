programa {
 real larg, alt, metquad

  funcao inicio() {
    escreva("qual é a largura da parede?")
    leia(larg)
    escreva("qual é a altura da parede?")
    leia(alt)
    //calculo do metro quadrado 
    metquad = larg * alt
    escreva("\nA area da parede é ", metquad ," Metros quadrados")
    // calculo de quantidade de tinta 
    escreva("\nA quantidade de litros de tinta será ",metquad / 2)



    
  }
}
