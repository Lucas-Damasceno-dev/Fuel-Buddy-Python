"""
/***********************************************************************************************
Autor: LUCAS DA CONCEIÇÃO DAMASCENO
Componente Curricular: EXA 854 - MI - Algoritmos
Comcluído em: 02/09/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação
************************************************************************************************/
"""

# Solicita o nome do primeiro posto e o converte para letras maiúsculas sem espaços à direita/esquerda.
nome_posto1 = str(input('Digite o nome do primeiro posto: ')).strip().upper()

# Solicita e valida o preço da gasolina no posto 1.
preco_gasolina_posto1 = input('Digite o valor da gasolina no posto 1: R$')
while not preco_gasolina_posto1.replace('.', '').isdigit() and not preco_gasolina_posto1.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_gasolina_posto1 = input('Digite o valor da gasolina no posto 1: R$')
preco_gasolina_posto1 = float(preco_gasolina_posto1.replace(',', '.'))

# Solicita e valida o preço do etanol no posto 1.
preco_etanol_posto1 = input('Digite o valor da etanol no posto 1: R$')
while not preco_etanol_posto1.replace('.', '').isdigit() and not preco_etanol_posto1.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_etanol_posto1 = input('Digite o valor do etanol no posto 1: R$')
preco_etanol_posto1 = float(preco_etanol_posto1.replace(',', '.'))

# Solicita e valida o preço do diesel no posto 1.
preco_diesel_posto1 = input('Digite o valor da diesel no posto 1: R$')
while not preco_diesel_posto1.replace('.', '').isdigit() and not preco_diesel_posto1.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_diesel_posto1 = input('Digite o valor do diesel no posto 1: R$')
preco_diesel_posto1 = float(preco_diesel_posto1.replace(',', '.'))

# Inicializa contadores e acumuladores para o primeiro posto.
numero_de_vezes_posto_1_teve_menor_preco = 0
quantidade_de_litros_abastecidos_no_posto_1 = 0

# Solicita o nome do segundo posto e o converte para letras maiúsculas sem espaços à direita/esquerda.
nome_posto2 = str(input('Digite o nome do segundo posto: ')).strip().upper()

# Solicita e valida o preço da gasolina no posto 2.
preco_gasolina_posto2 = input('Digite o valor da gasolina no posto 2: R$')
while not preco_gasolina_posto2.replace('.', '').isdigit() and not preco_gasolina_posto2.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_gasolina_posto2 = input('Digite o valor da gasolina no posto 2: R$')
preco_gasolina_posto2 = float(preco_gasolina_posto2.replace(',', '.'))

# Solicita e valida o preço do etanol no posto 2.
preco_etanol_posto2 = input('Digite o valor da etanol no posto 2: R$')
while not preco_etanol_posto2.replace('.', '').isdigit() and not preco_etanol_posto2.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_etanol_posto2 = input('Digite o valor do etanol no posto 2: R$')
preco_etanol_posto2 = float(preco_etanol_posto2.replace(',', '.'))

# Solicita e valida o preço do diesel no posto 2.
preco_diesel_posto2 = input('Digite o valor da diesel no posto 2: R$')
while not preco_diesel_posto2.replace('.', '').isdigit() and not preco_diesel_posto2.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_diesel_posto2 = input('Digite o valor do diesel no posto 2: R$')
preco_diesel_posto2 = float(preco_diesel_posto2.replace(',', '.'))

# Inicializa contadores e acumuladores para o segundo posto.
numero_de_vezes_posto_2_teve_menor_preco = 0
quantidade_de_litros_abastecidos_no_posto_2 = 0

# Solicita o nome do terceiro posto e o converte para letras maiúsculas sem espaços à direita/esquerda.
nome_posto3 = str(input('Digite o nome do terceiro posto: ')).strip().upper()

# Solicita e valida o preço da gasolina no posto 3.
preco_gasolina_posto3 = input('Digite o valor da gasolina no posto 3: R$')
while not preco_gasolina_posto3.replace('.', '').isdigit() and not preco_gasolina_posto3.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_gasolina_posto3 = input('Digite o valor da gasolina no posto 3: R$')
preco_gasolina_posto3 = float(preco_gasolina_posto3.replace(',', '.'))

# Solicita e valida o preço do etanol no posto 3.
preco_etanol_posto3 = input('Digite o valor da etanol no posto 3: R$')
while not preco_etanol_posto3.replace('.', '').isdigit() and not preco_etanol_posto3.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_etanol_posto3 = input('Digite o valor do etanol no posto 3: R$')
preco_etanol_posto3 = float(preco_etanol_posto3.replace(',', '.'))

# Solicita e valida o preço do diesel no posto 3.
preco_diesel_posto3 = input('Digite o valor da diesel no posto 3: R$')
while not preco_diesel_posto3.replace('.', '').isdigit() and not preco_diesel_posto3.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_diesel_posto3 = input('Digite o valor do diesel no posto 3: R$')
preco_diesel_posto3 = float(preco_diesel_posto3.replace(',', '.'))

# Inicializa contadores e acumuladores para o terceiro posto.
numero_de_vezes_posto_3_teve_menor_preco = 0
quantidade_de_litros_abastecidos_no_posto_3 = 0

# Inicializa o contador de consultas.
quantidade_de_consultas = 0

