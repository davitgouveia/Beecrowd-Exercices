entrada = input()

dias, saldo = entrada.split(" ")



dias = int(dias)
saldo = int(saldo)

saldoList = [saldo]

for x in range(dias):
    transacao = int(input())
    saldo = saldo + transacao
    saldoList.append(saldo)
    

print(min(saldoList))