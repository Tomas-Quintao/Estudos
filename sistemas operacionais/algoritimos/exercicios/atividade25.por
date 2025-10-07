programa {


 //25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
//Analise seus comprimentos e diga se é possível formar um triângulo com essas
//retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
//de cada lado deve ser menor que a soma dos outros dois.





 real seg1, seg2, seg3, var1, somatest

  funcao inicio() {
    escreva("escreva o primeiro segmento:")
    leia(seg1)

    escreva("escreva o segundo segmento:")
    leia(seg2)

    escreva("escreva o terceiro segmento:")
    leia(seg3)
    //Para formar um triângulo com três segmentos de reta, é preciso verificar a Inequação Triangular: a soma de quaisquer dois lados deve ser sempre maior que o terceiro lado, e nunca menor ou igual
    // e é exatamente isso que essa parte do codigo faz
    somatest = seg1 + seg2
    se (somatest > seg3){
     escreva ("é possivel fazer um triangulo com essas medidas.")
     
    }
    senao {escreva("não é possivel fazer um triangulo com essas medidas.")}


  
  


    
  }
}
