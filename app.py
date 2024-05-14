import os

livros = [{'titulo':'A Revolução dos Bichos', 'autor':'George Orwell', 'disponível':False, 'nota': '8'}, 
          {'titulo':'Dom Quixote', 'autor':'Miguel de Cervantes', 'disponível':True, 'nota': '10'},
          {'titulo':'O Pequeno Príncipe', 'autor':'Antoine de Saint-Exupéry', 'disponível':False, 'nota': '4'}]

def exibir_nome_do_programa():
    print("""
Biblioteca Express
""")

def exibir_opcoes():
    print('1. Cadastrar livro')
    print('2. Listar livros')
    print('3. Alternar estado do livro')
    print('4. Avalie o livro')
    print('5. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar aplicativo')

def voltar_ao_menu_principal():
    input('\nPressione qualquer tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_livro():
    exibir_subtitulo('Cadastro de novos livros')
    titulo_do_livro = input('Digite o título do livro que deseja cadastrar: ')
    autor = input(f'Digite o nome do autor do livro "{titulo_do_livro}": ')
    dados_do_livro = {'titulo':titulo_do_livro, 'autor':autor, 'disponível':False}
    livros.append(dados_do_livro)
    print(f'O livro "{titulo_do_livro}" foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_livros():
    exibir_subtitulo('Listando livros')

    print(f"{'Título do livro':<25} | {'Autor':<20} | Disponível | {'Nota':<5}")
    for livro in livros:
        titulo_livro = livro['titulo']
        autor = livro['autor']
        disponivel = 'Sim' if livro['disponível'] else 'Não'
        nota = livro.get('nota', 'Ainda não avaliado')
        print(f'- {titulo_livro:<20} | {autor:<20} | {disponivel:<10} | {nota:>5}')

    voltar_ao_menu_principal()



def alternar_estado_livro():
    exibir_subtitulo('Alterando estado do livro')
    titulo_livro = input('Digite o título do livro que deseja alterar o estado: ')
    livro_encontrado = False

    for livro in livros:
        if titulo_livro == livro['titulo']:
            livro_encontrado = True
            livro['disponível'] = not livro['disponível']
            mensagem = f'O livro "{titulo_livro}" foi marcado como disponível' if livro['disponível'] else f'O livro "{titulo_livro}" foi marcado como indisponível'
            print(mensagem)
            
    if not livro_encontrado:
        print('O livro não foi encontrado')
            
    voltar_ao_menu_principal()

def avalie_livro():
    exibir_subtitulo('Avalie o livro')
    titulo_livro = input('Digite o título do livro que deseja avaliar: ')
    livro_encontrado = False

    for livro in livros:
        if titulo_livro == livro['titulo']:
            livro_encontrado = True
            try:
                nota = int(input('Digite a nota para este livro (de 1 a 10): '))
                if 1 <= nota <= 10:
                    livro['nota'] = str(nota)
                    print(f'A avaliação para o livro "{titulo_livro}" foi registrada com sucesso.')
                else:
                    print('Por favor, insira uma nota entre 1 e 10.')
            except ValueError:
                print('Por favor, insira uma nota válida.')
    
    if not livro_encontrado:
        print('O livro não foi encontrado')
    voltar_ao_menu_principal()
            

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_livro()
        elif opcao_escolhida == 2: 
            listar_livros()
        elif opcao_escolhida == 3: 
            alternar_estado_livro()
        elif opcao_escolhida == 4: 
            avalie_livro()
        elif opcao_escolhida == 5: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
