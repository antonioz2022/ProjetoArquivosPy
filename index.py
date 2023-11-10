import functions


def main():
    opção = -1
    while opção != 0:
        print("           Menu")
        print("1 - Adicione um livro")
        print("2 - Remova um livro")
        print("3 - Agrupe livros em gêneros")
        print("4 - Gastos totais")
        print("5 - Buscar livros por gênero")
        print("6 - Ver bibliotecar")
        print("7 - Busque pelo livro mais caro")
        print("8 - Atualize algum livro da biblioteca")
        print("0 - Parar o programa")
        opção = int(input())
        if opção == 1:
            nome = input("Digite o nome do livro: ")
            autor = input("Digite o nome do autor do livro: ")
            try:
                preço = float(input("Digite o preço do livro: "))
            except ValueError:
                print("\nERRO!")
                print("Preço tem que ser um número.")
                continue
            genero = input("Digite o genero do livro: ")
            functions.adicionarLivro("books.txt", nome, autor, str(preço), genero)
        elif opção == 2:
            nome = input("Digite o nome do livro que você deseja remover: ")
            functions.removerLivro("books.txt", nome)
        elif opção == 3:
            functions.agruparLivros("books.txt")
        elif opção == 4:
            print("Gastos totais:", functions.gastosTotais("books.txt"), "R$")
        elif opção == 5:
            genero = input("Digite o genero que você deseja buscar:")
            functions.buscar("books.txt", genero)
        elif opção == 6:
            functions.verBiblioteca("books.txt")
        elif opção == 7:
            functions.livroMaisCaro("books.txt")
        elif opção == 8:
            nome = input("Digite o nome do livro que você deseja atualizar: ")
            opcao = input("Digite o que você deseja atualizar no livro ('nome', 'preço', 'autor' ou 'genero'): ")
            valor = input(f"Digite o novo {opcao} que ira substituir o antigo: ")
            functions.atualizarLivro("books.txt", nome, opcao, valor)
        elif opção == 0:
            print("Desligando...")
        else:
            print("Opção não reconhecida!")


if __name__ == "__main__":
    main()
