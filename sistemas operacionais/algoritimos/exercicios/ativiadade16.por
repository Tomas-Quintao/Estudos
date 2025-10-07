programa {
 real tempo, anos, diasperdidos,calculo
 inteiro cigarros

  funcao inicio() {
    escreva ("escreva quantos cigarros são consumidos por dia:")
    leia (cigarros)
    escreva ("quantos anos ja fumou:")
    leia (anos)
    calculo = anos * 365 + cigarros * 10
    diasperdidos = calculo / 1440
    escreva ("são aproximadamente",diasperdidos,"dias perdidos")




    
  }
}
