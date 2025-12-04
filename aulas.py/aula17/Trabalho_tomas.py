"""
Vamos praticar Pandas usando o dataset Titanic.csv.
Este trabalho vale 15 pontos.

Lembre-se: o semestre está acabando e a prova está chegando.
Aprenda!!
"""

#--------------------------------------------------
# 1. Importação da biblioteca e carregamento
#--------------------------------------------------
import pandas as pd
#importe aqui a planilha
dados_df = pd.read_csv(r"C:\Users\Tomás Quintão\OneDrive\Documentos\Estudos\aulas.py\aula17\titanic.csv")

print(dados_df.head())

#--------------------------------------------------
# 2. Explorando o dataset
#--------------------------------------------------
#print("Explorando o database")
print(dados_df.info())
print(dados_df.describe())

#--------------------------------------------------
# 3. Exercícios (RESPONDA USANDO CÓDIGO EM PYTHON)
#--------------------------------------------------

# 1) Quantas linhas e colunas o dataset possui?
#    Dica: use df.shape
print("quantas linhas e colunas o dataset possui?")
print(dados_df.shape)


# 2) Qual é a idade média dos passageiros?
#    Dica: mean()
print("2) Idade média dos passageiros:")
print(dados_df["Age"].mean())



# 3) Trazer apenas as colunas 'Name' e 'Age'
print("colunas nome e idade:")
print(dados_df[['Name', 'Age']])




# 4) Trazer apenas os passageiros do sexo feminino
mulheres = dados_df.loc[dados_df["Sex"] == "female"]
print(mulheres)


# 5) Trazer apenas passageiros do sexo masculino com idade > 30
diferenca = dados_df.loc[(dados_df["Sex"] == "male") & (dados_df["Age"] > 30), ["Name", "Sex",'Age']]
print(diferenca) 




# 6) Mostrar apenas mulheres sobreviventes
as_sobreviventes = dados_df.loc[(dados_df['Sex'] == 'female') & (dados_df['Survived']),['Name', 'Sex', 'Survived']] 
print(as_sobreviventes)



# 7) Mostrar passageiros da 1ª classe com menos de 18 
passageiros_da_primeira_classe = dados_df.loc[(dados_df['Pclass'] == 1) & (dados_df['Age'] < 18), ['Name', 'Pclass', 'Sex', 'Age']]
print(passageiros_da_primeira_classe)


# 8) Criar uma coluna chamada 'Faixa' com:
#       - CRIANCA para idade < 18
#       - ADULTO para idade >= 18
dados_df["Faixa"] = dados_df["Age"].apply(lambda idade: "CRIANCA" if idade < 18 else "ADULTO")



# 9) Agrupar e mostrar taxa de sobrevivência por sexo
taxa_sobrevivencia = dados_df.groupby("Sex")["Survived"].mean()
print(taxa_sobrevivencia)



# 10) Mostrar a tarifa média por classe
# Supondo que seu DataFrame se chama df
# e que as colunas são "Pclass" (classe) e "Fare" (tarifa)

tarifa_media = dados_df.groupby("Pclass")["Fare"].mean()

print(tarifa_media)



# 11) Qual é a idade da pessoa mais velha do Titanic?
#     Dica: df['Age'].max()
#{print (dados_df['age'].max())}
print("11) Idade da pessoa mais velha do Titanic:")
print(dados_df['Age'].max())


# 12) Qual foi a tarifa mais alta paga no Titanic?
#     Dica: df['Fare'].max()
print("12) Qual foi a tarifa mais alta paga no Titanic?")
print(dados_df['Fare'].max())



# 13) Qual classe tinha mais passageiros?
#     Dica: use value_counts()
print("13) Qual classe tinha mais passageiros?")
print(dados_df['Pclass'].value_counts())



#--------------------------------------------------
# 5. Exportação
#--------------------------------------------------


# 14) Exportar apenas os sobreviventes para um arquivo CSV
sobreviventes = dados_df[dados_df['Survived'] == 1]

sobreviventes.to_csv("sobreviventes.csv", index=False)

print("Arquivo 'sobreviventes.csv' criado.")














