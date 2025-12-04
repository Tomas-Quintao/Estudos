import pandas as pd
dados_df = pd.read_excel("produtos_ficticios.xlsx")
#print(dados_df.to_string())

#print(dados_df.columns)

#print(dados_df.shape) 

#produto = dados_df ['Descrição']
#print (produto)

#roupas = dados_df.loc[dados_df["Categoria"] == "Roupas",["Categoria", "Código do produto","preço" ]]
#print (roupas) 

#Cor = dados_df.loc [dados_df["Cor"]== "Preto"]
#produto_cor_df = dados_df.loc[("Categoria")] == ("Roupas") & (dados_df["Cor"=="Preto"])

print(dados_df.loc[5,"Código do produto"]) 