# Inicia o loop do menu até que a escolha seja '3' (Sair do sistema).
menu = 0
while menu != 3:
    # Apresenta o menu ao usuário e solicita sua escolha.
    menu = input('-=-=-=-=-=-=-=-MENU-=-=-=-=-=-=-=-\n'
                 '1 - Consultar o sistema.\n'
                 '2 - Todas as informações.\n'
                 '3 - Sair do sistema.\n'
                 'Digite sua escolha: ')

    # Valida se a escolha é um número e se está entre 1 e 3.
    while not menu.isdigit() or not (0 < int(menu) < 4):
        print('Esse tipo de resposta não é válida... Tente novamente.')
        menu = input('Digite sua escolha: [1; 2; 3] ')
    menu = int(menu)

    # Se a escolha for '1', inicia a consulta de combustível.
    if menu == 1:
        # Solicita o tipo de combustível desejado (Gasolina, Etanol ou Diesel).
        tipo_de_combustivel = input(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
                                    'TIPOS DE COMBUSTÍVEIS;\n'
                                    '1 - Gasolina.\n'
                                    '2 - Etanol.\n'
                                    '3 - Diesel.\n'
                                    'Digite sua escolha: ')

        # Valida se a escolha é um número e se está entre 1 e 3.
        while not tipo_de_combustivel.isdigit() or not (0 < int(tipo_de_combustivel) < 4):
            print('Esse tipo de resposta não é válida... Tente novamente.')
            tipo_de_combustivel = input('Digite sua escolha: [1; 2; 3] ')
        tipo_de_combustivel = int(tipo_de_combustivel)

        # Converte o tipo de combustível escolhido em uma string.
        if tipo_de_combustivel == 1:
            tipo_de_combustivel = 'Gasolina'
        elif tipo_de_combustivel == 2:
            tipo_de_combustivel = 'Etanol'
        else:
            tipo_de_combustivel = 'Diesel'

        # Solicita a quantidade de litros desejada e valida se é um número válido.
        litragem = input(f'Quantos litros de {tipo_de_combustivel} você quer comprar? ')
        while not litragem.replace('.', '').isdigit() and not litragem.replace(',', '').isdigit():
            print('Esse tipo de resposta não é válida... Tente novamente.')
            litragem = input(f'Quantos litros de {tipo_de_combustivel} você quer comprar? ')
        litragem = float(litragem.replace(',', '.'))

        # Incrementa o contador de consultas.
        quantidade_de_consultas += 1

        print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

        # Verifica se o tipo de combustível escolhido pelo usuário é 'Gasolina'.
        if tipo_de_combustivel == 'Gasolina':
            # Verifica se todos os postos têm o mesmo preço para a gasolina.
            if preco_gasolina_posto1 == preco_gasolina_posto2 == preco_gasolina_posto3:
                # Solicita ao usuário que escolha um posto se todos têm o mesmo preço.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por litro de gasolina: R${preco_gasolina_posto1}\n'
                                      f'Neste caso, por favor, escolha em qual posto deseja abastecer:\n'
                                      f'1 - Posto {nome_posto1}.\n'
                                      f'2 - Posto {nome_posto2}.\n'
                                      f'3 - Posto {nome_posto3}.\n'
                                      f'Digite sua escolha: ')

                # Valida a escolha do usuário para garantir que seja um número entre 1 e 3.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 4):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2; 3] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_1_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_1 += litragem
                elif escolha_posto == 2:
                    numero_de_vezes_posto_2_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_2 += litragem
                else:
                    numero_de_vezes_posto_3_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_3 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço da gasolina no posto 1 é igual ao preço da gasolina no posto 2 e menor que no posto 3.
            if preco_gasolina_posto1 == preco_gasolina_posto2 < preco_gasolina_posto3:
                # Solicita ao usuário que escolha entre os postos 1 e 2, já que eles têm o preço mais baixo.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por litro de gasolina: R${preco_gasolina_posto1}\n'
                                      f'Neste caso, por favor, escolha em qual posto deseja abastecer:\n'
                                      f'1 - Posto {nome_posto1}.\n'
                                      f'2 - Posto {nome_posto2}.\n'
                                      f'Digite sua escolha: ')

                # Valida a escolha do usuário para garantir que seja um número entre 1 e 2.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 3):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_1_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_1 += litragem
                else:
                    numero_de_vezes_posto_2_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_2 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço da gasolina no posto 1 é igual ao preço da gasolina no posto 3 e menor que no posto 2.
            elif preco_gasolina_posto1 == preco_gasolina_posto3 < preco_gasolina_posto2:
                # Solicita ao usuário que escolha entre os postos 1 e 3, já que eles têm o preço mais baixo.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por litro de gasolina: R${preco_gasolina_posto1}\n'
                                      f'Neste caso, por favor, escolha em qual posto deseja abastecer:\n'
                                      f'1 - Posto {nome_posto1}.\n'
                                      f'2 - Posto {nome_posto3}.\n'
                                      f'Digite sua escolha: ')

                # Valida a escolha do usuário para garantir que seja um número entre 1 e 2.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 3):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_1_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_1 += litragem
                else:
                    numero_de_vezes_posto_3_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_3 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço da gasolina no posto 2 é igual ao preço da gasolina no posto 3 e menor que no posto 1.
            elif preco_gasolina_posto2 == preco_gasolina_posto3 < preco_gasolina_posto1:
                # Solicita ao usuário que escolha entre os postos 2 e 3, já que eles têm o preço mais baixo.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por litro de gasolina: R${preco_gasolina_posto1}\n'
                                      f'Neste caso, por favor, escolha em qual posto deseja abastecer:\n'
                                      f'1 - Posto {nome_posto2}.\n'
                                      f'2 - Posto {nome_posto3}.\n'
                                      f'Digite sua escolha: ')
                # Valida a escolha do usuário para garantir que seja um número entre 1 e 2.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 3):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_2_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_2 += litragem
                else:
                    numero_de_vezes_posto_3_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_3 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço da gasolina no posto 1 é menor que o preço no posto 2 e igual ao preço no posto 3.
            elif preco_gasolina_posto1 < preco_gasolina_posto2 == preco_gasolina_posto3:
                menor_gasto = litragem * preco_gasolina_posto1
                media_gasto_1_2 = litragem * preco_gasolina_posto2
                economia = media_gasto_1_2 - menor_gasto

                # Exibe informações sobre o posto mais barato e a economia.
                print(f'O posto {nome_posto1} é o posto com a gasolina mais barata: R${preco_gasolina_posto1:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto1}, você pagará R${menor_gasto}\n'
                      f'Os postos ({nome_posto2}; {nome_posto3}) '
                      f'cobram o mesmo valor por litro de gasolina: R${preco_gasolina_posto2}\n'
                      f'Economizará R${economia} no total em comparação aos postos ({nome_posto2}; {nome_posto3})\n')

                # Atualiza as estatísticas com base na escolha do posto.
                numero_de_vezes_posto_1_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_1 += litragem

            # Verifica se o preço da gasolina no posto 2 é menor que o preço no posto 1 e igual ao preço no posto 3.
            elif preco_gasolina_posto2 < preco_gasolina_posto1 == preco_gasolina_posto3:
                menor_gasto = litragem * preco_gasolina_posto2
                media_gasto_1_2 = litragem * preco_gasolina_posto1
                economia = media_gasto_1_2 - menor_gasto

                # Exibe informações sobre o posto mais barato e a economia.
                print(f'O posto {nome_posto2} é o posto com a gasolina mais barata: R${preco_gasolina_posto2:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto2}, você pagará R${menor_gasto}\n'
                      f'Os postos ({nome_posto1}; {nome_posto3}) '
                      f'cobram o mesmo valor por litro de gasolina: R${preco_gasolina_posto1}\n'
                      f'Economizará R${economia} no total em comparação aos postos ({nome_posto1}; {nome_posto3})\n')

                # Atualiza as estatísticas com base na escolha do posto.
                numero_de_vezes_posto_2_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_2 += litragem

            # Verifica se o preço da gasolina no posto 3 é menor que o preço no posto 1 e igual ao preço no posto 2.
            elif preco_gasolina_posto3 < preco_gasolina_posto1 == preco_gasolina_posto2:
                menor_gasto = litragem * preco_gasolina_posto3
                media_gasto_1_2 = litragem * preco_gasolina_posto1
                economia = media_gasto_1_2 - menor_gasto

                # Exibe informações sobre o posto mais barato e a economia.
                print(f'O posto {nome_posto3} é o posto com a gasolina mais barata: R${preco_gasolina_posto3:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto3}, você pagará R${menor_gasto}\n'
                      f'Os postos ({nome_posto1}; {nome_posto2}) '
                      f'cobram o mesmo valor por litro de gasolina: R${preco_gasolina_posto1}\n'
                      f'Economizará R${economia} no total em comparação aos postos ({nome_posto1}; {nome_posto2})\n')

                # Atualiza as estatísticas com base na escolha do posto.
                numero_de_vezes_posto_3_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_3 += litragem

            # Verificando se o preço da gasolina no posto 1 é o mais baixo em relação aos postos 2 e 3.
            elif preco_gasolina_posto1 < preco_gasolina_posto2 < preco_gasolina_posto3:
                menor_gasto = litragem * preco_gasolina_posto1
                medio_gasto = litragem * preco_gasolina_posto2
                maior_gasto = litragem * preco_gasolina_posto3
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 1, 2 e 3, destacando que o posto 1 oferece o preço mais baixo.
                print(f'O posto {nome_posto1} é o posto com a gasolina mais barata: R${preco_gasolina_posto1:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto2}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto3}\n'
                      f'Demais postos ({nome_posto2}; {nome_posto3}) apresentam os seguintes valores para gasolina '
                      f'por L:\n'
                      f'(R${preco_gasolina_posto2}; R${preco_gasolina_posto3} respectivamente.)')

                # Incrementando o contador para o posto 1 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_1_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_1 += litragem

            # Verificando se o preço da gasolina no posto 1 é o mais baixo em relação aos postos 3 e 2.
            elif preco_gasolina_posto1 < preco_gasolina_posto3 < preco_gasolina_posto2:
                menor_gasto = litragem * preco_gasolina_posto1
                medio_gasto = litragem * preco_gasolina_posto3
                maior_gasto = litragem * preco_gasolina_posto2
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 1, 3 e 2, destacando que o posto 1 oferece o preço mais baixo.
                print(f'O posto {nome_posto1} é o posto com a gasolina mais barata: R${preco_gasolina_posto1:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto3}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto2}\n'
                      f'Demais postos ({nome_posto3}; {nome_posto2}) apresentam os seguintes valores para gasolina '
                      f'por L:\n'
                      f'(R${preco_gasolina_posto3}; R${preco_gasolina_posto2} respectivamente.)')

                # Incrementando o contador para o posto 1 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_1_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_1 += litragem

            # Verificando se o preço da gasolina no posto 2 é o mais baixo em relação aos postos 1 e 3.
            elif preco_gasolina_posto2 < preco_gasolina_posto1 < preco_gasolina_posto3:
                menor_gasto = litragem * preco_gasolina_posto2
                medio_gasto = litragem * preco_gasolina_posto1
                maior_gasto = litragem * preco_gasolina_posto3
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 2, 1 e 3, destacando que o posto 2 oferece o preço mais baixo.
                print(f'O posto {nome_posto2} é o posto com a gasolina mais barata: R${preco_gasolina_posto2:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto1}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto3}\n'
                      f'Demais postos ({nome_posto1}; {nome_posto3}) apresentam os seguintes valores para gasolina '
                      f'por L:\n'
                      f'(R${preco_gasolina_posto1}; R${preco_gasolina_posto3} respectivamente.)')

                # Incrementando o contador para o posto 2 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_2_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_2 += litragem

            # Verificando se o preço da gasolina no posto 2 é o mais baixo em relação aos postos 3 e 1.
            elif preco_gasolina_posto2 < preco_gasolina_posto3 < preco_gasolina_posto1:
                menor_gasto = litragem * preco_gasolina_posto2
                medio_gasto = litragem * preco_gasolina_posto3
                maior_gasto = litragem * preco_gasolina_posto1
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 2, 3 e 1, destacando que o posto 2 oferece o preço mais baixo.
                print(f'O posto {nome_posto2} é o posto com a gasolina mais barata: R${preco_gasolina_posto2:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto3}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto1}\n'
                      f'Demais postos ({nome_posto3}; {nome_posto1}) apresentam os seguintes valores para gasolina '
                      f'por L:\n'
                      f'(R${preco_gasolina_posto3}; R${preco_gasolina_posto1} respectivamente.)')

                # Incrementando o contador para o posto 2 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_2_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_2 += litragem

            # Verificando se o preço da gasolina no posto 3 é o mais baixo em relação aos postos 1 e 2.
            elif preco_gasolina_posto3 < preco_gasolina_posto1 < preco_gasolina_posto2:
                menor_gasto = litragem * preco_gasolina_posto3
                medio_gasto = litragem * preco_gasolina_posto1
                maior_gasto = litragem * preco_gasolina_posto2
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 3, 1 e 2, destacando que o posto 3 oferece o preço mais baixo.
                print(f'O posto {nome_posto3} é o posto com a gasolina mais barata: R${preco_gasolina_posto3:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto1}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto2}\n'
                      f'Demais postos ({nome_posto1}; {nome_posto2}) apresentam os seguintes valores para gasolina '
                      f'por L:\n'
                      f'(R${preco_gasolina_posto1}; R${preco_gasolina_posto2} respectivamente.)')

                # Incrementando o contador para o posto 3 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_3_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_3 += litragem

            # Se nenhum dos casos anteriores se aplicar, significa que o posto 3 possui a gasolina mais barata.
            else:
                menor_gasto = litragem * preco_gasolina_posto3
                medio_gasto = litragem * preco_gasolina_posto2
                maior_gasto = litragem * preco_gasolina_posto1
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 3, 2 e 1, destacando que o posto 3 oferece o preço mais baixo.
                print(f'O posto {nome_posto3} é o posto com a gasolina mais barata: R${preco_gasolina_posto3:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto2}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto1}\n'
                      f'Demais postos ({nome_posto2}; {nome_posto1}) apresentam os seguintes valores para gasolina '
                      f'por L:\n'
                      f'(R${preco_gasolina_posto2}; R${preco_gasolina_posto1} respectivamente.)')

                # Incrementando o contador para o posto 3 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_3_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_3 += litragem

        # Verifica se o tipo de combustível escolhido pelo usuário é 'Etanol'.
        if tipo_de_combustivel == 'Etanol':
            # Verificando se todos os postos têm o mesmo preço de etanol.
            if preco_etanol_posto1 == preco_etanol_posto2 == preco_etanol_posto3:
                # Solicita ao usuário que escolha um posto se todos têm o mesmo preço.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por L de etanol: R${preco_etanol_posto1}\n'
                                      f'Neste caso, devo perguntar qual posto será a sua escolha para abastecer?\n'
                                      f'1 - Posto {nome_posto1}.\n'
                                      f'2 - Posto {nome_posto2}.\n'
                                      f'3 - Posto {nome_posto3}.\n'
                                      f'Digite sua escolha: ')

                # Valida a escolha do usuário para garantir que seja um número entre 1 e 3.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 4):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2; 3] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_1_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_1 += litragem
                elif escolha_posto == 2:
                    numero_de_vezes_posto_2_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_2 += litragem
                else:
                    numero_de_vezes_posto_3_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_3 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço do etanol no posto 1 é igual ao preço do etanol no posto 2 e menor que no posto 3.
            elif preco_etanol_posto1 == preco_etanol_posto2 < preco_etanol_posto3:
                # Solicita ao usuário que escolha entre os postos 1 e 2, já que eles têm o preço mais baixo.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por L de etanol: R${preco_etanol_posto1}\n'
                                      f'Neste caso, devo perguntar qual posto será a sua escolha para abastecer?\n'
                                      f'1 - Posto {nome_posto1}.\n'
                                      f'2 - Posto {nome_posto2}.\n'
                                      f'Digite sua escolha: ')

                # Valida a escolha do usuário para garantir que seja um número entre 1 e 2.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 3):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_1_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_1 += litragem
                else:
                    numero_de_vezes_posto_2_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_2 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço do gasolina no posto 1 é igual ao preço do etanol no posto 3 e menor que no posto 2.
            elif preco_etanol_posto1 == preco_etanol_posto3 < preco_etanol_posto2:
                # Solicita ao usuário que escolha entre os postos 1 e 3, já que eles têm o preço mais baixo.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por L de etanol: R${preco_etanol_posto1}\n'
                                      f'Neste caso, devo perguntar qual posto será a sua escolha para abastecer?\n'
                                      f'1 - Posto {nome_posto1}.\n'
                                      f'2 - Posto {nome_posto3}.\n'
                                      f'Digite sua escolha: ')
                # Valida a escolha do usuário para garantir que seja um número entre 1 e 2.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 3):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2] ')
                escolha_posto = int(escolha_posto)
                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_1_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_1 += litragem
                else:
                    numero_de_vezes_posto_3_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_3 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço do etanol no posto 2 é igual ao preço do etanol no posto 3 e menor que no posto 1.
            elif preco_etanol_posto2 == preco_etanol_posto3 < preco_etanol_posto1:
                # Solicita ao usuário que escolha entre os postos 2 e 3, já que eles têm o preço mais baixo.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por L de etanol: R${preco_etanol_posto1}\n'
                                      f'Neste caso, devo perguntar qual posto será a sua escolha para abastecer?\n'
                                      f'1 - Posto {nome_posto2}.\n'
                                      f'2 - Posto {nome_posto3}.\n'
                                      f'Digite sua escolha: ')

                # Valida a escolha do usuário para garantir que seja um número entre 1 e 2.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 3):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_2_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_2 += litragem
                else:
                    numero_de_vezes_posto_3_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_3 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço da gasolina no posto 1 é menor que o preço no posto 2 e igual ao preço no posto 3.
            elif preco_etanol_posto1 < preco_etanol_posto2 == preco_etanol_posto3:
                menor_gasto = litragem * preco_etanol_posto1
                media_gasto_1_2 = litragem * preco_etanol_posto2
                economia = media_gasto_1_2 - menor_gasto

                # Exibe informações sobre o posto mais barato e a economia.
                print(f'O posto {nome_posto1} é o posto com o etanol mais barato: R${preco_etanol_posto1:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${menor_gasto}\n'
                      f'Os postos ({nome_posto2}; {nome_posto3}) '
                      f'cobram o mesmo valor por L de etanol: R${preco_etanol_posto2}\n'
                      f'Economizará R${economia} no total em comparação aos postos ({nome_posto2}; {nome_posto3})\n')

                # Atualiza as estatísticas com base na escolha do posto.
                numero_de_vezes_posto_1_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_1 += litragem

            # Verifica se o preço do etanol no posto 2 é menor que o preço no posto 1 e igual ao preço no posto 3.
            elif preco_etanol_posto2 < preco_etanol_posto1 == preco_etanol_posto3:
                menor_gasto = litragem * preco_etanol_posto2
                media_gasto_1_2 = litragem * preco_etanol_posto1
                economia = media_gasto_1_2 - menor_gasto

                # Exibe informações sobre o posto mais barato e a economia.
                print(f'O posto {nome_posto2} é o posto com o etanol mais barato: R${preco_etanol_posto2:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${menor_gasto}\n'
                      f'Os postos ({nome_posto1}; {nome_posto3}) '
                      f'cobram o mesmo valor por L de etanol: R${preco_etanol_posto1}\n'
                      f'Economizará R${economia} no total em comparação aos postos ({nome_posto1}; {nome_posto3})\n')

                # Atualiza as estatísticas com base na escolha do posto.
                numero_de_vezes_posto_2_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_2 += litragem

            # Verifica se o preço do etanol no posto 3 é menor que o preço no posto 1 e igual ao preço no posto 2.
            elif preco_etanol_posto3 < preco_etanol_posto1 == preco_etanol_posto2:
                menor_gasto = litragem * preco_etanol_posto3
                media_gasto_1_2 = litragem * preco_etanol_posto1
                economia = media_gasto_1_2 - menor_gasto

                # Exibe informações sobre o posto mais barato e a economia.
                print(f'O posto {nome_posto3} é o posto com o etanol mais barato: R${preco_etanol_posto3:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${menor_gasto}\n'
                      f'Os postos ({nome_posto1}; {nome_posto2}) '
                      f'cobram o mesmo valor por L de etanol: R${preco_etanol_posto1}\n'
                      f'Economizará R${economia} no total em comparação aos postos ({nome_posto1}; {nome_posto2})\n')

                # Atualiza as estatísticas com base na escolha do posto.
                numero_de_vezes_posto_3_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_3 += litragem

            # Verificando se o preço do etanol no posto 1 é o mais baixo em relação aos postos 2 e 3.
            elif preco_etanol_posto1 < preco_etanol_posto2 < preco_etanol_posto3:
                menor_gasto = litragem * preco_etanol_posto1
                medio_gasto = litragem * preco_etanol_posto3
                maior_gasto = litragem * preco_etanol_posto2
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 1, 2 e 3, destacando que o posto 1 oferece o preço mais baixo.
                print(f'O posto {nome_posto1} é o posto com o etanol mais barato: R${preco_etanol_posto1:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto2}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto3}\n'
                      f'Os demais postos ({nome_posto2}; {nome_posto3}) apresentam o seguinte valores para etanol:\n'
                      f'(R${preco_etanol_posto2}; R${preco_etanol_posto3} respectivamente.)')

                # Incrementando o contador para o posto 1 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_1_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_1 += litragem

            # Verificando se o preço do etanol no posto 1 é o mais baixo em relação aos postos 3 e 2.
            elif preco_etanol_posto1 < preco_etanol_posto3 < preco_etanol_posto2:
                menor_gasto = litragem * preco_etanol_posto1
                medio_gasto = litragem * preco_etanol_posto3
                maior_gasto = litragem * preco_etanol_posto2
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 1, 3 e 2, destacando que o posto 1 oferece o preço mais baixo.
                print(f'O posto {nome_posto1} é o posto com o etanol mais barato: R${preco_etanol_posto1:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto3}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto2}\n'
                      f'Os demais postos ({nome_posto3}; {nome_posto2}) apresentam o seguinte valores para etanol:\n'
                      f'(R${preco_etanol_posto3}; R${preco_etanol_posto2} respectivamente.)')

                # Incrementando o contador para o posto 1 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_1_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_1 += litragem

            # Verificando se o preço do etanol no posto 2 é o mais baixo em relação aos postos 1 e 3.
            elif preco_etanol_posto2 < preco_etanol_posto1 < preco_etanol_posto3:
                menor_gasto = litragem * preco_etanol_posto2
                medio_gasto = litragem * preco_etanol_posto1
                maior_gasto = litragem * preco_etanol_posto3
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 2, 1 e 3, destacando que o posto 2 oferece o preço mais baixo.
                print(f'O posto {nome_posto2} é o posto com o etanol mais barato: R${preco_etanol_posto2:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto1}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto3}\n'
                      f'Os demais postos ({nome_posto1}; {nome_posto3}) apresentam o seguinte valores para etanol:\n'
                      f'(R${preco_etanol_posto1}; R${preco_etanol_posto3} respectivamente.)')

                # Incrementando o contador para o posto 2 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_2_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_2 += litragem

            # Verificando se o preço do no posto 2 é o mais baixo em relação aos postos 3 e 1.
            elif preco_etanol_posto2 < preco_etanol_posto3 < preco_etanol_posto1:
                menor_gasto = litragem * preco_etanol_posto2
                medio_gasto = litragem * preco_etanol_posto3
                maior_gasto = litragem * preco_etanol_posto1
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 2, 3 e 1, destacando que o posto 2 oferece o preço mais baixo.
                print(f'O posto {nome_posto2} é o posto com o etanol mais barato: R${preco_etanol_posto2:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto3}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto1}\n'
                      f'Os demais postos ({nome_posto3}; {nome_posto1}) apresentam o seguinte valores para etanol:\n'
                      f'(R${preco_etanol_posto3}; R${preco_etanol_posto1} respectivamente.)')

                # Incrementando o contador para o posto 2 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_2_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_2 += litragem

            # Verificando se o preço do etanol no posto 3 é o mais baixo em relação aos postos 1 e 2.
            elif preco_etanol_posto3 < preco_etanol_posto1 < preco_etanol_posto2:
                menor_gasto = litragem * preco_etanol_posto3
                medio_gasto = litragem * preco_etanol_posto1
                maior_gasto = litragem * preco_etanol_posto2
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 3, 1 e 2, destacando que o posto 3 oferece o preço mais baixo.
                print(f'O posto {nome_posto2} é o posto com o etanol mais barato: R${preco_etanol_posto3:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto1}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto2}\n'
                      f'Os demais postos ({nome_posto1}; {nome_posto2}) apresentam o seguinte valores para etanol:\n'
                      f'(R${preco_etanol_posto1}; R${preco_etanol_posto2} respectivamente.)')

                # Incrementando o contador para o posto 3 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_3_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_3 += litragem

            # Se nenhum dos casos anteriores se aplicar, significa que o posto 3 possui o etanol mais barato.
            else:
                menor_gasto = litragem * preco_etanol_posto3
                medio_gasto = litragem * preco_etanol_posto2
                maior_gasto = litragem * preco_etanol_posto1
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 3, 2 e 1, destacando que o posto 3 oferece o preço mais baixo.
                print(f'O posto {nome_posto2} é o posto com o etanol mais barato: R${preco_etanol_posto3:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto2}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto1}\n'
                      f'Os demais postos ({nome_posto2}; {nome_posto1}) apresentam o seguinte valores para etanol:\n'
                      f'(R${preco_etanol_posto2}; R${preco_etanol_posto1} respectivamente.)')

                # Incrementando o contador para o posto 3 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_3_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_3 += litragem

        # Verifica se o tipo de combustível escolhido pelo usuário é 'Diesel'.
        if tipo_de_combustivel == 'Diesel':
            # Verifica se todos os postos têm o mesmo preço para o diesel.
            if preco_diesel_posto1 == preco_diesel_posto2 == preco_diesel_posto3:
                # Solicita ao usuário que escolha um posto se todos têm o mesmo preço.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por L de diesel :\n R${preco_diesel_posto1}\n'
                                      f'Neste caso devo perguntar qual posto será o de sua escolha para abastecer?\n'
                                      f'1 - Posto {nome_posto1}.\n'
                                      f'2 - Posto {nome_posto2}.\n'
                                      f'3 - Posto {nome_posto3}.\n'
                                      f'Digite sua escolha: ')

                # Valida a escolha do usuário para garantir que seja um número entre 1 e 3.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 4):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2; 3] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_1_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_1 += litragem
                elif escolha_posto == 2:
                    numero_de_vezes_posto_2_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_2 += litragem
                else:
                    numero_de_vezes_posto_3_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_3 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço da gasolina no posto 1 é igual ao preço do diesel no posto 2 e menor que no posto 3.
            elif preco_diesel_posto1 == preco_diesel_posto2 < preco_diesel_posto3:
                # Solicita ao usuário que escolha entre os postos 1 e 2, já que eles têm o preço mais baixo.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por L de diesel :\n R${preco_diesel_posto1}\n'
                                      f'Neste caso devo perguntar qual posto será o de sua escolha para abastecer?\n'
                                      f'1 - Posto {nome_posto1}.\n'
                                      f'2 - Posto {nome_posto2}.\n'
                                      f'Digite sua escolha: ')

                # Valida a escolha do usuário para garantir que seja um número entre 1 e 2.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 3):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_1_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_1 += litragem
                else:
                    numero_de_vezes_posto_2_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_2 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço do diesel no posto 1 é igual ao preço do diesel no posto 3 e menor que no posto 2.
            elif preco_diesel_posto1 == preco_diesel_posto3 < preco_diesel_posto2:
                # Solicita ao usuário que escolha entre os postos 1 e 3, já que eles têm o preço mais baixo.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por L de diesel :\n R${preco_diesel_posto1}\n'
                                      f'Neste caso devo perguntar qual posto será o de sua escolha para abastecer?\n'
                                      f'1 - Posto {nome_posto1}.\n'
                                      f'2 - Posto {nome_posto3}.\n'
                                      f'Digite sua escolha: ')

                # Valida a escolha do usuário para garantir que seja um número entre 1 e 2.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 3):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_1_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_1 += litragem
                else:
                    numero_de_vezes_posto_3_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_3 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço do diesel no posto 2 é igual ao preço do diesel no posto 3 e menor que no posto 1.
            elif preco_diesel_posto2 == preco_diesel_posto3 < preco_diesel_posto1:
                # Solicita ao usuário que escolha entre os postos 2 e 3, já que eles têm o preço mais baixo.
                escolha_posto = input(f'Os postos ({nome_posto1}; {nome_posto2}; {nome_posto3}) '
                                      f'cobram o mesmo valor por L de diesel :\n R${preco_diesel_posto1}\n'
                                      f'Neste caso devo perguntar qual posto será o de sua escolha para abastecer?\n'
                                      f'1 - Posto {nome_posto2}.\n'
                                      f'2 - Posto {nome_posto3}.\n'
                                      f'Digite sua escolha: ')
                # Valida a escolha do usuário para garantir que seja um número entre 1 e 2.
                while not escolha_posto.isdigit() or not (0 < int(escolha_posto) < 3):
                    print('Esse tipo de resposta não é válida... Tente novamente.')
                    escolha_posto = input('Digite sua escolha: [1; 2] ')
                escolha_posto = int(escolha_posto)

                # Atualiza as estatísticas com base na escolha do posto.
                if escolha_posto == 1:
                    numero_de_vezes_posto_2_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_2 += litragem
                else:
                    numero_de_vezes_posto_3_teve_menor_preco += 1
                    quantidade_de_litros_abastecidos_no_posto_3 += litragem

                # Exibe uma mensagem para confirmar o registro da escolha do posto.
                print('Ok. Salvamos a informação da sua preferência.')

            # Verifica se o preço do diesel no posto 1 é menor que o preço no posto 2 e igual ao preço no posto 3.
            elif preco_diesel_posto1 < preco_diesel_posto2 == preco_diesel_posto3:
                menor_gasto = litragem * preco_diesel_posto1
                media_gasto_1_2 = litragem * preco_diesel_posto2
                economia = media_gasto_1_2 - menor_gasto

                # Exibe informações sobre o posto mais barato e a economia.
                print(f'O posto {nome_posto1} é o posto com o diesel mais barata: R${preco_diesel_posto1:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${menor_gasto}\n'
                      f'Os postos ({nome_posto2}; {nome_posto3}) '
                      f'cobram o mesmo valor por L de diesel :\n R${preco_gasolina_posto2}\n'
                      f'Economizará R${economia} no total em comparação aos postos ({nome_posto2}; {nome_posto3})\n')

                # Atualiza as estatísticas com base na escolha do posto.
                numero_de_vezes_posto_1_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_1 += litragem

            # Verifica se o preço do diesel no posto 2 é menor que o preço no posto 1 e igual ao preço no posto 3.
            elif preco_diesel_posto2 < preco_diesel_posto1 == preco_diesel_posto3:
                menor_gasto = litragem * preco_diesel_posto2
                media_gasto_1_2 = litragem * preco_diesel_posto1
                economia = media_gasto_1_2 - menor_gasto

                # Exibe informações sobre o posto mais barato e a economia.
                print(f'O posto {nome_posto2} é o posto com o diesel mais barata: R${preco_diesel_posto2:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${menor_gasto}\n'
                      f'Os postos ({nome_posto1}; {nome_posto3}) '
                      f'cobram o mesmo valor por L de diesel :\n R${preco_diesel_posto1}\n'
                      f'Economizará R${economia} no total em comparação aos postos ({nome_posto1}; {nome_posto3})\n')

                # Atualiza as estatísticas com base na escolha do posto.
                numero_de_vezes_posto_2_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_2 += litragem

            # Verifica se o preço do diesel no posto 3 é menor que o preço no posto 1 e igual ao preço no posto 2.
            elif preco_diesel_posto3 < preco_diesel_posto1 == preco_diesel_posto2:
                menor_gasto = litragem * preco_diesel_posto3
                media_gasto_1_2 = litragem * preco_diesel_posto1
                economia = media_gasto_1_2 - menor_gasto

                # Exibe informações sobre o posto mais barato e a economia.
                print(f'O posto {nome_posto3} é o posto com o diesel mais barata: R${preco_diesel_posto3:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${menor_gasto}\n'
                      f'Os postos ({nome_posto1}; {nome_posto2}) '
                      f'cobram o mesmo valor por L de diesel :\n R${preco_diesel_posto1}\n'
                      f'Economizará R${economia} no total em comparação aos postos ({nome_posto1}; {nome_posto2})\n')

                # Atualiza as estatísticas com base na escolha do posto.
                numero_de_vezes_posto_3_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_3 += litragem

            # Verificando se o preço do diesel no posto 1 é o mais baixo em relação aos postos 2 e 3.
            elif preco_diesel_posto1 < preco_diesel_posto2 < preco_diesel_posto3:
                menor_gasto = litragem * preco_diesel_posto1
                medio_gasto = litragem * preco_diesel_posto2
                maior_gasto = litragem * preco_diesel_posto3
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 1, 2 e 3, destacando que o posto 1 oferece o preço mais baixo.
                print(f'O posto {nome_posto1} é o posto com o diesel mais barato: R${preco_diesel_posto1:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto2}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto3}\n'
                      f'Os demais postos ({nome_posto2}; {nome_posto3}) apresentam o seguinte valores para diesel:\n'
                      f'(R${preco_diesel_posto2}; R${preco_diesel_posto3} respectivamente.)')

                # Incrementando o contador para o posto 1 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_1_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_1 += litragem

            # Verificando se o preço do diesel no posto 1 é o mais baixo em relação aos postos 3 e 2.
            elif preco_diesel_posto1 < preco_diesel_posto3 < preco_diesel_posto2:
                menor_gasto = litragem * preco_diesel_posto1
                medio_gasto = litragem * preco_diesel_posto3
                maior_gasto = litragem * preco_diesel_posto2
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 1, 3 e 2, destacando que o posto 1 oferece o preço mais baixo.
                print(f'O posto {nome_posto1} é o posto com o diesel mais barato: R${preco_diesel_posto1:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto3}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto2}\n'
                      f'Os demais postos ({nome_posto3}; {nome_posto2}) apresentam o seguinte valores para diesel:\n'
                      f'(R${preco_diesel_posto3}; R${preco_diesel_posto2} respectivamente.)')

                # Incrementando o contador para o posto 1 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_1_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_1 += litragem

            # Verificando se o preço do diesel no posto 2 é o mais baixo em relação aos postos 1 e 3.
            elif preco_diesel_posto2 < preco_diesel_posto1 < preco_diesel_posto3:
                menor_gasto = litragem * preco_diesel_posto2
                medio_gasto = litragem * preco_diesel_posto1
                maior_gasto = litragem * preco_diesel_posto3
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 2, 1 e 3, destacando que o posto 2 oferece o preço mais baixo.
                print(f'O posto {nome_posto2} é o posto com o diesel mais barato: R${preco_diesel_posto2:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto1}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto3}\n'
                      f'Os demais postos ({nome_posto1}; {nome_posto3}) apresentam o seguinte valores para diesel:\n'
                      f'(R${preco_diesel_posto1}; R${preco_diesel_posto3} respectivamente.)')

                # Incrementando o contador para o posto 2 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_2_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_2 += litragem

            # Verificando se o preço do diesel no posto 2 é o mais baixo em relação aos postos 3 e 1.
            elif preco_diesel_posto2 < preco_diesel_posto3 < preco_diesel_posto1:
                menor_gasto = litragem * preco_diesel_posto2
                medio_gasto = litragem * preco_diesel_posto3
                maior_gasto = litragem * preco_diesel_posto1
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 2, 3 e 1, destacando que o posto 2 oferece o preço mais baixo.
                print(f'O posto {nome_posto2} é o posto com o diesel mais barato: R${preco_diesel_posto2:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto3}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto1}\n'
                      f'Os demais postos ({nome_posto3}; {nome_posto1}) apresentam o seguinte valores para diesel:\n'
                      f'(R${preco_diesel_posto3}; R${preco_diesel_posto1} respectivamente.)')

                # Incrementando o contador para o posto 2 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_2_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_2 += litragem

            # Verificando se o preço do diesel no posto 3 é o mais baixo em relação aos postos 1 e 2.
            elif preco_diesel_posto3 < preco_diesel_posto1 < preco_diesel_posto2:
                menor_gasto = litragem * preco_diesel_posto3
                medio_gasto = litragem * preco_diesel_posto1
                maior_gasto = litragem * preco_diesel_posto2
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 3, 1 e 2, destacando que o posto 3 oferece o preço mais baixo.
                print(f'O posto {nome_posto3} é o posto com o diesel mais barato: R${preco_diesel_posto3:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto1}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto2}\n'
                      f'Os demais postos ({nome_posto1}; {nome_posto2}) apresentam o seguinte valores para diesel:\n'
                      f'(R${preco_diesel_posto1}; R${preco_diesel_posto2} respectivamente.)')

                # Incrementando o contador para o posto 3 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_3_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_3 += litragem

            # Se nenhum dos casos anteriores se aplicar, significa que o posto 3 possui o diesel mais barato.
            else:
                menor_gasto = litragem * preco_diesel_posto3
                medio_gasto = litragem * preco_diesel_posto2
                maior_gasto = litragem * preco_diesel_posto1
                economia1 = medio_gasto - menor_gasto
                economia2 = maior_gasto - menor_gasto

                # Exibindo informações sobre o posto 3, 2 e 1, destacando que o posto 3 oferece o preço mais baixo.
                print(f'O posto {nome_posto3} é o posto com o diesel mais barato: R${preco_diesel_posto3:.2f}\n'
                      f'Comprando {litragem}L no posto {nome_posto3} você pagará R${menor_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto2} você pagará R${medio_gasto}\n'
                      f'Comprando {litragem}L no posto {nome_posto1} você pagará R${maior_gasto}\n'
                      f'Economizará R${economia1} no total em comparação ao posto {nome_posto2}\n'
                      f'Economizará R${economia2} no total em comparação ao posto {nome_posto1}\n'
                      f'Os demais postos ({nome_posto2}; {nome_posto1}) apresentam o seguinte valores para diesel:\n'
                      f'(R${preco_diesel_posto2}; R${preco_diesel_posto1} respectivamente.)')

                # Incrementando o contador para o posto 3 ter o menor preço e a quantidade de litros abastecidos.
                numero_de_vezes_posto_3_teve_menor_preco += 1
                quantidade_de_litros_abastecidos_no_posto_3 += litragem

    # Se a escolha for '2', Lista todas as informções dos postos cadastrados.
    if menu == 2:
        # Imprimindo os preços por litro de gasolina, etanol e diesel para os três postos.
        print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
              f'Preços por L de GASOLINA:\n'
              f'Posto {nome_posto1}    R${preco_gasolina_posto1:.2f}\n'
              f'Posto {nome_posto2}    R${preco_gasolina_posto2:.2f}\n'
              f'Posto {nome_posto3}    R${preco_gasolina_posto3:.2f}\n'
              f'Preços por L de ETANOL:\n'
              f'Posto {nome_posto1}    R${preco_etanol_posto1:.2f}\n'
              f'Posto {nome_posto2}    R${preco_etanol_posto2:.2f}\n'
              f'Posto {nome_posto3}    R${preco_etanol_posto3:.2f}\n'
              f'Preços por L de DIESEL:\n'
              f'Posto {nome_posto1}    R${preco_diesel_posto1:.2f}\n'
              f'Posto {nome_posto2}    R${preco_diesel_posto2:.2f}\n'
              f'Posto {nome_posto3}    R${preco_diesel_posto3:.2f}')

    # Imprimindo estatísticas gerais.
    print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
          f'Foram feitas {quantidade_de_consultas} consultas no sistema.\n'
          f'O posto {nome_posto1} foi apontado como o mais barato {numero_de_vezes_posto_1_teve_menor_preco} vezes.\n'
          f'O posto {nome_posto2} foi apontado como o mais barato {numero_de_vezes_posto_2_teve_menor_preco} vezes.\n'
          f'O posto {nome_posto3} foi apontado como o mais barato {numero_de_vezes_posto_3_teve_menor_preco} vezes.\n')

    # Calculando e imprimindo a média de litros abastecidos no posto 1, se aplicável.
    if numero_de_vezes_posto_1_teve_menor_preco > 0:
        media_litros_posto1 = quantidade_de_litros_abastecidos_no_posto_1 / numero_de_vezes_posto_1_teve_menor_preco
        print(f'A média de litros consultados no posto {nome_posto1} é: {media_litros_posto1}L')
    else:
        print(f'Não é possível calcular a média, pois o posto {nome_posto1} não foi apontado como o mais barato.')

    # Calculando e imprimindo a média de litros abastecidos no posto 2, se aplicável.
    if numero_de_vezes_posto_2_teve_menor_preco > 0:
        media_litros_posto2 = quantidade_de_litros_abastecidos_no_posto_2 / numero_de_vezes_posto_2_teve_menor_preco
        print(f'A média de litros consultados no posto {nome_posto2} é: {media_litros_posto2}L')
    else:
        print(f'Não é possível calcular a média, pois o posto {nome_posto2} não foi apontado como o mais barato.')

    # Calculando e imprimindo a média de litros abastecidos no posto 3, se aplicável.
    if numero_de_vezes_posto_3_teve_menor_preco > 0:
        media_litros_posto3 = quantidade_de_litros_abastecidos_no_posto_3 / numero_de_vezes_posto_3_teve_menor_preco
        print(f'A média de litros consultados no posto {nome_posto3} é: {media_litros_posto3}L')
    else:
        print(f'Não é possível calcular a média, pois o posto {nome_posto3} não foi apontado como o mais barato.')

