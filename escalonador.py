''' lucsgtv
    Escalonador de processos FIFO e SJF'''

import random,time
BAR = chr(9608)

class Processo:
    def __init__(self,nome):
        self.nome = nome
        self.tempo = 0
        self.criacao = 0
        #self.prioridade = prioridade

def fifo(sequencia):
    numeroprocessos = len(sequencia)
    somaesp = 0
    somapro = 0
    fila = []
    tupla = tuple()
    for i in sequencia:
        tupla = (i.nome,i.criacao,i.tempo)
        fila.append(tupla)
    fila.sort(key=lambda a: (a[1],a[2]))
    tempo=0
    tempoexe=0
    status =[]
    executando= True
    for i in fila:
        executando = True
        while executando:
            if tempo == int(i[1]) or tempo > int(i[1]):
                while True:
                    if int(i[2]) == tempoexe:
                        #criacao i[1] tucp i[2]
                        status.append((i[0],tempo-i[1]-i[2],tempo-i[1]))
                        tempoexe = 0
                        executando = False
                        break
                        tempo = tempo + 1
                    else:
                        print(i[0])
                        tempoexe = tempoexe + 1
                        tempo = tempo + 1

            else:
                print(BAR)
                tempo = tempo + 1

    for i in status:
        print('{0}: tempo de espera = {1} tempo de execucao = {2}'.format(i[0],i[1],i[2]))
        somaesp += i[1]
        somapro += i[2]
    TME = somaesp/numeroprocessos
    TMP = somapro/numeroprocessos
    print('TME = ', end = '')
    print(TME)
    print('TMP = ', end = '')
    print(TMP)
    return fila

def sjf(sequencia):
    numeroprocessos = len(sequencia)
    somaesp = 0
    somapro = 0
    fila = []
    fila1 =[]
    fila2 = []
    tupla = tuple()
    for i in sequencia:
        tupla = (i.nome,i.criacao,i.tempo)
        fila.append(tupla)
        fila1.append(tupla)
    fila.sort(key=lambda a: a[1])
    fila1.sort(key=lambda a: a[2])
    temp = fila[0][1]
    ucp = 0
    print(temp)
    for i in fila:
        if  i[1] <= temp and ucp <= i[2]:
            fila2.append(i)
        temp+=i[2]
        ucp += i[2]
    fila3 = []
    fila3 = fila2 + [i for i in fila1 if i[0] not in fila2]
    index = 1
    while index < len(fila3):
        if fila3[index] in fila3[ : index]:
            fila3.pop(index)
        else:
            index += 1
    tempo=0
    tempoexe=0
    status =[]
    pronto = []
    executando= True
    for i in fila3:
        executando = True
        while executando:
            if tempo == int(i[1]) or tempo > int(i[1]):
                while True:
                    if int(i[2]) == tempoexe:
                        #criacao i[1] tucp i[2]
                        status.append((i[0],tempo-i[1]-i[2],tempo-i[1]))
                        tempoexe = 0
                        executando = False
                        break
                        tempo = tempo + 1

                    else:
                        print(i[0])
                        tempoexe = tempoexe + 1
                        tempo = tempo + 1

            else:
                print(BAR)
                tempo = tempo + 1

    for i in status:
        print('{0}: tempo de espera = {1} tempo de execucao = {2}'.format(i[0],i[1],i[2]))
        somaesp += i[1]
        somapro += i[2]
    TME = somaesp/numeroprocessos
    TMP = somapro/numeroprocessos
    print('TME = ', end = '')
    print(TME)
    print('TMP = ', end = '')
    print(TMP)

    return fila3
def main():
    lista = []
    print('Digite o numero de processos: ')
    nomeprocessos = int(input())
    for p in range(nomeprocessos):
        lista.append(Processo('P'+str(p+1)))
    for i in lista:
            print('Tempo de UCP de {0} (-1 para aleatorio)'.format(i.nome))
            i.tempo = int(input())
            if i.tempo == -1:
                i.tempo = random.randint(1,20)
            print('Tempo de criacao de {0} (-1 para aleatorio)'.format(i.nome))
            i.criacao = int(input())
            if i.criacao == -1:
                i.criacao = random.randint(0,20)



    print('1-FIFO ou 2-SJF ')
    a = int(input())
    if a==1:
        print(fifo(lista))
    if a==2:
        print(sjf(lista))


if __name__ == '__main__':
    main()

