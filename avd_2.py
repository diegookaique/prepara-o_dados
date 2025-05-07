import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados_ex2.csv')

# Escreva seu código abaixo

min_max_scaler  = MinMaxScaler(feature_range=(0, 1))

df['Nota_MinMax'] = min_max_scaler.fit_transform(df[['Nota']])
df['N_Avaliacoes_MinMax'] = min_max_scaler.fit_transform(df[['N_Avaliacoes']])
df['Desconto_MinMax'] = min_max_scaler.fit_transform(df[['Desconto']])
df['Preco_MinMax'] = min_max_scaler.fit_transform(df[['Preco']])

label_encoder = LabelEncoder()

df['Marca_Cod'] = label_encoder.fit_transform(df['Marca'])

print("\nDataFrame após aplicar LabelEncoder em 'Marca':\n", df.head())

df['Material_Cod'] = label_encoder.fit_transform(df['Material'])

print("\nDataFrame após aplicar LabelEncoder em 'Material':\n", df.head())

df['Temporada_Cod'] = label_encoder.fit_transform(df['Temporada'])

print("\nDataFrame após aplicar LabelEncoder em 'Temporada':\n", df.head())