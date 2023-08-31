"""
/***********************************************************************************************
Autor: LUCAS DA CONCEIÇÃO DAMASCENO
Componente Curricular: EXA 854 - MI - Algoritmos
Comcluído em:
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação
************************************************************************************************/
"""


nome_posto1 = str(input('Digite o nome do primeiro posto: ')).strip().upper()

preco_gasolina_posto1 = input('Digite o valor da gasolina no posto 1: R$')
while not preco_gasolina_posto1.replace('.', '').isdigit() and not preco_gasolina_posto1.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_gasolina_posto1 = input('Digite o valor da gasolina no posto 1: R$')
preco_gasolina_posto1 = float(preco_gasolina_posto1.replace(',', '.'))

preco_etanol_posto1 = input('Digite o valor da etanol no posto 1: R$')
while not preco_etanol_posto1.replace('.', '').isdigit() and not preco_etanol_posto1.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_etanol_posto1 = input('Digite o valor do etanol no posto 1: R$')
preco_etanol_posto1 = float(preco_etanol_posto1.replace(',', '.'))

preco_diesel_posto1 = input('Digite o valor da diesel no posto 1: R$')
while not preco_diesel_posto1.replace('.', '').isdigit() and not preco_diesel_posto1.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_diesel_posto1 = input('Digite o valor do diesel no posto 1: R$')
preco_diesel_posto1 = float(preco_diesel_posto1.replace(',', '.'))

numero_de_vezes_posto_1_teve_menor_preco = 0
quantidade_de_litros_abastecidos_no_posto_1 = 0

nome_posto2 = str(input('Digite o nome do segundo posto: ')).strip().upper()

preco_gasolina_posto2 = input('Digite o valor da gasolina no posto 2: R$')
while not preco_gasolina_posto2.replace('.', '').isdigit() and not preco_gasolina_posto2.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_gasolina_posto2 = input('Digite o valor da gasolina no posto 2: R$')
preco_gasolina_posto2 = float(preco_gasolina_posto2.replace(',', '.'))

preco_etanol_posto2 = input('Digite o valor da etanol no posto 2: R$')
while not preco_etanol_posto2.replace('.', '').isdigit() and not preco_etanol_posto2.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_etanol_posto2 = input('Digite o valor do etanol no posto 2: R$')
preco_etanol_posto2 = float(preco_etanol_posto2.replace(',', '.'))

preco_diesel_posto2 = input('Digite o valor da diesel no posto 2: R$')
while not preco_diesel_posto2.replace('.', '').isdigit() and not preco_diesel_posto2.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_diesel_posto2 = input('Digite o valor do diesel no posto 2: R$')
preco_diesel_posto2 = float(preco_diesel_posto2.replace(',', '.'))

numero_de_vezes_posto_2_teve_menor_preco = 0
quantidade_de_litros_abastecidos_no_posto_2 = 0

nome_posto3 = str(input('Digite o nome do terceiro posto: ')).strip().upper()

preco_gasolina_posto3 = input('Digite o valor da gasolina no posto 3: R$')
while not preco_gasolina_posto3.replace('.', '').isdigit() and not preco_gasolina_posto3.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_gasolina_posto3 = input('Digite o valor da gasolina no posto 3: R$')
preco_gasolina_posto3 = float(preco_gasolina_posto3.replace(',', '.'))

preco_etanol_posto3 = input('Digite o valor da etanol no posto 3: R$')
while not preco_etanol_posto3.replace('.', '').isdigit() and not preco_etanol_posto3.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_etanol_posto3 = input('Digite o valor do etanol no posto 3: R$')
preco_etanol_posto3 = float(preco_etanol_posto3.replace(',', '.'))

preco_diesel_posto3 = input('Digite o valor da diesel no posto 3: R$')
while not preco_diesel_posto3.replace('.', '').isdigit() and not preco_diesel_posto3.replace(',', '').isdigit():
    print('Esse tipo de resposta não é valída... Tente novamente.')
    preco_diesel_posto3 = input('Digite o valor do diesel no posto 3: R$')