posto_gasolina_mais_cara = ''  # Nome do posto com a gasolina mais cara
posto_gasolina_mais_barata = ''  # Nome do posto com a gasolina mais barata
posto_etanol_mais_caro = ''  # Nome do posto com o etanol mais caro
posto_etanol_mais_barato = ''  # Nome do posto com o etanol mais barato
posto_diesel_mais_caro = ''  # Nome do posto com o diesel mais caro
posto_diesel_mais_barato = ''  # Nome do posto com o diesel mais barato

gasolina_mais_cara = 0  # Preço da gasolina mais cara
gasolina_mais_barata = 0  # Preço da gasolina mais barata
etanol_mais_caro = 0  # Preço do etanol mais caro
etanol_mais_barato = 0  # Preço do etanol mais barato
diesel_mais_caro = 0  # Preço do diesel mais caro
diesel_mais_barato = 0  # Preço do diesel mais barato

# Bloco que verifica qual posto será classificado como o mais caro e o mais barato por L de gasolina.
if preco_gasolina_posto1 == preco_gasolina_posto2 == preco_gasolina_posto3:
    posto_gasolina_mais_cara = 'Todos os postos apresentam como os mais caros;'
    posto_gasolina_mais_barata = 'Todos os postos apresentam como os mais baratos;'
    gasolina_mais_cara = preco_gasolina_posto1
    gasolina_mais_barata = preco_gasolina_posto1
