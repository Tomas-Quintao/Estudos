programa {
 //Constantes Globais 
 const inteiro xp_por_monstro = 150
 const real gp_medio_por_monstro = 25.5
 const real peso_loot_medio_por_monstro = 3.2
 const cadeia nome_monstro_padrao = "Cyclops" 
 // variaveis  
 cadeia nome_jogador
 inteiro montros_derrotados 
 real tempo // tempo de caça 
 real custo_supr // custo de suprimentos em GPs
 real xptotal
 real gptotal
 real pesototal
 real preju
 real mediaxp
 real mediagp

  funcao inicio() {
    // entrada de dados
    escreva ("---Relatorio Detalhado de Caçada no Tibia---")
    escreva ("\n Monstro Caçado:",nome_monstro_padrao)
    escreva ("\n")
    escreva ("Nome do seu personagem:")
    leia (nome_jogador)
    escreva ("quantos ",nome_monstro_padrao," voce derrotou:")
    leia (montros_derrotados)
    escreva ("tempo de caçada:")
    leia (tempo)
    escreva ("custo total de mantimentos (poções, etc.) em GPs:")
    leia (custo_supr)
    // saida de dados não processados 
    escreva ("\n-=-relatorio de caçada de ",nome_jogador,"-=-")
    escreva ("\nMonstro focado ",nome_monstro_padrao)
    escreva ("\nquantidade derrotada ",montros_derrotados)
    escreva ("\nTempo de caçada ", tempo)
    escreva ("\n==================================================")
    //calculos diversos
    xptotal = xp_por_monstro * montros_derrotados // calculo
    gptotal = gp_medio_por_monstro * montros_derrotados // calculo do gp total 
    pesototal = peso_loot_medio_por_monstro * montros_derrotados //calculo do peso total 
    preju = gptotal - custo_supr // calculo do prejuizo 
    mediaxp = xptotal / tempo
    mediagp = gptotal / tempo


   // saida final de dados 
    escreva ("\nxp total coletado: ",xptotal)
    escreva ("\nGP Total Estimado Coletado: ",gptotal," GPs")
    escreva ("\nPeso estimado do Loot: ",pesototal," Oz")
    escreva ("\n==================================================")
    escreva ("\nCusto de suprimentos:",custo_supr," GPs")
    escreva ("\nLucro/prejuizo Estimado:",preju," GPs") 
    escreva ("\n==================================================")
    escreva ("\nmédia de xp por hora:",mediaxp)
    escreva ("\nmédia de gp por hora:",mediagp)
    escreva ("\n--------------------------------------------------")
    escreva ("\nBom jogo ",nome_jogador,"!!!")
  


    
  }
}
