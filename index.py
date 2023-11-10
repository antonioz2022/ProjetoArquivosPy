def main():
    #buscar("books.txt", "romance")
    #print(gastosTotais("books.txt"))
    #agruparLivros("books.txt")
    opção = -1
    while opção != 0:
        printMenu()
        opção = int(input())
        if(opção == 1):
            adicionarLivro("books.txt")
        elif(opção == 2):
            removerLivro("books.txt")
        elif(opção == 3):
            agruparLivros("books.txt")
        elif(opção == 4):
            print("Gastos totais:",gastosTotais("books.txt"), "R$")
        elif(opção == 5):
            genero = input("Digite o genero que você deseja buscar:")
            buscar("books.txt", genero)
        elif(opção == 0):
            print("Desligando...")
        else:
            print("Opção não reconhecida!")

def printMenu():
    print("           Menu")
    print("1 - Adicione um livro")
    print("2 - Remova um livro")
    print("3 - Agrupe livros em gêneros")
    print("4 - Gastos totais")
    print("5 - Buscar livros por gênero")
    print("0 - Parar o programa")


def agruparLivros(arquivo_nome):
    dictionary_categorias = {}
    arquivo = open(arquivo_nome, "r")
    for f in arquivo:
        arquivo_split = f.strip().split(",")
        if arquivo_split[3] not in dictionary_categorias:
            lista_categorias = [arquivo_split[0]]
            dictionary_categorias[arquivo_split[3]] = lista_categorias
        else:
            dictionary_categorias[arquivo_split[3]].append(arquivo_split[0])
    #print(dictionary_categorias)
    for j in dictionary_categorias:
        print(j.upper() + ":")
        for k in dictionary_categorias[j]:
            print(k)
    arquivo.close()


def adicionarLivro(arquivo_nome):
    print("Hello World")


def removerLivro(arquivo_nome):
    print("Hello World")


def buscar(arquivo_nome, genero):
    arquivo = open(arquivo_nome, "r")
    for f in arquivo:
        arquivo_split = f.strip().split(",")
        if arquivo_split[3].lower() == genero.lower():
            print(arquivo_split[0])
    arquivo.close()


def gastosTotais(arquivo_nome):
    arquivo = open(arquivo_nome, "r")
    soma = 0
    for f in arquivo:
        arquivo_split = f.strip().split(",")
        soma += float(arquivo_split[2])
    arquivo.close()
    return soma

if __name__ == "__main__":
    main()