elif preco_gasolina_posto1 < preco_gasolina_posto2 == preco_gasolina_posto3:
    posto_gasolina_mais_cara = f'Os postos ({nome_posto2};{nome_posto3}) são os mais caros ambos com o mesmo preço;'
    posto_gasolina_mais_barata = nome_posto1
    gasolina_mais_cara = preco_gasolina_posto2
    gasolina_mais_barata = preco_gasolina_posto1
elif preco_gasolina_posto1 > preco_gasolina_posto2 == preco_gasolina_posto3:
    posto_gasolina_mais_cara = nome_posto1
    posto_gasolina_mais_barata = f'Os postos ({nome_posto2};{nome_posto3}) são os mais baratos ambos com o mesmo preço;'
    gasolina_mais_cara = preco_gasolina_posto1
    gasolina_mais_barata = preco_gasolina_posto2
elif preco_gasolina_posto2 < preco_gasolina_posto1 == preco_gasolina_posto3:
    posto_gasolina_mais_cara = f'Os postos ({nome_posto1};{nome_posto3}) são os mais caros ambos com o mesmo preço;'
    posto_gasolina_mais_barata = nome_posto2
    gasolina_mais_cara = preco_gasolina_posto1
    gasolina_mais_barata = preco_gasolina_posto2
elif preco_gasolina_posto2 > preco_gasolina_posto3 == preco_gasolina_posto1:
    posto_gasolina_mais_cara = nome_posto2
    posto_gasolina_mais_barata = f'Os postos ({nome_posto1};{nome_posto3}) são os mais baratos ambos com o mesmo preço;'
    gasolina_mais_cara = preco_gasolina_posto2
    gasolina_mais_barata = preco_gasolina_posto1
