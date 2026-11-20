from src.guloso import troco_guloso

valor = 185

resultado = troco_guloso(valor)

print("PROBLEMA DO TROCO - ALGORITMO GULOSO")
print("------------------------------------")
print(f"Valor solicitado: R$ {valor / 100:.2f}")

print("\nMoedas utilizadas:")

for moeda, quantidade in resultado.items():
    print(f"{quantidade} moeda(s) de R$ {moeda / 100:.2f}")

total = sum(resultado.values())

print(f"\nQuantidade total de moedas: {total}")