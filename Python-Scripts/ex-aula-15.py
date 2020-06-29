def main():
    listaObj = list()
    i = 0
    dicionario1 = {'numeros': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]}
    print("******************************************************\n")
    print("* Aula 15 - Web Dev                                  *\n")
    print("* Filtrando numeros pares dentro do dicionario...    *\n")
    print("******************************************************\n")

    print("Conteudo do dicionario:\n")
    print(dicionario1["numeros"])

    print("Conteudo filtrado: \n")
    for i in range(len(dicionario1["numeros"])):
        listaObj = list(filter(lambda x: x % 2 == 0, dicionario1["numeros"]))

    print(listaObj)

main()