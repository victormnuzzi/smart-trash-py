from time import sleep
from random import randint
import json

# Função para definir o tamanho do programa no printdo terminal
def tamProg(titulo='Aplicativo SmartTrash'):
    return len(titulo) * 3 # armazenando em uma variável o tamanho do título para formatação do menu

# Função de linha simples para estética
def linSimples(tam):
    print('-' * tam)

# Função de linha com detalhe para estética
def linDetalhe(tam):
    print('-=' * tam)

# Função de sublinhado para estética
def subli(frase, variavel):
    linSimples(len(frase + str(variavel)))
    sleep(1)

# Função para mostrar opcão para sair do aplicativo e para voltar ao Menu Principal
def menuSairVoltar():
    # Menus:
      # Principal --> 0
      # Notificações --> 1
      # Ajuda --> 2
      # Sair --> 3
    sleep(0.4)
    if menu != 0:
        frase = len("[888] Voltar ao Menu Principal")
    else: 
        frase = len("[999] Sair do aplicativo")
    tam_sair = ((tam_titulo - frase ) // 2)
    print()
    print(' ' * (tam_sair - 3), '~' * (frase + 6))
    if menu != 0:
        print(' ' * tam_sair, f'{"[888] Voltar ao Menu Principal":^{tam_sair}}')
    print(' ' * tam_sair, f'{"[999] Sair do aplicativo":^{tam_sair}}')
    print(' ' * (tam_sair - 3), '~' * (frase + 6))
    print()

# Função para mostrar que usuário está voltando ao Menu Principal
def voltandoMenu(menu):
        sleep(0.7)
        print('\n')
        linSimples(len(f'Voltando ao Menu {menu}...'))
        print(f'Voltando ao Menu {menu}...')
        linSimples(len(f'Voltando ao Menu {menu}...'))
        print()
        sleep(1.3)

# Função para "carregar" o menu
def carregandoMenu(menu):
    print('\n')
    linSimples(len(f'Carregando o Menu {menu}...'))
    print(f'Carregando o Menu {menu}...')
    linSimples(len(f'Carregando o Menu {menu}...'))
    print()
    sleep(0.5)
        
def tratarErro(inputTratamento='',tipo=''):
    '''
    Função para tratar erros:
    - Inteiro
    - String
    :param inputTratamento: Frase do sistema para o usuário
    :param tipo: Tipo string "str" ou tipo inteiro "int"
    '''
    try:
        if tipo == 'str':
            # Se o tipo a ser tratado for string
            if not isinstance(inputTratamento, str):
                raise ValueError
            elif inputTratamento != 888 or inputTratamento != 999:
                pass
            elif inputTratamento.isdigit():
                raise ValueError
             
        elif tipo == 'int':
            # Se o tipo a ser tratado for inteiro
            if not inputTratamento.isdigit():
                raise ValueError
            else:
                return int(inputTratamento)

        else:
            # Se o tipo a ser tratado for diferente de string ou int
            raise ValueError

    except Exception:
        print('\n')
        print('\033[31m', f"{'#~~~~~~~~~~~~~~~~~~~# ERRO DE INPUT #~~~~~~~~~~~~~~~~~~~#':^{tamProg()}}")
        print(f"{f'Opção {inputTratamento} inválida. Por favor, tente novamente':^{tamProg()}}", '\033[m')
        sleep(0.7)
        return inputTratamento


# ------------- Programa principal --------------

menu = resp = perg = 0 # Menu é o principal  | resposta: opção do menu inicial | pergunta: tem certeza se deseja sair é 0
fechar = lig = 1 # Programa ligado (binário)
menus = []
nomes_lixeiras = ['Lixeira A', 'Lixeira B', 'Lixeira C']

while lig == 1:

    # Simulação dos sensores 

    with open("lixeiras.json", "r") as lixeiras_json:
        dados_lixeiras = json.load(lixeiras_json)

    for keys in dados_lixeiras:
        sensor_enchimento = randint(0, 100)
        dados_lixeiras[keys].update({'Enchimento (%)':sensor_enchimento})
        if sensor_enchimento < 50:
            dados_lixeiras[keys].update({'Coleta':'Concluida'})
        elif sensor_enchimento >= 50 and sensor_enchimento < 75:
            dados_lixeiras[keys].update({'Coleta':'Pendente'})
        else:
            dados_lixeiras[keys].update({'Coleta':'Em andamento'})


    with open("lixeiras.json", "w") as lixeiras_json:
        json.dump(dados_lixeiras, lixeiras_json)


    # Loop programa principal
    while fechar == 1:
        menus.append(menu) # adicionar menu na lista para listar operação do usuário no fim do programa 
        # Menu Principal

        tam_titulo = tamProg()

        # Print do título
        print()
        linDetalhe(tam_titulo // 2)
        print(f'\n{"Aplicativo SmartTrash":^{tam_titulo}}\n')
        linDetalhe(tam_titulo // 2)
        print()

        # Formatação menu
        frase = len('[4] Verificar Lixeiras')
        tam_opcoes = ((tam_titulo - (frase)) // 2)
        print()
        linSimples(tam_titulo)
        print(f'\n{"MENU PRINCIPAL":^{tam_titulo}}\n')
        print(' ' * (tam_opcoes - 4), '-' * (frase + 6))
        print(' ' * (tam_opcoes - 1), '[1] Notificações')
        print(' ' * (tam_opcoes - 1), '[2] Preciso de ajuda')
        print(' ' * (tam_opcoes - 1), '[3] Enviar sugestões')
        print(' ' * (tam_opcoes - 1), '[4] Verificar Lixeiras')
        print(' ' * (tam_opcoes - 4), '-' * (frase + 6))
        print('\n')
        linSimples(tam_titulo)

        # Menu Digite 999 para sair
        menuSairVoltar()

        # Input do usuário  -->  verificação de erro
        resp = input('\nSelecione uma opção: ')
        subli('Selecione uma opção: ', resp)

        resp = tratarErro(resp, 'int')

        sleep(1)
        # Verificação da escolha do Menu Principal
        if resp == 1: # Menu notificações
            menu = 1 # para menu ser Notificações
            menus.append(menu) # adicionar menu na lista para listar operação do usuário no fim do programa
            # Mensagem de carregando menu
            carregandoMenu('Notificações')
            # Formatação menu
            print()
            frase = len('Você não tem nenhuma notificação.')
            tam_notif = ((tam_titulo - frase ) // 2)
            linSimples(tam_titulo)  
            print(f'\n{"NOTIFICACÕES":^{tam_titulo}}\n')            
            print(' ' * (tam_notif - 3), '~' * (frase + 6))
            print(' ' * tam_notif, f'{"Você não tem nenhuma notificação.":^{tam_notif}}')
            print(' ' * (tam_notif - 3), '~' * (frase + 6))
            print('\n')
            linSimples(tam_titulo)  

            sleep(1)
            
            voltandoMenu('Principal') 

        elif resp == 2: # Menu ajuda
            while True:
                menu = 2 # para menu ser Ajuda
                menus.append(menu) # adicionar menu na lista para listar operação do usuário no fim do programa 
                # Mensagem de carregando menu
                carregandoMenu('Ajuda')
                # Formatação menu
                print()
                frase = len('[4] Que tipo de lixo posso descartar na lixeira?')
                tam_ajuda = ((tam_titulo - (frase)) // 2)
                linSimples(tam_titulo)
                print(f'\n{"AJUDA":^{tam_titulo}}')
                print()
                print(' ' * (tam_ajuda - 4), '-' * (frase + 6))
                print(' ' * (tam_ajuda - 1), '[1] Como funciona para descartar o lixo?')
                print(' ' * (tam_ajuda - 1), '[2] Como funciona a coleta de lixo?')
                print(' ' * (tam_ajuda - 1), '[3] Como posso enviar sugestões?')
                print(' ' * (tam_ajuda - 1), '[4] Que tipo de lixo posso descartar na lixeira?')
                print(' ' * (tam_ajuda - 1), '[5] Como a lixeira inteligente funciona?')
                print(' ' * (tam_ajuda - 1), '[6] Desejo entrar em contato com o suporte.')
                print(' ' * (tam_ajuda - 4), '-' * (frase + 6))
                print('\n')
                linSimples(tam_titulo)
                
                menuSairVoltar()

                # input do usuário
                duvida = input('\nQual é o número da sua dúvida? ')
                subli('Qual é o número da sua dúvida? ', duvida)

                duvida = tratarErro(duvida, 'int')

                print()

                try:
                    if 6 >= duvida and duvida >= 1:
                        menus.append(duvida + 20) # adicionar menu na lista para listar operação do usuário no fim do programa
                    
                    if duvida == 1: # Opção 1 - Como funciona para descartar o lixo?
                        print('\nVocê deve se direcionar até a lixeira inteligente, colocar o lixo no espaço destinado, esperar até que a lixeira analise o material e o separe adequadamente.') 
                        sleep(2)
                        voltandoMenu('Ajuda')
                    elif duvida == 2: # Opção 2 - Como funciona a coleta de lixo?
                        print('A coleta de lixo é feita automaticamente por uma empresa de reciclagem quando a lixeira inteligente fica próxima de sua capacidade máxima.') 
                        sleep(2)                    
                        voltandoMenu('Ajuda')       
                    elif duvida == 3: # Opção 3 - Como posso enviar sugestões?
                        print('\nPara enviar sugestões, você deve selecionar no menu principal a opção "[3] Enviar sugestões".') 
                        sleep(2)  
                        voltandoMenu('Ajuda')     
                    elif duvida == 4: # Opção 4 - Que tipo de lixo posso descartar na lixeira inteligente?
                        print('\nVocê pode descartar o lixo desde que ele seja de: metal, plástico, papel ou vidro.') 
                        sleep(2)      
                        voltandoMenu('Ajuda') 
                    elif duvida == 5: # Opção 5 - Como a lixeira inteligente funciona?
                        print('\nA lixeira inteligente separa o lixo automaticamente com sensores sem você precisar se preocupar com qual material ele é feito. Basta apenas colocar separadamente o lixo dentro da lixeira e ela se encarrega do resto!') 
                        sleep(2)     
                        voltandoMenu('Ajuda')  
                    elif duvida == 6: # Opção 6 - Desejo entrar em contato com o suporte.
                        print('\nEnvie um email com a sua dúvida para: help@cleantech.com.br') 
                        sleep(2)      
                        voltandoMenu('Ajuda') 
                    elif duvida == 888: # Voltar ao menu principal
                        menus.append(888) # adicionar menu na lista para listar operação do usuário no fim do programa
                        voltandoMenu('Principal') 
                        break
                    elif duvida == 999: # Sair do aplicativo
                        fechar = 0
                        menus.append(999) # adicionar menu na lista para listar operação do usuário no fim do programa
                        break
                    else:
                        tratarErro(duvida)
                except:
                    pass

        elif resp == 3: # Menu sugestões
            while True:
                menu = 3 # para menu ser Sugestões
                menus.append(menu) # adicionar menu na lista para listar operação do usuário no fim do programa 
                # Mensagem de carregando menu
                carregandoMenu('Sugestões')
                # Formatação menu
                print()
                linSimples(tam_titulo)  
                frase = len('Envie uma sugestão ou relate um bug :)')
                tam_sug = ((tam_titulo - frase ) // 2)
                print(f'\n{"SUGESTÕES":^{tam_titulo}}\n')    
                print(' ' * (tam_sug - 3), '-' * (frase + 6))
                print(' ' * tam_sug, f'{"Envie uma sugestão ou relate um bug :)":^{tam_sug}}')
                print(' ' * (tam_sug - 3), '-' * (frase + 6))       
                print('\n')
                linSimples(tam_titulo)  
                menuSairVoltar()
                sug = input('\nDigite a sua sugestão: ')
                subli('Digite a sua sugestão: ', sug)

                tratarErro(sug, 'str')

                if sug.isdigit():
                    # Verificando se a sugestão não é 999 ou 888
                    if sug == '888':
                        menus.append(888) # adicionar menu na lista para listar operação do usuário no fim do programa 
                        voltandoMenu('Principal')                
                        break
                    elif sug == '999':
                        fechar = 0
                        menus.append(999) # adicionar menu na lista para listar operação do usuário no fim do programa 
                        break
                    else:
                        print('\033[31m', '\n\nO valor digitado precisa ser alfabético! Digite novamente.')
                        subli('O valor digitado precisa ser alfabético! Digite novamente.', 0)
                        print('\033[m', end='')

                # Confirmação do envio da sugestão
                else:
                    verificar_sug = sug.replace(' ', '') # verificar se é vazia
                    if len(verificar_sug) == 0:
                        print('\033[31m', '\n\nO valor digitado não pode ser vazio! Digite novamente.')
                        subli('O valor digitado não pode ser vazio! Digite novamente.', 0)
                        print('\033[m')
                    else:
                        sleep(1)
                        print(f'\n\n\033[32mA sugestão "{sug}" foi enviada com sucesso!\033[m')
                        sleep(1)
                        voltandoMenu('Principal')
                        break
        elif resp == 4: # Menu Verificar lixeiras
            while True:
                menu = 4
                menus.append(menu) # adicionar menu na lista para listar operação do usuário no fim do programa
                # Mensagem de carregando menu
                carregandoMenu('Verificar Lixeiras')
                # Formatação menu
                print()
                frase = len('[3] Lixeira Z')
                tam_lixeira = ((tam_titulo - (frase)) // 2)
                linSimples(tam_titulo)
                print(f'\n{"Lixeiras":^{tam_titulo}}')
                print()
                print(' ' * (tam_lixeira - 4), '-' * (frase + 6))
                for l in range(0, len(nomes_lixeiras)):
                    print(' ' * (tam_lixeira - 1), f'[{l+1}]', nomes_lixeiras[l])
                print(' ' * (tam_lixeira - 4), '-' * (frase + 6))
                print('\n')
                linSimples(tam_titulo)
                
                menuSairVoltar()

                # input do usuário
                escolha_lixeira = input('\nQual lixeira você deseja verificar? ')
                subli('Qual lixeira você deseja verificar? ', escolha_lixeira)

                escolha_lixeira = tratarErro(escolha_lixeira, 'int')

                print()

                try:
                    if int(escolha_lixeira):
                        if 3 >= escolha_lixeira and escolha_lixeira >= 1:
                            menus.append(escolha_lixeira + 40) # adicionar menu na lista para listar operação do usuário no fim do programa
                            linDetalhe(20)
                            print()
                            print(f'\033[35m{nomes_lixeiras[escolha_lixeira-1]:^40}\033[m\n')
                            for k, v in dados_lixeiras[f'lixeira{escolha_lixeira}'].items():
                                sleep(1)
                                print(f'- \033[33m{k}\033[m: {v}')
                            print()
                            linDetalhe(20)
                            sleep(4)

                        elif escolha_lixeira == 888: # Voltar ao menu principal
                            menus.append(888) # adicionar menu na lista para listar operação do usuário no fim do programa
                            voltandoMenu('Principal') 
                            break
                        elif escolha_lixeira == 999: # Sair do aplicativo
                            fechar = 0
                            menus.append(999) # adicionar menu na lista para listar operação do usuário no fim do programa
                            break
                        else:
                            tratarErro(escolha_lixeira)
                except:
                    pass

        elif resp == 999: # Sair do aplicativo
            menus.append(999) # adicionar menu na lista para listar operação do usuário no fim do programa 
            fechar = 0
            perg = 0
        
    menu = 0 # para menu voltar a ser o Principal
    resp = 0
    
    # Loop para usuário decidir se quer sair ou ficar no programa
    while perg != 1 and perg != 2:
        cont = 1
        print()
        linSimples(tam_titulo)
        print(f'\n{"OPERAÇÃO REALIZADA":^{tam_titulo}}\n') # Título do Menu Operação

        frase = len('Menu Notificações')
        tam_operacao = ((tam_titulo - (frase)) // 2)
        print(' ' * (tam_operacao - 4), '-' * (frase + 6))
        # Listar operação realizada pelo usuário 
        for m in menus:
            print(' '* (tam_operacao - 1), f'[{cont}]',end=' ')
            if m == 0: # 0 de Menu Principal
                print('Menu Principal')
            elif m == 1: # 1 de Menu Notificações
                print('Menu Notificações')
            elif m == 2: # 2 de Menu Ajuda
                print('Menu Ajuda')
            elif 26 >= m and m >= 21: # 26 a 21 são as dúvidas (2 de Menu Ajuda + núm dúvida)
                print(f'Dúvida {m-20}')
            elif m == 3: # 3 de Menu Sugestões
                print('Menu Sugestões')
            elif m == 4:
                print('Menu Lixeiras')
            elif 43 >= m and m >= 41: # 46 a 41 são as dúvidas (4 de Menu Ajuda + núm dúvida)
                print(f'Lixeira {m-40}')
            elif m == 888: # 888 de voltar ao menu anterior
                print(f'Voltou' )
            elif m == 999: # 999 de Menu Sair
                print('Menu Sair')

            cont += 1
        print(' ' * (tam_operacao - 4), '-' * (frase + 6))


        print()
        linSimples(tam_titulo)
        print()

        sleep(0.7)
        # Formatação da opção de saída ou permanência do aplicativo
        frase = len('[1] Voltar')
        tam_sair = ((tam_titulo - (frase)) // 2)
        print()
        print('~' * tam_titulo)
        print(f'\n{"Você tem certeza que deseja sair do aplicativo?":^{tam_titulo}}\n')
        print(' ' * (tam_sair - 4), '-' * (frase + 6))
        print(' ' * (tam_sair - 1), '[1] Voltar')
        print(' ' * (tam_sair - 1), '[2] Sair')
        print(' ' * (tam_sair - 4), '-' * (frase + 6))
        print()
        print('~' * tam_titulo)

        # Input do usuário
        perg = input('\nOpção: ')
        subli('Opção: ', perg)

        perg = tratarErro(perg, 'int')

        # Verificação do input
        if perg == 1:
            fechar = 1
            voltandoMenu('Principal')
        elif perg == 2: 
            lig = 0


# Print final - Programa encerra
sleep(0.5)
print('\n\n')
linDetalhe(tam_titulo // 2)
print(f'\n{"Fechando aplicativo...":^{tam_titulo}}\n')
linDetalhe(tam_titulo // 2)
print('\n\n')
sleep(2)