from functions import valor_entrada, valor_a_guardar, parcela_mensal, parcela_anoN_igpm, parcela_anoN_juros

# ===== Entrada de dados do usuário =====
valor_imovel = int(input("Informe o valor do imóvel: "))
percentual_entrada = int(input("Informe o percentual da entrada: "))
anos_contrato = int(input("Informe a duração do contrato em anos: "))
taxa_juros = int(input("Informe a taxa de juros sugerida: "))

# ===== Cálculos =====
valor_entrada_calculado = valor_entrada(valor_imovel, percentual_entrada)  # valor da entrada
valor_a_guardar_calculado = valor_a_guardar(valor_imovel)                  # valor total a guardar
parcela_mensal_calculada = parcela_mensal(valor_a_guardar_calculado, anos_contrato)  # parcela mensal base

# dicionários com valores anuais
dici_parcelas_igpm, valor_mensal_base = parcela_anoN_igpm(parcela_mensal_calculada, anos_contrato)
dici_parcelas_juros = parcela_anoN_juros(parcela_mensal_calculada, anos_contrato, taxa_juros)

# ===== Saída dos resultados =====
print(f"- Valor da entrada: R${valor_entrada_calculado:.2f}")
print(f"- Valor a guardar: R${valor_a_guardar_calculado:.2f}")
print(f"- Valor mensal base: R${valor_mensal_base:.2f}")

print("\nValor mensal pelo IGPM:")
for ano, valor in dici_parcelas_igpm.items():
    print(f"{ano}: R${valor:.2f}")

print(f"\nValor mensal com {taxa_juros}% ao ano:")
for ano, valor in dici_parcelas_juros.items():
    print(f"{ano}: R${valor:.2f}")
