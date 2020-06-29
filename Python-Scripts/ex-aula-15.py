def transposta(matriz, size):
    transposta = list()
    transposta = [[linha[i] for linha in matriz] for i in range(size)]
    return transposta

def parse(x):
    return lambda x: x % 2 == 0

#Filtra os valores do vetor q são pares
def foo(rule, dict):
    print("Conteudo filtrado: \n")
    _list_ = list(filter(rule, dict["numeros"]))
    return _list_

def _foo_alunos_(rule, dict):
    localList = list()
    for i in range(len(dict)):
        if(rule(dict[i]) == True):
            localList.append(dict[i])
    return localList

# Filtrando as chaves q são pares
def _foo_parser_(rule, dict):
    localList = list(filter(rule,dict))
    return localList

# Programa inicial
def main():

    matriz = [[1,0,33,0,2], [65,22,33,44,2], [1,2,3,8,96]]

    dicionario1 = {'numeros': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]}
    dicionario2 = {
        0: {'Professor': 'James'},
        1: {'Professor': 'João'},
        2: {'Aluno': 'Kevin'},
        3: {'Aluno': 'Claudio'},
        4: {'Aluno': 'Leo'},
        5: {'Aluno': 'Lucas'}
    }
    dicionario3 = {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar', 6: 'par', 7: 'impar'}

    print("******************************************************\n")
    print("* Aula 15 - Web Dev                                  *\n")
    print("* Desafio                                            *\n")
    print("* Filtrando contents no dicionario...                *\n")
    print("******************************************************\n")

    print("               **DESAFIO**     \n")
    print("\nMatriz passada: \n", matriz)
    print("\nTransposta: \n", transposta(matriz,5))
    print("\n             **FIM DESAFIO**     \n")

    print("Dicionarios nao filtrados:n\n")
    print("Dicionario 1:", dicionario1)
    print("Dicionario 2:", dicionario2)
    print("Dicionario 3:", dicionario3)

    print("\n       **Conteudos dos dicionarios1 e 3, somente pares**\n")
    print("Dicionario 1:", foo(lambda x: x % 2 == 0,dicionario1))
    print("Dicionario 3:", _foo_parser_((lambda item: item % 2 == 0),dicionario3))
    print("\n       **Conteudos dos dicionarios1 e 3, somente pares**\n")

    print("\n       **Conteudo do dicionario2, Alunos ou Professores**\n")
    print(_foo_alunos_((lambda item: 'Aluno' in item), dicionario2))
    print("\n       **Conteudo do dicionario2, Alunos ou Professores**\n")

main()