portugues = '''
00 Antes do mundo existir,
01 Ngutapa já existia.
02 Ele não teve pai nem mãe.'''

ticuna = '''
00 Nüma ga Ngutapa ga naãne nama'ã ya ĩĩtchicü,
01 rü nge'eǖ rü na tauma i ta'acü i nhũma na yema i na i aẽǖrü'ǖ.
02 Rü yiĩ'ǖ ngema na yamareǖ ga Ngutapa.'''

def construir_dicionario_traducao(texto_portugues,texto_ticuna):
    conto_portugues = portugues.split('\n')
    conto_ticuna = ticuna.split('\n')

    dicionario_portugues_ticuna = {}
    for i in range(len(conto_ticuna)):
        #print(conto_portugues[i][3:])
        #print(conto_ticuna[i][3:])
        if i:
            dicionario_portugues_ticuna[i-1] = (conto_portugues[i][3:],conto_ticuna[i][3:])
    #print(dicionario_portugues_ticuna.keys())
    print(dicionario_portugues_ticuna)
    #return dicionario_portugues_ticuna)

#def formatar_texto_json(texto_portugues, texto_ticuna):
    #print(construir_dicionario_traducao(texto_portugues,texto_ticuna))
'''
'''

dicionario_portugues_ticuna = {0: ('Antes do mundo existir,', "Nüma ga Ngutapa ga naãne nama'ã ya ĩĩtchicü,"), 1: ('Ngutapa já existia.', "rü nge'eǖ rü na tauma i ta'acü i nhũma na yema i na i aẽǖrü'ǖ."), 2: ('Ele não teve pai nem mãe.', "Rü yiĩ'ǖ ngema na yamareǖ ga Ngutapa.")}
#ideia, criar as chaves do dicionario e usar elas para navegar pela funcao
#e com isso ir decremtnado por ela e acessando os valores
dicionario_portugues_ticuna.keys()
tamanho_dicionario = len(dicionario_portugues_ticuna);
tamanho_inicial_dic = tamanho_dicionario
def combinar_textos_recursivamente(tamanho,dicionario):
    global tamanho_inicial_dic
    if tamanho == 0:
        print('[')
    elif tamanho < tamanho_inicial_dic:        
        combinar_textos_recursivamente(tamanho -1, dicionario_portugues_ticuna)
        print(' {')
        print(f'  "id": {tamanho-1},')
        print(f'  "translation": {{')
        print(f'   "pt": "{dicionario[tamanho-1][0]}",')
        print(f'   "tca": "{dicionario[tamanho-1][1]}"')
        print('  }')
        print(' },')
    else:
        combinar_textos_recursivamente(tamanho -1, dicionario_portugues_ticuna)
        print(' {')
        print(f'  "id": {tamanho-1},')
        print(f'  "translation": {{')
        print(f'   "pt": "{dicionario[tamanho-1][0]}",')
        print(f'   "tca": "{dicionario[tamanho-1][1]}"')
        print('  }')
        print(' }')
        print(']')
combinar_textos_recursivamente(tamanho_dicionario, dicionario_portugues_ticuna)

'''
    # Chama recursivamente para a próxima linha
    combinar_textos_recursivamente(num_linhas - 1, dicionario, chaves[1:])
"""


# Começa a combinação recursiva
#combinar_textos_recursivamente(len(dicionario_portugues_ticuna), dicionario_portugues_ticuna)


#combinar_textos_recursivamente(len(portugues.split('\n')), dicionario_portugues_ticuna)
#print(len(portugues.split('\n')))
#construir_dicionario_traducao(portugues,ticuna)
#formatar_texto_json(portugues, ticuna)

'''
# Função para navegar e acessar os valores do dicionário

