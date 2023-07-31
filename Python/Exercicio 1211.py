lista = []
economizou = 0
resultado = []

while True:
    try:
        n = int(input())
        
        for i in range(n):
            x = input()
            lista.append(x)
        
        for y in range(n-1):
            for z in range(len(lista[0])):
                if lista[y][z] == lista[y-1][z]:
                    economizou = economizou + 1
                else:
                    break
            resultado.append(economizou)
            economizou = 0
        y = 0
        z = 0
        lista.clear()
    except EOFError:
        for result in resultado:
            print(result)
        break