elif preco_gasolina_posto3 < preco_gasolina_posto1 == preco_gasolina_posto2:
    posto_gasolina_mais_cara = f'Os postos ({nome_posto1}; {nome_posto2}) são os mais caros ambos com o mesmo preço;'
    posto_gasolina_mais_barata = nome_posto3
    gasolina_mais_cara = preco_gasolina_posto1
    gasolina_mais_barata = preco_gasolina_posto3
elif preco_gasolina_posto3 > preco_gasolina_posto2 == preco_gasolina_posto1:
    posto_gasolina_mais_cara = nome_posto3
    posto_gasolina_mais_barata = f'Os postos ({nome_posto1};{nome_posto2}) são os mais baratos ambos com o mesmo preço;'
    gasolina_mais_cara = preco_gasolina_posto3
    gasolina_mais_barata = preco_gasolina_posto1
elif preco_gasolina_posto1 < preco_gasolina_posto2 < preco_gasolina_posto3:
    posto_gasolina_mais_cara = nome_posto3
    posto_gasolina_mais_barata = nome_posto1
    gasolina_mais_cara = preco_gasolina_posto3
    gasolina_mais_barata = preco_gasolina_posto1
elif preco_gasolina_posto1 < preco_gasolina_posto3 < preco_gasolina_posto2:
    posto_gasolina_mais_cara = nome_posto2
    posto_gasolina_mais_barata = nome_posto1
    gasolina_mais_cara = preco_gasolina_posto2
    gasolina_mais_barata = preco_gasolina_posto1
