import pandas as pd 

dados_df = pd.read_excel("produtos_ficticios.xlsx")
#qual é o produto mais caro? e o mais barato?
mais_caro = dados_df.loc[dados_df["preço"].idxmax()]
print(mais_caro)

mais_barato = dados_df.loc[dados_df]["preço"].idexmax()]