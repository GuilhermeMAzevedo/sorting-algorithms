def heap_sort(vetor):
    n = len(vetor)
    
    for i in range(n // 2 - 1, -1, -1): 
        heapfy(vetor, n, i)

    for i in range(n - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]
        heapfy(vetor, i, 0)
    return vetor

        

def heapfy(vetor, n, i):
    maior = i
    esquerda = 2*i + 1
    direita = 2*i + 2
    if esquerda < n and vetor[esquerda] > vetor[maior]:
        maior = esquerda
    if direita < n and vetor[direita] > vetor[maior]:
        maior = direita
    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        heapfy(vetor, n, maior)

def main():
    vetor = [10, 5, 7, 60, 4, 11, 45, 17, 9]
    print(heap_sort(vetor))

if __name__ == "__main__":
    main()