elif preco_gasolina_posto2 < preco_gasolina_posto1 < preco_gasolina_posto3:
    posto_gasolina_mais_cara = nome_posto3
    posto_gasolina_mais_barata = nome_posto2
    gasolina_mais_cara = preco_gasolina_posto3
    gasolina_mais_barata = preco_gasolina_posto2
elif preco_gasolina_posto2 < preco_gasolina_posto3 < preco_gasolina_posto1:
    posto_gasolina_mais_cara = nome_posto1
    posto_gasolina_mais_barata = nome_posto2
    gasolina_mais_cara = preco_gasolina_posto1
    gasolina_mais_barata = preco_gasolina_posto2
elif preco_gasolina_posto3 < preco_gasolina_posto1 < preco_gasolina_posto2:
    posto_gasolina_mais_cara = nome_posto2
    posto_gasolina_mais_barata = nome_posto3
    gasolina_mais_cara = preco_gasolina_posto2
    gasolina_mais_barata = preco_gasolina_posto3
elif preco_gasolina_posto3 < preco_gasolina_posto2 < preco_gasolina_posto1:
    posto_gasolina_mais_cara = nome_posto1
    posto_gasolina_mais_barata = nome_posto3
    gasolina_mais_cara = preco_gasolina_posto1
    gasolina_mais_barata = preco_gasolina_posto3

