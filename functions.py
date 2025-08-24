# Calcula o valor da entrada do imóvel
def valor_entrada(valor_imovel, percentual_entrada):
    return valor_imovel * (percentual_entrada / 100)

# Calcula 15% do valor do imóvel a ser guardado
def valor_a_guardar(valor_imovel):
    return valor_imovel * 0.15

# Calcula a parcela mensal base (total a guardar dividido pelos meses do contrato)
def parcela_mensal(total_a_guardar, anos_contrato):
    return total_a_guardar / (anos_contrato * 12)

# Calcula o valor mensal corrigido pelo IGPM para cada ano
def parcela_anoN_igpm(parcela_mensal, N):
    dici_parcelas_igpm = {}
    for ano in range(1, N+1):
        parcela_anoN_igpm = parcela_mensal * (1 + 0.06)**(ano-1)
        dici_parcelas_igpm[f'Ano {ano}'] = parcela_anoN_igpm
        if ano == 1:
            valor_mensal_base = parcela_anoN_igpm  # salva a primeira parcela para exibir como base
    return dici_parcelas_igpm, valor_mensal_base

# Calcula o valor mensal com juros composto anual para cada ano
def parcela_anoN_juros(parcela_mensal, N, taxa_juros):
    dici_parcelas_juros = {}
    for ano in range(1, N+1):
        parcela_anoN_juros = parcela_mensal * (1 + taxa_juros/100)**(ano-1)  
        dici_parcelas_juros[f'Ano {ano}'] = parcela_anoN_juros
    return dici_parcelas_juros
