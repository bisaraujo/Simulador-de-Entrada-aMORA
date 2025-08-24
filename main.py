from functions import valor_entrada, valor_a_guardar, parcela_mensal, parcela_anoN_igpm, parcela_anoN_juros

valor_imovel = int(input("Informe o valor do imóvel: "))
percentual_entrada = int(input("Informe o percentual da entrada: "))
anos_contrato = int(input("Informe a duração do contrato em anos: "))
taxa_juros = int(input("Informe a taxa de juros sugerida: "))

valor_entrada = valor_entrada(valor_imovel, percentual_entrada)
valor_a_guardar = valor_a_guardar(valor_imovel)
parcela_mensal = parcela_mensal(valor_a_guardar, anos_contrato)
dici_parcelas_igpm, valor_mensal_base = parcela_anoN_igpm(parcela_mensal, anos_contrato)
dici_parcelas_juros = parcela_anoN_juros(parcela_mensal, anos_contrato, taxa_juros)

print(f"- Valor da entrada: R${valor_entrada}")
print(f"Valor a guardar: R${valor_a_guardar}")
print(f'Valor mensal base: R${valor_mensal_base:.2f}')
print("Valor mensal pelo IGPM:")
for ano, valor in dici_parcelas_igpm.items():
    print(f"{ano}: R${valor:.2f}")

print(f"Valor mensal com {taxa_juros}% ao ano:")
for ano, valor in dici_parcelas_juros.items():
    print(f"{ano}: R${valor:.2f}")

