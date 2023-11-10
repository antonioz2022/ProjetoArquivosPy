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