preco_diesel_posto3 = float(preco_diesel_posto3.replace(',', '.'))

numero_de_vezes_posto_3_teve_menor_preco = 0
quantidade_de_litros_abastecidos_no_posto_3 = 0

escolha_voltar = str(input('Deseja alterar alguma informação sobre o cadastros dos postos? [s/n] ')) \
    .strip().lower()
while escolha_voltar not in 'sn':
    print('Esse tipo de resposta não é valída... Tente novamente.')
    escolha_voltar = str(input('Deseja alterar alguma informação sobre o cadastros dos postos? [s/n] ')) \
        .strip().lower()

alteracao_posto = 0
if escolha_voltar == 's':
    alteracao_posto = input(f'Digite 1 para o posto {nome_posto1} \n'
                            f'Digite 2 para o posto {nome_posto2} \n'
                            f'Digite 3 para o posto {nome_posto3} \n'
                            f'Em qual posto você deseja fazer a alteração? ')
    while not alteracao_posto.isdigit() and alteracao_posto.isdigit() > 3 or alteracao_posto.isdigit() < 1:
        print('Esse tipo de resposta não é valída... Tente novamente.')
    alteracao_posto = int(alteracao_posto)
    print('Escolha qual informação deseja alterar...\n'
          'Digite 1 para alterar o nome do posto\n'
          'Digite 2 para alterar o valor da gasolina\n'
          'Digite 3 para alterar o valor do etanol\n'
          'Digite 4 para alterar o valor do diesel\n'
          'Digite 5 para alterar as todas as informações do posto')

    if alteracao_posto == 1:
        alteracao_info_posto = input(f'Qual sua escolha de alteração no posto {nome_posto1}? ')
        while not alteracao_info_posto.isdigit() and \
                alteracao_info_posto.isdigit() > 5 or alteracao_info_posto.isdigit() < 1:
            print('Esse tipo de resposta não é valída... Tente novamente.')
            alteracao_info_posto = input(f'Qual sua escolha de alteração no posto {nome_posto1}? ')

        if alteracao_info_posto == 1:
            certeza = ''
            while certeza not in 's':
                nome_posto1 = str(input('Digite o novo nome do posto 1: ')).strip().upper()
                certeza = str(input('Têm certeza quanto a alteração feita? [s/n] ')).strip().lower()

        elif alteracao_info_posto == 2:
            preco_gasolina_posto1 = input('Digite o novo valor da gasolina no posto 1: R$')
            while not preco_gasolina_posto1.replace('.', '').isdigit() \
                    and not preco_gasolina_posto1.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_gasolina_posto1 = input('Digite o novo valor da gasolina no posto 1: R$')
            preco_gasolina_posto1 = float(preco_gasolina_posto1.replace(',', '.'))

        elif alteracao_info_posto == 3:
            preco_etanol_posto1 = input('Digite o novo valor da etanol no posto 1: R$')
            while not preco_etanol_posto1.replace('.', '').isdigit() \
                    and not preco_etanol_posto1.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_etanol_posto1 = input('Digite o novo valor do etanol no posto 1: R$')
            preco_etanol_posto1 = float(preco_etanol_posto1.replace(',', '.'))

        elif alteracao_info_posto == 4:
            preco_diesel_posto1 = input('Digite o novo valor da diesel no posto 1: R$')
            while not preco_diesel_posto1.replace('.', '').isdigit() \
                    and not preco_diesel_posto1.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_diesel_posto1 = input('Digite o novo valor do diesel no posto 1: R$')
            preco_diesel_posto1 = float(preco_diesel_posto1.replace(',', '.'))

        elif alteracao_info_posto == 5:
            certeza = ''
            while certeza not in 's':
                nome_posto1 = str(input('Digite o novo nome do posto 1: ')).strip().upper()
                certeza = str(input('Têm certeza quanto a alteração feita? [s/n] ')).strip().lower()

            preco_gasolina_posto1 = input('Digite o valor da gasolina no posto 1: R$')
            while not preco_gasolina_posto1.replace('.', '').isdigit() and \
                    not preco_gasolina_posto1.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_gasolina_posto1 = input('Digite o valor da gasolina no posto 1: R$')
            preco_gasolina_posto1 = float(preco_gasolina_posto1.replace(',', '.'))

            preco_etanol_posto1 = input('Digite o valor da etanol no posto 1: R$')
            while not preco_etanol_posto1.replace('.', '').isdigit() and \
                    not preco_etanol_posto1.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_etanol_posto1 = input('Digite o valor do etanol no posto 1: R$')
            preco_etanol_posto1 = float(preco_etanol_posto1.replace(',', '.'))

            preco_diesel_posto1 = input('Digite o valor da diesel no posto 1: R$')
            while not preco_diesel_posto1.replace('.', '').isdigit() and not preco_diesel_posto1.replace(',',
                                                                                                         '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_diesel_posto1 = input('Digite o valor do diesel no posto 1: R$')
            preco_diesel_posto1 = float(preco_diesel_posto1.replace(',', '.'))

    elif alteracao_posto == 2:
        alteracao_info_posto = input(f'Qual sua escolha de alteração no posto {nome_posto2}? ')
        while not alteracao_info_posto.isdigit() and \
                alteracao_info_posto.isdigit() > 5 or alteracao_info_posto.isdigit() < 1:
            print('Esse tipo de resposta não é valída... Tente novamente.')
            alteracao_info_posto = input(f'Qual sua escolha de alteração no posto {nome_posto2}? ')

        if alteracao_info_posto == 1:
            certeza = ''
            while certeza not in 's':
                nome_posto2 = str(input('Digite o novo nome do posto 2: ')).strip().upper()
                certeza = str(input('Têm certeza quanto a alteração feita? [s/n] ')).strip().lower()

        elif alteracao_info_posto == 2:
            preco_gasolina_posto2 = input('Digite o novo valor da gasolina no posto 2: R$')
            while not preco_gasolina_posto2.replace('.', '').isdigit() \
                    and not preco_gasolina_posto2.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_gasolina_posto2 = input('Digite o novo valor da gasolina no posto 2: R$')
            preco_gasolina_posto2 = float(preco_gasolina_posto2.replace(',', '.'))

        elif alteracao_info_posto == 3:
            preco_etanol_posto2 = input('Digite o novo valor da etanol no posto 2: R$')
            while not preco_etanol_posto2.replace('.', '').isdigit() \
                    and not preco_etanol_posto2.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_etanol_posto2 = input('Digite o novo valor do etanol no posto 2: R$')
            preco_etanol_posto2 = float(preco_etanol_posto2.replace(',', '.'))

        elif alteracao_info_posto == 4:
            preco_diesel_posto2 = input('Digite o novo valor da diesel no posto 2: R$')
            while not preco_diesel_posto2.replace('.', '').isdigit() \
                    and not preco_diesel_posto2.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_diesel_posto2 = input('Digite o novo valor do diesel no posto 2: R$')
            preco_diesel_posto2 = float(preco_diesel_posto2.replace(',', '.'))

        elif alteracao_info_posto == 5:
            certeza = ''
            while certeza not in 's':
                nome_posto2 = str(input('Digite o novo nome do posto 2: ')).strip().upper()
                certeza = str(input('Têm certeza quanto a alteração feita? [s/n] ')).strip().lower()

            preco_gasolina_posto2 = input('Digite o novo valor da gasolina no posto 2: R$')
            while not preco_gasolina_posto2.replace('.', '').isdigit() \
                    and not preco_gasolina_posto2.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_gasolina_posto2 = input('Digite o novo valor da gasolina no posto 2: R$')
            preco_gasolina_posto2 = float(preco_gasolina_posto2.replace(',', '.'))

            preco_etanol_posto2 = input('Digite o novo valor da etanol no posto 2: R$')
            while not preco_etanol_posto2.replace('.', '').isdigit() \
                    and not preco_etanol_posto2.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_etanol_posto2 = input('Digite o novo valor do etanol no posto 2: R$')
            preco_etanol_posto2 = float(preco_etanol_posto2.replace(',', '.'))

            preco_diesel_posto2 = input('Digite o novo valor da diesel no posto 2: R$')
            while not preco_diesel_posto2.replace('.', '').isdigit() \
                    and not preco_diesel_posto2.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_diesel_posto2 = input('Digite o novo valor do diesel no posto 2: R$')
            preco_diesel_posto2 = float(preco_diesel_posto2.replace(',', '.'))

    elif alteracao_posto == 3:
        alteracao_info_posto = input(f'Qual sua escolha de alteração no posto {nome_posto3}? ')
        while not alteracao_info_posto.isdigit() and \
                alteracao_info_posto.isdigit() > 5 or alteracao_info_posto.isdigit() < 1:
            print('Esse tipo de resposta não é valída... Tente novamente.')
            alteracao_info_posto = input(f'Qual sua escolha de alteração no posto {nome_posto3}? ')

        if alteracao_info_posto == 1:
            certeza = ''
            while certeza not in 's':
                nome_posto3 = str(input('Digite o novo nome do posto 3: ')).strip().upper()
                certeza = str(input('Têm certeza quanto a alteração feita? [s/n] ')).strip().lower()

        elif alteracao_info_posto == 2:
            preco_gasolina_posto3 = input('Digite o novo valor da gasolina no posto 3: R$')
            while not preco_gasolina_posto3.replace('.', '').isdigit() \
                    and not preco_gasolina_posto3.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_gasolina_posto3 = input('Digite o novo valor da gasolina no posto 3: R$')
            preco_gasolina_posto3 = float(preco_gasolina_posto3.replace(',', '.'))

        elif alteracao_info_posto == 3:
            preco_etanol_posto3 = input('Digite o novo valor da etanol no posto 3: R$')
            while not preco_etanol_posto3.replace('.', '').isdigit() \
                    and not preco_etanol_posto3.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_etanol_posto3 = input('Digite o novo valor do etanol no posto 3: R$')
            preco_etanol_posto3 = float(preco_etanol_posto3.replace(',', '.'))

        elif alteracao_info_posto == 4:
            preco_diesel_posto3 = input('Digite o novo valor da diesel no posto 3: R$')
            while not preco_diesel_posto3.replace('.', '').isdigit() \
                    and not preco_diesel_posto3.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_diesel_posto3 = input('Digite o novo valor do diesel no posto 3: R$')
            preco_diesel_posto3 = float(preco_diesel_posto3.replace(',', '.'))

        elif alteracao_info_posto == 5:
            certeza = ''
            while certeza not in 's':
                nome_posto3 = str(input('Digite o novo nome do posto 3: ')).strip().upper()
                certeza = str(input('Têm certeza quanto a alteração feita? [s/n] ')).strip().lower()

            preco_gasolina_posto3 = input('Digite o novo valor da gasolina no posto 3: R$')
            while not preco_gasolina_posto3.replace('.', '').isdigit() \
                    and not preco_gasolina_posto3.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_gasolina_posto3 = input('Digite o novo valor da gasolina no posto 3: R$')
            preco_gasolina_posto3 = float(preco_gasolina_posto3.replace(',', '.'))

            preco_etanol_posto3 = input('Digite o novo valor da etanol no posto 3: R$')
            while not preco_etanol_posto3.replace('.', '').isdigit() \
                    and not preco_etanol_posto3.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_etanol_posto3 = input('Digite o novo valor do etanol no posto 3: R$')
            preco_etanol_posto3 = float(preco_etanol_posto3.replace(',', '.'))

            preco_diesel_posto3 = input('Digite o novo valor da diesel no posto 3: R$')
            while not preco_diesel_posto3.replace('.', '').isdigit() \
                    and not preco_diesel_posto3.replace(',', '').isdigit():
                print('Esse tipo de resposta não é valída... Tente novamente.')
                preco_diesel_posto3 = input('Digite o novo valor do diesel no posto 3: R$')
            preco_diesel_posto3 = float(preco_diesel_posto3.replace(',', '.'))

"""tipo_de_combustivel_cliente = ''
quantidade_de_litros = 0"""
