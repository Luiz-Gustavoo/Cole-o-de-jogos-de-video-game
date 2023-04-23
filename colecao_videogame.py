def apresentacao(boas_vindas = 'Bem vindo ao coleciona games! Aqui você pode colocar todos os seus jogos favoritos! '):
    print('+', '-' * len(boas_vindas), '+')
    print('|', boas_vindas, '|')
    print('+', '-' * len(boas_vindas), '+')

def validar_opcao_menu(pergunta_opcao_menu, min_opcao, max_opcao): # validando se o input do usuario esta dentro das opções permitidas
    opcao_menu = int(input(pergunta_opcao_menu))
    while (opcao_menu < min_opcao) or (opcao_menu > max_opcao) :
        print('Escolha apenas as opções listadas acima.')
        opcao_menu = input(pergunta_opcao_menu)
    return opcao_menu

def existe_arquivo(nome_arquivo): # função que verifica se o arquivo colecao_jogos.txt existe
    try:
        abrir = open(nome_arquivo, 'rt') # abrir o arquivo
        print(abrir.read()) # ler o conteúdo do arquivo
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome_arquivo):
    try:
        arq = open(nome_arquivo, 'wt+') # abrindo o arqv passado. w: abrir arqv no modo gravação. t: arqv tipo texto. +: cria aqrv
    except:
        print('Erro na criação do arquivo.')
    else:
        print('Arquivo criado com sucesso.')

def cadastrar_jogo(arquivo_gravar, pergunta_nome_jogo, pergunta_desenvolvedora, pergunta_ano_lancamento): # função de cadastro de jogo
    abrir_arquivo = open(arquivo_gravar, 'at') # abrindo o arquivo passado como parametro
    nome_jogo = input(pergunta_nome_jogo)
    desenvolvedora = input(pergunta_desenvolvedora)
    lancamento = input(pergunta_ano_lancamento)
    abrir_arquivo.write(' Nome do jogo :{}; Desenvolvedora: {}; Ano de lançamento: {} \n'.format(nome_jogo, desenvolvedora, lancamento)) # gravando no arquivo 

def listar_colecao(arquivo_colecao): # função que mostra a lista de jogos
    arqv = open(arquivo_colecao, 'r')
    print(arqv.read())

# >>>>> programa principal <<<<<
arquivo = 'colecao_jogos.txt' # arquivo onde a coleção vai ser salva

if existe_arquivo(arquivo):
    print('Achamos o arquivo')
else:
    print('Não achamos o aquivo mas vamos cria-lo')
    criar_arquivo(arquivo)

apresentacao()

while True:
    print('1 = Cadastrar novo jogo')
    print('2 = Mostrar os jogos cadastrados')
    print('3 = sair')

    decisao_menu = validar_opcao_menu('O que deseja fazer?: ', 1, 3) # chamando funcao validar_opcao_menu e o intervalo de escolha no menu
    if decisao_menu == 1:
        cadastro = cadastrar_jogo(arquivo, 'Qual o nome do jogo?: ', 'Quem desenvolveu?: ', 'Em que ano foi lançado?: ') # chamando função cadastrar_jogo e passando os inputs como parametro 
    elif decisao_menu == 2:
        print('Aqui está a sua coleção:')
        listar_colecao(arquivo)
    elif decisao_menu == 3:
        print('Saindo...')
        break
