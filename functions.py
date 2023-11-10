def agruparLivros(arquivo_nome):
    dictionary_categorias = {}
    arquivo = open(arquivo_nome, "r")
    for f in arquivo:
        arquivo_split = f.strip().split(",")
        genero = arquivo_split[3].lower()
        if genero not in dictionary_categorias:
            lista_categorias = [arquivo_split[0]]
            dictionary_categorias[genero] = lista_categorias
        else:
            dictionary_categorias[genero].append(arquivo_split[0])
    for j in dictionary_categorias:
        print(j.upper() + ":")
        with open(arquivo_nome) as arquivo_2:
            for a in arquivo_2:
                arquivo_split = a.strip().split(",")
                if arquivo_split[0] in dictionary_categorias[j]:
                    print(
                        "Nome:",
                        arquivo_split[0],
                        "Autor(a):",
                        arquivo_split[1],
                        "Preço:",
                        float(arquivo_split[2]),
                        "R$",
                    )
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


def verBiblioteca(arquivo_nome):
    arquivo = open(arquivo_nome)
    print("                           BIBLIOTECA")
    for f in arquivo:
        arquivo_split = f.strip().split(",")
        print(
            "Nome: " + arquivo_split[0] + ",",
            "Autor(a): " + arquivo_split[1] + ",",
            "Preço:",
            float(arquivo_split[2]),
            "R$,",
            "Genero: " + arquivo_split[3],
        )


def atualizarLivro(arquivo_nome, nome, opcao, valor):
    lista_livros = []
    with open(arquivo_nome) as arquivo:
        for a in arquivo:
            lista_livros.append(a)
    count = 0
    for k in lista_livros:
        if k.split(",")[0] == nome:
            if opcao == "nome":
                string_replace = k.replace(k.split(",")[0], valor)
                lista_livros[count] = string_replace
            elif opcao == "autor":
                string_replace = k.replace(k.split(",")[1], valor)
                lista_livros[count] = string_replace
            elif opcao == "preço":
                v = float(valor)
                string_replace = k.replace(k.split(",")[2], str(v))
                lista_livros[count] = string_replace
            elif opcao == "genero":
                string_replace = k.replace(k.split(",")[3], valor)
                lista_livros[count] = string_replace
        count += 1
    with open(arquivo_nome, "w") as arquivo_2:
        for l in lista_livros:
            if l == lista_livros[len(lista_livros) - 1]:
                arquivo_2.write(l.strip())
            else:
                arquivo_2.write(l)


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
            print(
                "Nome:",
                arquivo_split[0] + ",",
                "Autor(a):",
                arquivo_split[1] + ",",
                "Preço:",
                float(arquivo_split[2]),
                "R$",
            )
    arquivo.close()


def livroMaisCaro(arquivo_nome):
    mais_caro = 0
    nome_mais_caro = []
    with open(arquivo_nome) as arquivo:
        for f in arquivo:
            preço = float(f.strip().split(",")[2])
            if preço > mais_caro:
                mais_caro = preço
    with open(arquivo_nome) as arquivo:
        for j in arquivo:
            nome = j.strip().split(",")[0]
            preço = float(j.strip().split(",")[2])
            if preço == mais_caro:
                nome_mais_caro.append(nome)

    if len(nome_mais_caro) > 1:
        print("Mais de um livro com maior preço!")
        print("Nomes:")
        for n in nome_mais_caro:
            print(n)
    else:
        print("Nome: ", nome_mais_caro[0])
    print("Preço:", mais_caro, "R$")


def gastosTotais(arquivo_nome):
    arquivo = open(arquivo_nome, "r")
    soma = 0
    for f in arquivo:
        arquivo_split = f.strip().split(",")
        soma += float(arquivo_split[2])
    arquivo.close()
    return soma
