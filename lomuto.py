import time
import statistics
import sys
from createArray import createArray

def quickSort(A,e,d): 

    if e<d:
         pivo=lomuto(A,e,d)
         quickSort(A,e,pivo-1)
         quickSort(A,pivo+1,d)
        
    
def lomuto(A,e,d):
     pivo=A[d]
     i=e-1

     for j in range(e,d):
          if A[j]<=pivo:
               i+=1
               A[i],A[j]=A[j],A[i]
              
     
     A[i],A[d]=A[d],A[i]
     return i+1


if __name__ == '__main__':

        size=int(input("Digite o tamanho do arquivo: "))
        sys.setrecursionlimit(size)
        historico_tempo = []
        for i in range(5):
            createArray(size)
            with open('entrada', 'r', encoding='utf-8') as arquivo:
                valores=arquivo.read().split()
                valoresInt = [int(valor) for valor in valores]
            inicio = time.perf_counter()*1000 #ms
            quickSort(valoresInt,0,len(valoresInt)-1)
            fim = time.perf_counter()*1000

            timer = (fim - inicio)
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ms')

        media = sum(historico_tempo) / 5
        desvio_padrao = statistics.stdev(historico_tempo)
        print(f'Tempo Médio: {media:.2f}ms')
        print(f'Desvio Padrão: {desvio_padrao:.2f}ms')
 