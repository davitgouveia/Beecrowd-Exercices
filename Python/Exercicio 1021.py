entrada = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

resultado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

notas_moedas = [
    (100.00, "nota(s) de R$ 100.00"),
    (50.00, "nota(s) de R$ 50.00"),
    (20.00, "nota(s) de R$ 20.00"),
    (10.00, "nota(s) de R$ 10.00"),
    (5.00, "nota(s) de R$ 5.00"),
    (2.00, "nota(s) de R$ 2.00"),
    (1.00, "moeda(s) de R$ 1.00"),
    (0.50, "moeda(s) de R$ 0.50"),
    (0.25, "moeda(s) de R$ 0.25"),
    (0.10, "moeda(s) de R$ 0.10"),
    (0.05, "moeda(s) de R$ 0.05"),
    (0.01, "moeda(s) de R$ 0.01")
]

def decomposicao(value):
    if value > notas[0]:
        dividido = value // notas[0]
        resto = value - dividido * notas[0]
        resultado[0] = resultado[0] + 1 * dividido
        
        decomposicao(resto)
    elif value > notas[1]:
        dividido = value // notas[1]
        resto = value - dividido * notas[1]
        resultado[1] = resultado[1] + 1 * dividido
        
        decomposicao(resto)
    elif value > notas[2]:
        dividido = value // notas[2]
        resto = value - dividido * notas[2]
        resultado[2] = resultado[2] + 1 * dividido
        
        decomposicao(resto)
    elif value > notas[3]:
        dividido = value // notas[3]
        resto = value - dividido * notas[3]
        resultado[3] = resultado[3] + 1 * dividido
        
        decomposicao(resto)
    elif value > notas[4]:
        dividido = value // notas[4]
        resto = value - dividido * notas[4]
        resultado[4] = resultado[4] + 1 * dividido
        
        decomposicao(resto)
    elif value > notas[5]:
        dividido = value // notas[5]
        resto = value - dividido * notas[5]
        resultado[5] = resultado[5] + 1 * dividido
        
        decomposicao(resto)
    
    elif value > moedas[0]:
        dividido = value // moedas[0]
        resto = value - dividido * moedas[0]
        resultado[6] = resultado[6] + 1 * dividido
        
        decomposicao(resto)
    elif value > moedas[1]:
        dividido = value // moedas[1]
        resto = value - dividido * moedas[1]
        resultado[7] = resultado[7] + 1 * dividido
        
        decomposicao(resto)
    elif value > moedas[2]:
        dividido = value // moedas[2]
        resto = value - dividido * moedas[2]
        resultado[8] = resultado[8] + 1 * dividido
        
        decomposicao(resto)
    elif value > moedas[3]:
        dividido = value // moedas[3]
        resto = value - dividido * moedas[3]
        resultado[9] = resultado[9] + 1 * dividido
        
        decomposicao(resto)
    elif value > moedas[4]:
        dividido = value // moedas[4]
        resto = value - dividido * moedas[4]
        resultado[10] = resultado[10] + 1 * dividido
        
        decomposicao(resto)
    elif value > moedas[5]:
        dividido = value // moedas[5]
        resto = value - dividido * moedas[5]
        resultado[11] = resultado[11] + 1 * dividido
        
        decomposicao(resto)
    elif value == 0:
        return

decomposicao(entrada)

print("NOTAS:")
for valor, descricao in notas_moedas[:6]:
    quantidade = resultado[notas_moedas.index((valor, descricao))]
    print(f"{int(quantidade)} {descricao}")

print("MOEDAS:")
for valor, descricao in notas_moedas[6:]:
    quantidade = resultado[notas_moedas.index((valor, descricao))]
    print(f"{int(quantidade)} {descricao}")