def valor_entrada(valor_imovel, percentual_entrada):
    valor_entrada = valor_imovel * (percentual_entrada / 100)
    return valor_entrada

def valor_a_guardar(valor_imovel):
    total_a_guardar = valor_imovel * 0.15
    return total_a_guardar

def parcela_mensal(total_a_guardar, anos_contrato):
    parcela_mensal = total_a_guardar / (anos_contrato * 12)
    return parcela_mensal

def parcela_anoN_igpm(parcela_mensal, N):
    dici_parcelas_igpm = {}
    for ano in range(N, 0, -1):
        parcela_anoN_igpm = parcela_mensal * (1 + 0.06)**(ano-1)
        dici_parcelas_igpm[f'Ano {ano}'] = parcela_anoN_igpm
        if ano == 1:
            valor_mensal_base = parcela_anoN_igpm
            
    return dici_parcelas_igpm, valor_mensal_base

def parcela_anoN_juros(parcela_mensal, N, taxa_juros):
    dici_parcelas_juros = {}
    for ano in range(N, 0, -1):
        parcela_anoN_juros = parcela_mensal * (1 + taxa_juros/100)**(N-1)
        dici_parcelas_juros[f'Ano {ano}'] = parcela_anoN_juros
    return dici_parcelas_juros


    