import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('C:/Users/kaiqu/OneDrive/Área de Trabalho/Ciência de Dados/M9/clientes-v2.csv')

print(df.head())

# Codificação one-hot para 'estado_civil'
df = pd.concat(object[df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print("\nDataFrame após codificação one-hot para 'estado_civil':\n", df.head())

# Codificação ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['ensino_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)  # Mapeia os valores para as respostas

print("\nDataFrame após codificação ordinal para 'nivel_educacao':\n", df.head())

# Transformar 'area_atuacao' em categorias codificadas usando o método .cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print("\nDataFrame após transformar 'area_atuacao' em códigos numéricos:\n", df.head())

# LabelEncoder para 'estado'
# LabelEncoder converte cada valor único em números de 0 a n_classes-1
label_encoder = Label_encoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])

print("\nDataFrame após aplicar LabelEncoder em 'estado':\n", df.head())