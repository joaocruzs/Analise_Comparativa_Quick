import time
import statistics
from createArray import createArray


def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  
 
        heapify(arr, n, largest)
 
 
def heapSort(arr):
    n = len(arr)
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)
 

if __name__ == '__main__':
        size=int(input("Digite o tamanho do arquivo: "))
      
        historico_tempo = []
        for i in range(5):
            createArray(size)
            with open('entrada', 'r', encoding='utf-8') as arquivo:
                valores=arquivo.read().split()
                valoresInt = [int(valor) for valor in valores]
            inicio = time.perf_counter()*1000 #ms
            heapSort(valoresInt)
            fim = time.perf_counter()*1000

            timer = (fim - inicio)
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ms')

        media = sum(historico_tempo) / 5
        desvio_padrao = statistics.stdev(historico_tempo)
        print(f'Tempo Médio: {media:.2f}ms')
        print(f'Desvio Padrão: {desvio_padrao:.2f}ms')