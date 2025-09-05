programa {
 const cadeia magia="poção"
 const inteiro custo_mana = 20 // contante mantem o valor de uma variavel permanente
 inteiro quant, mana 


  funcao inicio() {
    escreva ("---calculadora de custo de mana (magia:energy bean)---")
    escreva ("quantas vezes você pretende lançar a 'magia energy beam'?")
    leia (quant)
    mana = custo_mana * quant
    escreva ("para lançar a magia 'energy beam'" ,quant," vez(es),você gastará: ",mana," de mana.")
 

    
  }
}
