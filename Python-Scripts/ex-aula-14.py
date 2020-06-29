import math

def mediaGeometrica(numero, listaPar, terminou):
    if(terminou):
        a = 1
        for i in range(len(listaPar)):
            a = a * listaPar[i]
        a = (a ** (-len(listaPar)))
        return a
    else:
        listaPar.append(numero)

def mediaAritmetica(numero, listaImpar, terminou):
    if(terminou):
        a = 0
        for i in range(len(listaImpar)):
            a = a + listaImpar[i]
        a = (a / len(listaImpar))
        return a
    else:
        listaImpar.append(numero)

def main():
    print("Aula 14 - Web Dev.\n\n")
    print("> Média Geométrica para para valores pares.\n> Média Aritmética para impáres.\n")
    print("** Deseja inverter o exercicio ? **\n")
    print("1 - Sim\n0 - Não")
    op = int(input())
    terminou = False
    if(op == 0):
        quantNum = float(input("Digite a quantidade dos números: "))
    
        listaNumeros = []
        listaPar = []
        listaImpar = []

        print("Digite os numeros abaixo\n")
        i = 0
        while (i < quantNum):
            print(">: ")
            listaNumeros.append(float(input()))
            i = i + 1
        print("\n")
        print(listaNumeros)
        print("\n")
        i = 0
        for i in range(len(listaNumeros)):
            if (i % 2 == 0):
                mediaGeometrica(listaNumeros[i], listaPar, terminou)
            else: mediaAritmetica(listaNumeros[i], listaImpar, terminou)
        terminou = True
        print("Média Geométrica: %d",( mediaGeometrica(listaNumeros[i], listaPar,terminou)) )
        print("Média Aritmética: %d",( mediaGeometrica(listaNumeros[i], listaImpar,terminou)) )
    else:
        quantNum = float(input("Digite a quantidade dos números: "))
    
        listaNumeros = []
        listaPar = []
        listaImpar = []

        print("Digite os numeros abaixo\n")
        i = 0
        while (i < quantNum):
            print(">: ")
            listaNumeros.append(float(input()))
            i = i + 1
        print("\n")
        print(listaNumeros)
        print("\n")
        i = 0
        for i in range(len(listaNumeros)):
            if (i % 2 != 0):
                mediaGeometrica(listaNumeros[i], listaImpar, terminou)
            else: mediaAritmetica(listaNumeros[i], listaPar, terminou)
        terminou = True
        print("Média Geométrica: %d",( mediaGeometrica(listaNumeros[i], listaImpar,terminou)) )
        print("Média Aritmética: %d",( mediaGeometrica(listaNumeros[i], listaPar,terminou)) )

main()