# Bloco que verifica qual posto será classificado como o mais caro e o mais barato por L de etanol.
if preco_etanol_posto1 == preco_etanol_posto2 == preco_etanol_posto3:
    posto_etanol_mais_caro = 'Todos os postos apresentam como os mais caros;'
    posto_etanol_mais_barato = 'Todos os postos apresentam como os mais baratos;'
    etanol_mais_caro = preco_etanol_posto1
    etanol_mais_barato = preco_etanol_posto1
elif preco_etanol_posto1 < preco_etanol_posto2 == preco_etanol_posto3:
    posto_etanol_mais_caro = f'Os postos ({nome_posto2};{nome_posto3}) são os mais caros ambos com o mesmo preço;'
    posto_etanol_mais_barato = nome_posto1
    etanol_mais_caro = preco_etanol_posto2
    etanol_mais_barato = preco_etanol_posto1
elif preco_etanol_posto1 > preco_etanol_posto2 == preco_etanol_posto3:
    posto_etanol_mais_caro = nome_posto1
    posto_etanol_mais_barato = f'Os postos ({nome_posto2};{nome_posto3}) são os mais baratos ambos com o mesmo preço;'
    etanol_mais_caro = preco_etanol_posto1
    etanol_mais_barato = preco_etanol_posto2
elif preco_etanol_posto2 < preco_etanol_posto1 == preco_etanol_posto3:
    posto_etanol_mais_caro = f'Os postos ({nome_posto1};{nome_posto3}) são os mais caros ambos com o mesmo preço;'
    posto_etanol_mais_barato = nome_posto2
    etanol_mais_caro = preco_etanol_posto1
    etanol_mais_barato = preco_etanol_posto2
elif preco_etanol_posto2 > preco_etanol_posto3 == preco_etanol_posto1:
    posto_etanol_mais_caro = nome_posto2
    posto_etanol_mais_barato = f'Os postos ({nome_posto1};{nome_posto3}) são os mais baratos ambos com o mesmo preço;'
    etanol_mais_caro = preco_etanol_posto2
    etanol_mais_barato = preco_etanol_posto1
elif preco_etanol_posto3 < preco_etanol_posto1 == preco_etanol_posto2:
    posto_etanol_mais_caro = f'Os postos ({nome_posto1}; {nome_posto2}) são os mais caros ambos com o mesmo preço;'
    posto_etanol_mais_barato = nome_posto3
    etanol_mais_caro = preco_etanol_posto1
    etanol_mais_barato = preco_etanol_posto3
