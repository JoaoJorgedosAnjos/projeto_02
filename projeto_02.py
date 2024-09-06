portugues = '''
01 Antes do mundo existir,
02 Ngutapa já existia.
03 Ele não teve pai nem mãe.
'''

ticuna = '''
01 Nüma ga Ngutapa ga naãne nama'ã ya ĩĩtchicü,
02 rü nge'eǖ rü na tauma i ta'acü i nhũma na yema i na i aẽǖrü'ǖ.
03 Rü yiĩ'ǖ ngema na yamareǖ ga Ngutapa.
'''

def traduz_conto_ticuna_pro_portugues(texto_portugues,texto_ticuna):
    conto_portugues = texto_portugues.split('\n')
    conto_ticuna = texto_ticuna.split('\n')

    traducao = []
    dicio = {}
  
    print('[')
    
    for frase_ticuna in conto_ticuna:
        indice = frase_ticuna[:2]  
        texto_ticuna = frase_ticuna[3:]
        texto_ticuna = texto_ticuna.strip()
        dicio[indice] = [texto_ticuna]
    
        for frase_portugues in conto_portugues:
            if frase_portugues.startswith(indice) and indice != '':
                texto_portugues = frase_portugues[3:]  
                texto_portugues = texto_portugues.strip()
                dicio[indice] += [texto_portugues]
            
                print(' {')
                print(f'  "id":{int(indice)},')
                print('  "translation":{')
                print(f'   "pt": "{dicio[indice][1]}",')
                print(f'   "tca": "{dicio[indice][0]}",')
                print('  }')
                
                if indice != 27:
                    print(' },')
                else:
                    print(' }')
                
                break
    print(']')            

traduz_conto_ticuna_pro_portugues(portugues,ticuna)