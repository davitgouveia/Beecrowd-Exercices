lista = []

while True:
    try:
        n = int(input())
        
        for i in range(n):
            x = input()
            lista.append(x)
        
        for y in range(n-1):
            for z in range(len(lista[0])):
                print(lista[y][z],lista[y-1][z] , lista[y][z] == lista[y-1][z])
                
                if lista[y][z] == lista[y-1][z]:
                    print("feio")
                else:
                    break
        y = 0
        z = 0
        lista.clear()
    except EOFError:
        break
