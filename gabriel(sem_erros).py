from time import sleep
from random import randint

adeus = ''
adeus1 = ''
adeus2 = ''
nome = ''
senha = ''
bebida = ('\033[4;33m--BEBIDAS--\033[m\n'
          '[1] = Suco de uva\n'
          '[2] = Suco de laranja\n'
          '[3] = Suco de limão\n'
          '[4] = Sair')
comlan = ('\033[4;33m--LANCHES/COMIDAS--\033[m\n'
          '[1] = Hámburguer\n'
          '[2] = Hot Dog/Cachrro Quente\n'
          '[3] = Lasanha\n'
          '[4] = kibe\n'
          '[5] = Sair')
dobresa = ('\033[4;33m--SOBREMESAS/DOCES--\033[m\n'
           '[1] = Brigadeiro\n'
           '[2] = Prestigio Gelado\n'
           '[3] = Mousse\n'
           '[4] = Sair')
beb = ''
com = ''
sob = ''
nmr = ''
mesa = ''
car = ''

def painel():
    print('\033[4;34m=-=Login--LanchoneteSucot=-=\033[m\n'
          '[1] = Cadastro\n'
          '[2] = Login\n'
          '[3] = Sair')
    opc = input('Informe sua opção: ')
    return opc
def login():
    nome = str(input('Informe seu nome: '))
    while '1' in nome or '2' in nome or '3' in nome or '4' in nome or '5' in nome or '6' in nome or '7' in nome or '8' in nome or '9' in nome or '10' in nome:
        print('\033[0;31mnome inválido\033[m')
        nome = input('Informe outro nome válido: ')
    senha = (input('Informe a sua senha: '))
    return (nome, senha)
