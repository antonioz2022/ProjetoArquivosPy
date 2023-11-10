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


def adicionarLivro(arquivo_nome, nome, autor, preço, genero):
    arquivo = open(arquivo_nome, "a")
    arquivo_r = open(arquivo_nome, "r")
    if len(arquivo_r.read()) == 0:
        arquivo.write(nome + "," + autor + "," + preço + "," + genero)
    else:
        arquivo.write("\n" + nome + "," + autor + "," + preço + "," + genero)
    arquivo.close()
    arquivo_r.close()


def removerLivro(arquivo_nome, nome):
    arquivo = open(arquivo_nome)
    check = 0
    linhas = arquivo.readlines()
    for l in linhas:
        if l.strip().split(",")[0] == nome:
            check = 1
    if check == 1:
        for l in linhas:
            if l.strip().split(",")[0] == nome:
                linhas.remove(l)
        with open(arquivo_nome, "w") as a:
            for linha in linhas:
                if linha == linhas[len(linhas) - 1]:
                    a.write(linha.strip())
                else:
                    a.write(linha)

    else:
        print("Não existe livro com esse nome no arquivo.")
        return
    check = 0
    for l in arquivo:
        if l.strip.split(",")[0] == nome:
            check = 1
    if check == 0:
        print("Livro removido com sucesso!")
    else:
        print("Livro não removido")
    arquivo.close()


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
