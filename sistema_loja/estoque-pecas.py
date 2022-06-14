listaPecas = []


def realce(s1):
    tamCab = len(cab) - 9

    print('\033[34m_\033[m' * tamCab)
    print('\033[1;36m                            ', s1, '\033[m')
    print('\033[34m_\033[m' * tamCab)


# --------------Começo da Função: Cadastramento de peças---------------------------------
def cadastrarPeca(cod):
    # ----------Cabeçalho do menu de castro de peças---------------------------------------
    print()
    print('\033[7;32mMenu de CADASTRO de peças\033[m\n')
    print('\033[1;36mCodigo de peça: \033[4;32m{}\033[m'.format(cod))

    codigo = cod
    # ----------- Entrada de dados(armazenados em variáveis)para cadastro de peças-------
    while True:
        nomePeca = input('\033[1;36mDigite o nome da peça: ➜ \033[m ')
        if nomePeca == "":
            print('\033[1;31;40m VALOR INVÁLIDO  ❌ \033[m')
        else:
            break
    while True:
        fabriPeca = input('\033[1;36mDigite o fabricante da peça: ➜ \033[m ').upper()
        if fabriPeca == "":
            print('\033[1;31;40m VALOR INVÁLIDO  ❌ \033[m')
        else:
            break
    while True:
        valorPeca = input('\033[1;36mDigite o valor da peça: ➜ \033[m ')
        if valorPeca == "":
            print('\033[1;31;40m VALOR INVÁLIDO  ❌ \033[m')
        else:
            break
    print()
    print('\033[1;32;40mPEÇA CADASTRADA COM SUCESSO ✔ \033[m')
    print()







    # -----Inserindo no dicionário dicPecas os dados recebidos e armazenados nas variáveis-------
    dicPecas = {'Código': cod,
                'Nome da peça': nomePeca,
                'Fabricante da peça': fabriPeca,
                'Valor da peça': valorPeca}
    # -----Copiando para a lista------------
    listaPecas.append(dicPecas.copy())


# --------------Fim do função: Cadastramento de peças---------------------------


# --------------Função para consultar peças-------------------------------------
def consultarPeca():
    while True:

        try:
            # ----------Cabeçalho do menu consulta de peças---------------------------------------
            print()
            print('\033[7;93m    Menu de consulta de peças  \033[m\n')
            print('\033[33m1)    Consultar Todas as Peças\033[m')
            print('\033[33m2)    Consulta Peças por Código\033[m')
            print('\033[33m3)    Consulta Peças por Fabricante\033[m')
            print('\033[31m4)    Retornar\033[m')

            opConsultar = int(input('\n\033[1;36mEscolha uma das opções acima: ➜ \033[m '))
            print('\033[33m--\033[m' * 70)

            # -------Caso o usuário desejar consultar todas as peças----------------------------------
            if opConsultar == 1:
                print('\033[1;33;40m Consultar todas as peças  \033[m\n  ')
                print('\033[33m--\033[m' * 70)

                # -----Esse 'for' vai em cada item da lista de peças--------
                for pecas in listaPecas:
                    # -----vai percorrer em cada conjunto (chave/valor) do dicionário contido na lista peças---(ex: 'Nome peça' :'Banco')
                    for key, value in pecas.items():
                        # -----Print de cada conjunto---
                        print('{} : {} '.format(key, value))
                    print('\033[33m--\033[m' * 70)

            # -----------Caso o usuário desejar consultar por código de peça-------------------------
            elif opConsultar == 2:

                print('\033[1;33;40mConsultar peças por código  \033[m\n')
                try:
                    consultaCod = int(input('\n\033[1;36mDigite o código deseja: ➜ \033[m'))
                    for pecas in listaPecas:
                        if (pecas['Código'] == consultaCod):
                            for key, value in pecas.items():
                                print('{} : {} '.format(key, value))


                except ValueError:
                    print(
                        '\033[1;31;40mERRO! Você digitou um caractere no lugar de número ou um valor com virgula\033[m')

            # -----------Caso o usuário desejar consultar por Fabricante----------------------------
            elif opConsultar == 3:
                print('\033[1;33;40mConsultar peças por Fabricante  \033[m\n')
                try:
                    consultaFabri = input('\n\033[1;36mDigite o FABRICANTE desejado: ➜ \033[m').upper()
                    for pecas in listaPecas:
                        if (pecas['Fabricante da peça'] == consultaFabri):
                            for key, value in pecas.items():
                                print('{} : {} '.format(key, value))


                except ValueError:
                    print(
                        '\033[1;31;40mERRO! Você digitou um caractere no lugar de número ou um valor com virgula\033[m')

            # -----------Caso o usuário desejar retornar------------------------
            elif opConsultar == 4:
                break

            # -----------Caso o usuário digitar um número que não esteja na lista-------------------------
            else:
                print('\033[1;31;40mERRO! Opção inválida! \033[m')
                continue
        except ValueError:
            print('\033[1;31;40mERRO! Você inseriu um caractere ou número com virgula\033[m')


# --------------Fim da Função para consultar peças------------------------------

# --------------Função para remover peças---------------------------------------
def removerPeca():
    print('\033[7;37mMenu de remoção de peças\033[m\n')
    remover = int(input('\n\033[1;36mDigite o código deseja para remover a peça: ➜ \033[m'))
    for pecas in listaPecas:
        if (pecas['Código'] == remover):
            listaPecas.remove(pecas)
            print('\033[1;31;40mPEÇA REMOVIDA COM SUCESSO ✔ \033[m')



# --------------FIM da Função para remover peças---------------------------------------

# -------------Programa principal----------------------------------------------

cab = ('\033[7;32mBem vindo a bicicletaria ︽ Speed Night Bikes ︽ - João da Silva Barbosa \033[m')
print()
print(cab)
codPeca = 100

while True:
    realce('MENU')
    print('\033[1;32m1- Cadastrar Peça\033[m')
    print('\033[1;33m2- Consultar Peça\033[m')
    print('\033[1;37m3- Remover Peças\033[m')
    print('\033[1;31m4- Sair\033[m')
    try:
        resp = int(input('\033[1;36mEscolha uma das opções acima: ➜\033[m '))
        if resp == 1:
            print('\033[34m_\033[m' * 70)
            codPeca = codPeca + 1
            cadastrarPeca(codPeca)

        elif resp == 2:
            print('\033[34m_\033[m' * 70)
            consultarPeca()
        elif resp == 3:
            print('\033[34m_\033[m' * 70)

            removerPeca()
        elif resp == 4:
            print('\033[34m_\033[m' * 70)
            print('\033[1;31mSaindo...\033[m')
            print('\033[34m_\033[m' * 70)

            break
        else:
            print(
                '\033[1;31;40mERRO! Opção inválida! \033[m')
    except ValueError:
        print('\033[1;31;40mERRO! Você digitou um caractere no lugar de número ou um valor com virgula\033[m')

# -------------Fim--Programa principal----------