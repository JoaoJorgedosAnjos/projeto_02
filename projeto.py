from assets.conto_nosso_povo_cap_1_ptbr_ticuna import portugues 
from assets.conto_nosso_povo_cap_1_ptbr_ticuna import ticuna 

def construir_dicionario_traducao(conto_portugues,conto_ticuna):
    conto_portugues = conto_portugues.split('\n')
    conto_ticuna = conto_ticuna.split('\n')
    dicionario_portugues_ticuna = {}
    for i in range(len(conto_ticuna)):
        if i:
            dicionario_portugues_ticuna[i-1] = (conto_portugues[i][3:],conto_ticuna[i][3:])
    return dicionario_portugues_ticuna    
    
def combinar_textos_recursivamente(tamanho_dic,dicionario,tamanho_inicial_dic):
    if tamanho_dic == 0:
        print('[')
    elif tamanho_dic < tamanho_inicial_dic:        
        combinar_textos_recursivamente(tamanho_dic -1, dicionario,tamanho_inicial_dic)
        print(' {')
        print(f'  "id": {tamanho_dic-1},')
        print(f'  "translation": {{')
        print(f'   "pt": "{dicionario[tamanho_dic-1][0]}",')
        print(f'   "tca": "{dicionario[tamanho_dic-1][1]}"')
        print('  }')
        print(' },')
    else:
        combinar_textos_recursivamente(tamanho_dic-1, dicionario,tamanho_inicial_dic)
        print(' {')
        print(f'  "id": {tamanho_dic-1},')
        print(f'  "translation": {{')
        print(f'   "pt": "{dicionario[tamanho_dic-1][0]}",')
        print(f'   "tca": "{dicionario[tamanho_dic-1][1]}"')
        print('  }')
        print(' }')
        print(']')
        
def formatar_texto_json(texto_portugues, texto_ticuna):
    dicionario_portugues_ticuna = construir_dicionario_traducao(texto_portugues,texto_ticuna)
    tamanho_dicionario = len(dicionario_portugues_ticuna);
    tamanho_inicial_dic = tamanho_dicionario
    combinar_textos_recursivamente(tamanho_dicionario, dicionario_portugues_ticuna,tamanho_inicial_dic)

formatar_texto_json(portugues,ticuna)

