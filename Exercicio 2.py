import json

# Suponha que temos o faturamento diário em um arquivo chamado faturamento.json
with open('faturamento.json', 'r') as f:
    dados = json.load(f)

# Filtrando apenas os dias com faturamento (ignorando zeros)
faturamento_diario = [valor for valor in dados if valor > 0]

# Calculando o menor e maior valor de faturamento
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# Calculando a média mensal
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Contando os dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
