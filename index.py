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
        print("0 - Parar o programa")
        opção = int(input())
        if opção == 1:
            functions.adicionarLivro("books.txt")
        elif opção == 2:
            functions.removerLivro("books.txt")
        elif opção == 3:
            functions.agruparLivros("books.txt")
        elif opção == 4:
            print("Gastos totais:", functions.gastosTotais("books.txt"), "R$")
        elif opção == 5:
            genero = input("Digite o genero que você deseja buscar:")
            functions.buscar("books.txt", genero)
        elif opção == 0:
            print("Desligando...")
        else:
            print("Opção não reconhecida!")


if __name__ == "__main__":
    main()
