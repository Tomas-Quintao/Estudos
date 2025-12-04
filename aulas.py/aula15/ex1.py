import pandas as pd
#mostre o nome e preço dos produtos com valor acima de 300,00 reais
dados_df = pd. read_excel("produtos_ficticios.xlsx")
print(dados_df.to_string())
caros = dados_df [dados_df["preços" > 300]["Nome do produto", ["preços"]]]

