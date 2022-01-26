from random import randint
from time import sleep

def cardapio():
    print('\033[0;33m=-=Cárdapio=-=\033[m\n'
          '[1] = Bebidas \n' 
          '[2] = Comidas/lanches \n' 
          '[3] = Sobremesas\doces \n' 
          '[4] = Cancelar')
    opc2 = str(input('Informe sua opção: '))
    return opc2
def painel():
    print('\033[4;34m=-=-Login/Cadastro-=-=\033[m\n'
          '[1] Cadastro \n'
          '[2] Login \n'
          '[3] Sair ')
    opc = input('Informe uma opção: ')
    return opc
def login():
    log = str(input('Informe o seu nome\033[4m(não é necessário colocar nome completo, ou coloque sem espaço)\033[m: '))
    sen = input('Informe uma senha: ')
    return log, sen
def buscar(log, sen):
    usuario = []
    try:
        with open('usuario.txt', 'r', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip("")
                usuario.append(linha.split())
            for usuario in usuario:
                nome = usuario[0]
                password = usuario[1]
                if log == nome and sen == password:
                    return True
    except FileNotFoundError:
        return False

log = ''
sen = ''
adeus = ''
adeus1 = ''
pedido = ''
exed = ''
pedi = ''
pedil = ''
bebidas = ('\033[4;33m--BEBIDAS--\033[m\n'
           '[1] = Suco de uva\n'
           '[2] = Suco de laranja\n'
           '[3] = Suco de Limão\n'
           '[4] = Cancelar')
comlan = ('\033[4;33m=-=Comidas/Lanches=-=\033[m\n'
        '--Lanches--\n'
        '[1] = Hámburguer\n'
        '[2] = Hot-Dog/Cachorro-Quente\n'
        '--Comidas--\n'
        '[3] = Arroz com feijão e fritas\n'
        '[4] = Lasanha\n'
        '[5] = Cancelar')
sobr =('\033[4;33m=-=Sobremesas/Doces=-=\033[m\n'
    '[1] = Brgadeiro\n'
    '[2] = Prestigio Gelado\n'
    '[3] = Mousse\n'
    '[4] = Cancelar')
cont = ''
opc2 = ''
senha = randint(0, 100)
#Esta compactação de while serve para o cadastro e o login dos usuários, onde as informações são salvas em arquivos .txt
#Diferentes para logados ou cadastrados
while True:
    opc = painel()
    if opc == '1' or opc == 'cadastro':
        log, sen = login()
        #O sistema da 3 chances de informar nome e senha após isso o programa é encerrado
        while log == sen:
            print('\033[4mSua senha deve ser diferente do nome informado\033[m')
            sen = input('Informe outra senha: ')
        while log == '':
            print('Informe um \033[0;31mnome\033[m para \033[4mmelhor configuração do sistema\033[m')
            log = input('Informe aqui seu nome: ')
        while sen == '':
            print('Coloque uma \033[0;31msenha\033[m para \033[4mmelhor segurança\033[m')
            sen = input('Informe aqui: ')
        while log == sen:
            print('Sua \033[4msenha deve ser diferente do nome informado\033[m')
            sen = input('Informe outra senha: ')
        while log == '':
            print('Informe um \033[0;31mnome\033[m para \033[4mmelhor configuração do sistema\033[m')
            log = input('Informe aqui seu nome: ')
        while sen == '':
            print('Coloque uma \033[0;31msenha\033[m para \033[4mmelhor segurança\033[m')
            sen = input('Informe aqui: ')
        while log == sen:
            print('Sua senha deve ser diferente do nome informado')
            sen = input('Informe outra senha: ')
        while log == '':
            print('Informe um nome para melhor configuração do sistema')
            log = input('Informe aqui seu nome: ')
        while sen == '':
            print('Coloque uma senha para melhor segurança')
            sen = input('Informe aqui: ')
        if '' or sen == '':
            print('Exedido o número de tentativas.')
            print('O programa será fechado.')
            adeus1 = 'vá embora'
            break
        user = buscar(log, sen)
        if user == True:
            '''Se existir ele retorna para o usuário...'''
            print('\033[0;31mUsuario já existe\033[m')
        else:
            '''Se o usuário não existir ele aceita o cadastro'''
            with open('usuario.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                arquivo.writelines(f'{log} {sen} \n')
            print('\033[0;32mCadastro aprovado\033[m')
            print(20 * '=')
            break
    elif opc == '2' or opc == 'login':
        log, sen = login()
        user = buscar(log, sen)
        if user == True:
            print('\033[1;32mLogin realizado com sucesso\033[m')
            if log != 'fun' and sen != 'funcionario@5544':
                print(f'Você utilizou \033[4m{log}\033[m como usuario e informou a senha \033[4m{sen}\033[m')
                print(20 * '=')
            break
        else:
            print('Você deve ter digitado seu \033[4mnome ou senha errado\033[m')
    elif opc == '3' or opc == 'sair':
        adeus = 'indo'
        log = ''
        break
    else:
        print('\033[0;31mOpção invalida\033[m')
        print('Tente novamente')
'''
este if serve para analisar se a pessoa que logou ou se cadastrou é um cliente
e dentro mostra o cárdapio, o pedido do usuário é salvo em arquivos .txt
'''
if log != 'fun' and log != '' and adeus1 != 'vá embora':
    if '2' in opc or 'login' in opc:
        with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
            arquivo.writelines(f'{pedi}\n')
        with open('usuariol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
            arquivo.writelines(f'{log}, {sen}')
    if '1' in opc or 'cadasto' in opc:
        with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
            arquivo.writelines(f'{pedi}\n')
        if cont != 'sim' or cont != '1':
            print('Obrigado pelo seu cadastro, VOCÊ ganho um desconto de 30% !!!')
    #Já este while serve para exibir o cárdapio e armazenar as informações e os pedidos dos clientes
    while True:
        opc2 = cardapio()
        print(15*'=')
        opc2.lower()
        if '1' in opc2 or 'bebida' in opc2:
            print(bebidas)
            print(15*'=')
            opcb = str(input('Qual bebida você gostaria ? '))
            opcb.lower()
            while opcb != 'uva'and opcb != 'suco de uva'and opcb != 'laranja'and opcb !='suco de laranja'and opcb !='limão'and opcb != 'suco de limão'and opcb != 'cancelar'and opcb != '1'and opcb != '2'and opcb != '3'and opcb != '4':
                print('\033[0;31mOpção inválida tente novamente\033[m')
                print(bebidas)
                opcb = input('Qual bebida você gostaria ?')
                opcb.lower()
            if '1' in opcb or 'uva' in opcb or 'suco de uva' in opcb:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido: {opcb}, nome/login: {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido: {opcb}, nome/login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                print('[1] = Sim\n'
                      '[2] = Não ')
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '2' in opcb or 'laranja' in opcb or 'suco de laranja' in opcb:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido bebida:{opcb} nome/login: {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido: {opcb}, nome/login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '3' in opcb or 'limão' in opcb or 'suco de limão' in opcb:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido bebida: {opcb} nome/login: {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido: {opcb}, nome/login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '4' in opcb or 'cancelar' in opcb:
                print('ok retornando para o cárdapio...')
        if '2' in opc2 or 'comidas' in opc2 or 'lanches' in opc2:
            print(comlan)
            print(15*'=')
            opcl = input('Qual comida ou lanche você gostaria ? ')
            opcl.lower()
            while opcl != '1' and opcl!= '2' and opcl != '3' and opcl != '4' and opcl != '5' and opcl!= 'hámburguer' and opcl != 'hamburguer' and opcl != 'arroz' and opcl != 'lasanha' and opcl != 'cancelar':
                print('\033[0;31mOpção inválida tente novamente\033[m')
                print(comlan)
                opcl = input('Qual comida ou lanche você gostaria ?')
                opcl.lower()
            if '1' in opcl or 'hámburguer' in opcl or 'hamburguer' in opcl:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido comida/lanche: {opcl} nome/login: {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido comida/lanche: {opcl} nome/login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '2' in opcl or 'hot dog' in opcl or 'hotdog' in opcl or 'cachorro quente' in opcl or 'cachorroquente' in opcl:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, opção lanche/comida: {opcl} nome/login {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opção do cardápio: {opc2}, pedido comida/lanche: {opcl} nome/login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '3' in opcl or 'arroz' in opcl:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2} pedido lanche/comida\: {opcl} nome/loggin: {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido comida/lanche: {opcl} nome/login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '4' in opcl or 'lasanha' in opcl:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2} pedido lanche/comida: {opcl} nome/loggin: {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2}, pedido comida/lanche: {opcl} nome/login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '5' in opcl or 'cancelar' in opcl:
               print('Ok retornando para o cárdapio...')
        if '3' in opc2 or 'doce' in opc2 or 'sobremesa' in opc2:
            print(sobr)
            print(15*'=')
            opcd = input('Qual comida ou lanche você gostaria ? ')
            opcd.lower()
            while opcd != '1' and opcd!= '2' and opcd != '3' and opcd != '4' and opcd != 'brigadeiro' and opcd != 'prestigio gelado' and opcd != 'mousse' and opcd != 'cancelar':
                print('\033[0;31mOpção inválida tente novamente\033[m')
                print(sobr)
                opcd = input('Qual comida ou lanche você gostaria ? ')
                opcd.lower()
            if '1' in opcd or 'brigadeiro' in opcd:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2} pedido doce:{opcd} nome\login: {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2} pedido doce:{opcd} nome\login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '2' in opcd or 'prestigio gelado' in opcd:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2} doce pedido: {opcd} nome/login {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2} pedido doce:{opcd} nome\login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida...')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '3' in opcd or 'mousse' in opcd:
                if '2' in opc or 'login' in opc:
                    with open('pedidol.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2} dece pedido: {opcd} nome/login: {log}\n')
                if '1' in opc or 'cadasto' in opc:
                    with open('pedido.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'opcao do cardapio: {opc2} pedido doce:{opcd} nome\login: {log}\n')
                cont = str(input('Ok, você gostaria de mais alguma coisa ? '))
                cont.lower()
                if 'não' in cont or '2' in cont:
                    print('Ok já iremos preparar seu pedido')
                    break
                while cont != 'sim' and cont != 'não':
                    print('Opção invalida')
                    cont = str(input('Você gostaria de mais alguma coisa ? '))
                    cont.lower()
                    if 'não' in cont or '2' in cont:
                        print('Ok já iremos preparar seu pedido')
                        break
            if '4' in opcd or 'cancelar' in opcd:
                print('Ok retornando para o cárdapio...')
        if '4' in opc2 or 'sair' in opc2:
            adeus = 'indo'
            break
        if opc2 != '1' and opc2 != '2' and opc2 != '3' and opc2 != '4':
            print('\033[0;31mOpção inválida tente novamente\033[m')
#if simples para encerrar o programa se o usuário desejar sair
if adeus == 'indo':
    print('Ok, até uma próxima !')
    print('Tenha um bom dia')
'''
if utilizado para mostrar as informações dos clientes, 
isso se quem logou for um funcionario, para isso utilizei também a comparação de senha.
'''
if log == 'fun' and sen == '5544':
    print(15* '=-')
    print(bebidas)
    print(15 * '=-')
    print(comlan)
    print(15 * '=-')
    print(sobr)
    print(15* '=-')
    print('\033[4;34m=-=USUÁRIOS=-=\033[m')
    usunl = open('usuario.txt', 'r')
    print(usunl.read())
    usunl.seek(0)
    print(15 * '=-')
    print('\033[4;34m=-=USUÁRIO LOGIN=-=\033[m')
    usul = open('usuariol.txt', 'r')
    print(usul.read())
    usul.seek(0)
    print('\033[4;34m=-=PEDIDO LOGIN=-=\033[m')
    pedil = open('pedidol.txt', 'r')
    print(pedil.read())
    pedil.seek(0)
    print(15 * '=-')
    print('\033[4;34m=-=PEDIDO CADASTRO=-=\033[m')
    pedi = open('pedido.txt', 'r')
    print(pedi.read())
    pedi.seek(0)
    print(15*'=-')
    print('\033[4;34m=-=MESA DO CLIENTE=-=\033[m')
    mes = open('mesa.txt', 'r')
    print(mes.read())
    mes.seek(0)
'''
este if é utilizado para o cliente escolher como retirará seu pedido(por entrega ou retirada no balcão)
2 arquivos .txt são utilizados para guardar as informações de usuários logados e seus pedidos,
os usúarios cadastrados e seus pedidos são salvos em outros 2 arquivos
'''
#Também é criado um arquivo só para guardar o número da mesa do cliente
if opc != '3' and opc != 'sair' and opc2 != '4' and opc2 != 'sair' and log != 'fun' and sen != '5544':
    sleep(5)
    print(15*'=')
    ret = str(input('Você gostaria que \033[4mlavássemos\033[m seu pedido até sua mesa \nou você vem \033[4mretirar\033[m no balcão ? '))
    ret.lower()
    if 'retirar' in ret or 'balcão' in ret:
        print(f'Ok, Sua \033[4msenha\033[m é: {senha}.')
        print('Aguarde sua senha \033[4maparecer no monitor\033[m')
        print('Agardecemos sua presença tenha um bom dia!')
    if 'mesa' in ret or 'levar' in ret or 'entregue':
        mesa = int(input('Ok, \033[4minforme o número da sua mesa para mais agilidade\033[m: '))
        print('Muito obrigado aguarde alguns instantes enquanto preparamos seu pedido')
        print('Sua presença é muito importante para nós')
        with open('mesa.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
            arquivo.writelines(f'Onde cliente se encontra: {mesa}, nome/login: {log}\n')
    if ret != 'retirar' or ret != 'balcão' or ret != 'mesa' or ret != 'levar' or ret != 'entregue':
        print('Opção inválida')
'''
os outros 2 arquivos .txt são arquivos para guardar as informações de usuários logados e seus pedidos,
os usúarios cadastrados e seus pedidos são salvos em outros arquivos
'''
'''
Este programa possui alguns erros: um deles é que o sistema aceita números como forma de nome,
outro erro é que o sistema de continuar ou não seu pedido só aceita a opção de não continuar(isso em forma de número,
que corresponde ao 2).
O último erro que eu reparei foi que o sistema pede o número da mesa, mesmo que o úsuario tenha pedido para retirar no 
balcão
'''
#Este programa utilizou 430 linhas, possui 5 arquivos .txt e demorou 3 dias para ser feito