def buscar(nome, senha):
    usuarios = []
    try:
        with open('usuarios(sem_erros).txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                usuarios.append(linha.split())
            for usuario in usuarios:
                log = usuario[0]
                password = usuario[1]
                if nome == log and senha == password:
                    return True
    except FileNotFoundError:
        return False
def cardapio():
    print('\033[4;33m=-=CÀRDPIO=-=\033[m'
          '\n[1] = Bebidas'
          '\n[2] = Comidas/Lanches'
          '\n[3] = Doces/sobremesas'
          '\n[4] = Sair')
    car = input('Qual a sua escolha ? ')
    return car

#while usado para fazer login ou cadastro de usuarios.
while True:
    opc = painel()
    opc.lower()
    if opc == '1' or opc == 'cadastro':
        nome, senha = login()
        while nome == senha:
            print('Sua \033[4msenha tem que ser diferente do nome informado\033[m')
            senha = input('Informe outra senha: ')
        while senha == '':
            print('\033[0;31mSenha inválida...\033[m')
            senha = input('Informe uma \033[4msenha para mais segurança\033[m: ')
        while nome == '' or '1' in nome or '2' in nome or '3' in nome or '4' in nome or '5' in nome or '6' in nome or '7' in nome or '8' in nome or '9' in nome or '10' in nome:
            print('\033[0;31mNome inválido...\033[m')
            nome = input('Informe um \033[4mnome para melhor configuração do sistema:\033[m ')
        user = buscar(nome, senha)
        if user == True:
            print('\033[0;31mUsúario já existe !\033[m')
            print('Tente novamente')
        else:
            with open('usuarios(sem_erros).txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                arquivo.writelines(f'{nome} {senha}\n')
            print('\033[0;32mCadastro aprovado !\033[m')
            print(15* '=')
            break
    elif opc == '2' or opc == 'login':
        nome, senha = login()
        user = buscar(nome, senha)
        if user == True:
            print('\033[0;32mLogin realizado com sucesso !\033[m')
            print(15* '=')
            break
        else:
            print('Você pode ter informado seu \033[4mnome\033[m ou sua \033[4msenha de forma incorreta\033[m, tente novamente...')
    elif opc == '3' or opc == 'sair':
        adeus = 'indo'
        break
    else:
        print('\033[0;31mOpcão invalida\033[m')
#if para mostrar o cárdapio e o usuário poder informar seus pedidos.
if nome != 'fun' and senha != '5544@' and opc != '3' and opc != 'Sair':
    if '1' in opc or 'cadastro' in opc:
        print('Bem-vindo ao programa da Lanchonete Sucot')
    if '2' in opc or 'login' in opc:
        print('Bem vindo de volta !')
    while adeus1 != 'pedif':
        opc2 = input('deseja o cárdapio ?'
                    '\n[1] = Sim    [2] = Não'
                    '\nInforme aqui a sua escolha: ')
        opc2.lower()
        if '1' in opc2 or 'sim' in opc2:
            while True and adeus1 != 'pedif':
                car = (cardapio())
                car.lower()
                if car == '1' or car == 'bebida':
                    while True:
                        print(bebida)
                        beb = input('Informe seu pedido: ')
                        beb.lower()
                        if '1' in beb or 'suco de uva' in beb or 'uva' in beb:
                            contb = input('Ok gostaria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            contb.lower()
                            if 'sim' in contb or '1' in contb:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in contb or '2' in contb:
                                print('Ok, já iremos preparar seu pedido')
                                adeus1 = 'pedif'
                                break
                        elif '2' in beb or 'suco de laranja' or 'laranja' in beb:
                            contb1 = input('Ok gostaria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            contb1.lower()
                            if 'sim' in contb1 or '1' in contb1:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in contb1 or '2' in contb1:
                                print('Ok, já iremos preparar seu pedido')
                                adeus1 = 'pedif'
                                break
                        elif '3' in beb or 'suco de limão' in beb or 'limão' in beb:
                            contb2 = input('Ok gostaria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            contb2.lower()
                            if 'sim' in contb2 or '1' in contb2:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in contb2 or '2' in contb2:
                                adeus1 = 'pedif'
                                break
                        elif '4' in beb or 'sair' in beb:
                            sleep(2)
                            adeus = 'indo'
                            break
                        else:
                            print('Opção inválida tente novamente')
                elif car == '2' or car == 'comida' or car == 'lanche':
                    while True:
                        print(comlan)
                        com = input('Informe seu pedido: ')
                        com.lower()
                        if '1' in com or 'hamburguer' in com or 'hámburguer' in com:
                            contl = input('Ok gosteria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            contl.lower()
                            if 'sim' in contl or '1' in contl:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in contl or '2' in contl:
                                print('Ok, já iremos preparar seu pedido')
                                adeus1 = 'pedif'
                                break
                        elif '2' in com or 'hot dog' in com or 'hotdog' in com or 'cachorro quente' in com or 'cachorroquente' in com:
                            contl1 = input('Ok gosteria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            contl1.lower()
                            if 'sim' in contl1 or '1' in contl1:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in contl1 or '2' in contl1:
                                print('Ok, já iremos preparar seu pedido')
                                adeus1 = 'pedif'
                                break
                        elif '3' in com or 'lasanha' in com:
                            contl2 = input('Ok gosteria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            contl2.lower()
                            if 'sim' in contl2 or '1' in contl2:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in contl2 or '2' in contl2:
                                print('Ok, já iremos preparar seu pedido')
                                adeus1 = 'pedif'
                                break
                        elif '4' in com or 'kibe' in com:
                            contl3 = input('Ok gosteria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            contl3.lower()
                            if 'sim' in contl3 or '1' in contl3:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in contl3 or '2' in contl3:
                                print('Ok, já iremos preparar seu pedido')
                                adeus1 = 'pedif'
                                break
                        elif '5' in com or 'sair' in com:
                            sleep(2)
                            adeus = 'indo'
                            break
                        else:
                            print('Opção inválida')
                elif car == '3' or car == 'doces' or car == 'sobremesa':
                    while True:
                        print(dobresa)
                        sob = input('Informe o seu pedido: ')
                        sob.lower()
                        if '1' in sob or 'brigadeiro' in sob:
                            conts = input('Ok gosteria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            conts.lower()
                            if 'sim' in conts or '1' in conts:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in conts or '2' in conts:
                                print('Ok, já iremos preparar seu pedido')
                                adeus1 = 'pedif'
                                break
                        elif '2' in sob or 'prestigio gelado' in sob or 'prestigiogelado' in sob:
                            conts1 = input('Ok gosteria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            conts1.lower()
                            if 'sim' in conts1 or '1' in conts1:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in conts1 or '2' in conts1:
                                print('Ok, já iremos preparar seu pedido')
                                adeus1 = 'pedif'
                                break
                        elif '3' in sob or 'mousse' in sob:
                            conts3 = input('Ok gosteria de mais alguma coisa ?\n'
                                          '[1] = Sim    [2] = Não\n'
                                          'Informe aqui: ')
                            conts3.lower()
                            if 'sim' in conts3 or '1' in conts3:
                                print('retornando ao cárdapio')
                                break
                            elif 'não' in conts3 or '2' in conts3:
                                print('Ok, já iremos preparar seu pedido')
                                adeus1 = 'pedif'
                                break
                        elif '4' in sob or 'sair' in sob:
                            sleep(2)
                            adeus = 'indo'
                            break
                        else:
                            print('Opção inválida')
                elif car ==  '4' or car == 'sair':
                    sleep(2)
                    adeus = 'indo'
                    break
                else:
                    print('Opção inválida tente novamente...')
            if car == '4' or car == 'sair':
                sleep(2)
                adeus = 'indo'
                break
        elif '2' in opc2 or 'não' in opc2:
            sleep(2)
            adeus = 'indo'
            break
        else:
            print('Opção inválida tente novamente')
#if para o cliente poder dizer se quer que entregue ou se vai retirar.
if adeus1 == 'pedif':
    sleep(5)
    print(15*'=')
    ent = input('Você gostaria que \033[4mentreguassemos\033[m o seu pedido\n'
                'Ou você vem \033[4mretirar no balcão\033[m ?\n'
                '[1] = Entrega [2] = Retirar no balcão\n'
                'Informe aqui: ')
    if 'entrega' in ent or '1' in ent or 'mesa' in ent:
        mesa = int(input('Ok, \033[4minforme o número da sua mesa para mais agilidade\033[m\n'
                         'Informe aqui:'))
        print('Agora aguarde apenas mais alguns instantes')
        print(5*'=--')
        print('\033[0;32mAgradecemos a sua presença\033[m')
        print('\033[4;34mO programa agora será encerrado...\033[m')
        sleep(2)
    if 'retirar' in ent or '2' in ent or 'balcão' in ent:
        nmr = randint(1, 100)
        print(f'Ok, sua senha é: \033[4m{nmr}\033[m')
        print('Aguarde ela aparecer no monitor acima do balcão.')
        print(5*'=--')
        print('\033[0;32mAgradecemos a sua presença.\033[m')
        print('\033[0;34mO programa agora será encerrado...\033[m')
        sleep(2)
    adeus2 = 'pedidof'
#if usado só para poder guardar as informações de pedidos.
if adeus2 == 'pedidof':
    with open('pedidos(sem_erros).txt', 'a+', encoding='Utf-8', newline='')as arquivo:
        arquivo.writelines(f'\nNome informado:{nome} \nMesa que se encontra:{mesa} ou senha adiquirida:{nmr}\n'
                           f'Opcao de bebida:{beb}, opcao de lanche/comida:{com}, opcao de doce/sobremesa:{sob}\n')
'''
if utilizado para diferenciar se quem está utilizando o programa no momento é um funcionário,
Para só assim mostrar as informações dos seus clientes.
'''
if 'fun' in nome and '5544@' in senha:
    print('Bem vindo de volta')
    sleep(2)
    print(bebida)
    print(15*'=')
    print(comlan)
    print(15*'=')
    print(dobresa)
    print(15*'=')
    usu1 = (open('usuarios(sem_erros).txt', 'r'))
    print(usu1.read())
    usu1.seek(0)
    print(15*'=-')
    usu2 = (open('pedidos(sem_erros).txt', 'r'))
    print(usu2.read())
    usu2.seek(0)
#If para encerrar o progrma caso usuário quiser.
if adeus == 'indo':
    print('Ok, programa será fechado...')
    print('Tenha um bom dia')