elif preco_etanol_posto3 > preco_etanol_posto2 == preco_etanol_posto1:
    posto_etanol_mais_caro = nome_posto3
    posto_etanol_mais_barato = f'Os postos ({nome_posto1};{nome_posto2}) são os mais baratos ambos com o mesmo preço;'
    etanol_mais_caro = preco_etanol_posto3
    etanol_mais_barato = preco_etanol_posto1
elif preco_etanol_posto1 < preco_etanol_posto2 < preco_etanol_posto3:
    posto_etanol_mais_caro = nome_posto3
    posto_etanol_mais_barato = nome_posto1
    etanol_mais_caro = preco_etanol_posto3
    etanol_mais_barato = preco_etanol_posto1
elif preco_etanol_posto1 < preco_etanol_posto3 < preco_etanol_posto2:
    posto_etanol_mais_caro = nome_posto2
    posto_etanol_mais_barato = nome_posto1
    etanol_mais_caro = preco_etanol_posto2
    etanol_mais_barato = preco_etanol_posto1
elif preco_etanol_posto2 < preco_etanol_posto1 < preco_etanol_posto3:
    posto_etanol_mais_caro = nome_posto3
    posto_etanol_mais_barato = nome_posto2
    etanol_mais_caro = preco_etanol_posto3
    etanol_mais_barato = preco_etanol_posto2
elif preco_etanol_posto2 < preco_etanol_posto3 < preco_etanol_posto1:
    posto_etanol_mais_caro = nome_posto1
    posto_etanol_mais_barato = nome_posto2
    etanol_mais_caro = preco_etanol_posto1
    etanol_mais_barato = preco_etanol_posto2
elif preco_etanol_posto3 < preco_etanol_posto1 < preco_etanol_posto2:
    posto_etanol_mais_caro = nome_posto2
    posto_etanol_mais_barato = nome_posto3
    etanol_mais_caro = preco_etanol_posto2
    etanol_mais_barato = preco_etanol_posto3
elif preco_etanol_posto3 < preco_etanol_posto2 < preco_etanol_posto1:
    posto_etanol_mais_caro = nome_posto1
    posto_etanol_mais_barato = nome_posto3
    etanol_mais_caro = preco_etanol_posto1
    etanol_mais_barato = preco_etanol_posto3

# Bloco que verifica qual posto será classificado como o mais caro e o mais barato por L de diesel.
if preco_diesel_posto1 == preco_diesel_posto2 == preco_diesel_posto3:
    posto_diesel_mais_caro = 'Todos os postos apresentam como os mais caros;'
    posto_diesel_mais_barato = 'Todos os postos apresentam como os mais baratos;'
    diesel_mais_caro = preco_diesel_posto1
    diesel_mais_barato = preco_diesel_posto1
elif preco_diesel_posto1 < preco_diesel_posto2 == preco_diesel_posto3:
    posto_diesel_mais_caro = f'Os postos ({nome_posto2};{nome_posto3}) são os mais caros ambos com o mesmo preço;'
    posto_diesel_mais_barato = nome_posto1
    diesel_mais_caro = preco_diesel_posto2
    diesel_mais_barato = preco_diesel_posto1
elif preco_diesel_posto1 > preco_diesel_posto2 == preco_diesel_posto3:
    posto_diesel_mais_caro = nome_posto1
    posto_diesel_mais_barato = f'Os postos ({nome_posto2};{nome_posto3}) são os mais baratos ambos com o mesmo preço;'
    diesel_mais_caro = preco_diesel_posto1
    diesel_mais_barato = preco_diesel_posto2
elif preco_diesel_posto2 < preco_diesel_posto1 == preco_diesel_posto3:
    posto_diesel_mais_caro = f'Os postos ({nome_posto1};{nome_posto3}) são os mais caros ambos com o mesmo preço;'
    posto_diesel_mais_barato = nome_posto2
    diesel_mais_caro = preco_diesel_posto1
    diesel_mais_barato = preco_diesel_posto2
elif preco_diesel_posto2 > preco_diesel_posto3 == preco_diesel_posto1:
    posto_diesel_mais_caro = nome_posto2
    posto_diesel_mais_barato = f'Os postos ({nome_posto1};{nome_posto3}) são os mais baratos ambos com o mesmo preço;'
    diesel_mais_caro = preco_diesel_posto2
    diesel_mais_barato = preco_diesel_posto1
elif preco_diesel_posto3 < preco_diesel_posto1 == preco_diesel_posto2:
    posto_diesel_mais_caro = f'Os postos ({nome_posto1}; {nome_posto2}) são os mais caros ambos com o mesmo preço;'
    posto_diesel_mais_barato = nome_posto3
    diesel_mais_caro = preco_diesel_posto1
    diesel_mais_barato = preco_diesel_posto3
elif preco_diesel_posto3 > preco_diesel_posto2 == preco_diesel_posto1:
    posto_diesel_mais_caro = nome_posto3
    posto_diesel_mais_barato = f'Os postos ({nome_posto1};{nome_posto2}) são os mais baratos ambos com o mesmo preço;'
    diesel_mais_caro = preco_diesel_posto3
    diesel_mais_barato = preco_diesel_posto1
elif preco_diesel_posto1 < preco_diesel_posto2 < preco_diesel_posto3:
    posto_diesel_mais_caro = nome_posto3
    posto_diesel_mais_barato = nome_posto1
    diesel_mais_caro = preco_diesel_posto3
    diesel_mais_barato = preco_diesel_posto1
elif preco_diesel_posto1 < preco_diesel_posto3 < preco_diesel_posto2:
    posto_diesel_mais_caro = nome_posto2
    posto_diesel_mais_barato = nome_posto1
    diesel_mais_caro = preco_diesel_posto2
    diesel_mais_barato = preco_diesel_posto1
elif preco_diesel_posto2 < preco_diesel_posto1 < preco_diesel_posto3:
    posto_diesel_mais_caro = nome_posto3
    posto_diesel_mais_barato = nome_posto2
    diesel_mais_caro = preco_diesel_posto3
    diesel_mais_barato = preco_diesel_posto2
elif preco_diesel_posto2 < preco_diesel_posto3 < preco_diesel_posto1:
    posto_diesel_mais_caro = nome_posto1
    posto_diesel_mais_barato = nome_posto2
    diesel_mais_caro = preco_diesel_posto1
    diesel_mais_barato = preco_diesel_posto2
elif preco_diesel_posto3 < preco_diesel_posto1 < preco_diesel_posto2:
    posto_diesel_mais_caro = nome_posto2
    posto_diesel_mais_barato = nome_posto3
    diesel_mais_caro = preco_diesel_posto2
    diesel_mais_barato = preco_diesel_posto3
elif preco_diesel_posto3 < preco_diesel_posto2 < preco_diesel_posto1:
    posto_diesel_mais_caro = nome_posto1
    posto_diesel_mais_barato = nome_posto3
    diesel_mais_caro = preco_diesel_posto1
    diesel_mais_barato = preco_diesel_posto3

# Cria uma exibição dos postos com os preços mais caros e mais baratos por litro de gasolina, etanol e diesel.
print(f'-=-=-=-=-=-=-=-=-RALAÇÃO POR COMBUSTÍVEL + CARO / + BARATO-=-=-=-=-=-=-=-=-\n'
      f'Preços por L de GASOLINA:\n'
      f'{posto_gasolina_mais_cara}    R${gasolina_mais_cara:.2f}\n'  # Mostra o posto mais caro e seu preço
      f'{posto_gasolina_mais_barata}    R${gasolina_mais_barata:.2f}\n'  # Mostra o posto mais barato e seu preço
      f'Preços por L de ETANOL:\n'
      f'{posto_etanol_mais_caro}    R${etanol_mais_caro:.2f}\n'  # Mostra o posto mais caro e seu preço
      f'{posto_etanol_mais_barato}    R${etanol_mais_barato:.2f}\n'  # Mostra o posto mais barato e seu preço
      f'Preços por L de DIESEL:\n'
      f'{posto_diesel_mais_caro}    R${diesel_mais_caro:.2f}\n'  # Mostra o posto mais caro e seu preço
      f'{posto_diesel_mais_barato}    R${diesel_mais_barato:.2f}')  # Mostra o posto mais barato e seu preço
