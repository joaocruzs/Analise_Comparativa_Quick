# Analise_Comparativa_Quick
Partições no Quick Sort: Estudo Comparativo com Merge Sort e Heap Sort Através de Experimentos Computacionais

## Descrição
Dispõe-se dos seguintes códigos para se realizar uma análise experimental dos algoritmos de ordenação Quick Sort - um para Hoare e outro ara Lommuto - além de Merge Sort e Heap Sort.
1. Quick usando Loare <br>
   Escolhe-se um pivô e rearranja-se os elementos de forma a dividir o array em duas partes - menores a esquerda e maiores a direita - para que de forma recursiva ele seja ordenado.
2. Quick usando Lomuto <br>
   Similar a metodologia do Loare, porém com um único índice de partição - neste caso tendo como pivô o último elemento do array.
3. Merge Sort <br>
   Divide recursivamente o array em subarrays menores, ordena cada subarray e os combina de forma ordenada. 
4. Heap Sort <br>
   Transforma o array em uma heap máxima, remove o maior elemento (raiz) iterativamente e ajusta a heap até ordenar todos os elementos.

