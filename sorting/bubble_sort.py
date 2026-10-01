def bubble_sort(vetor):
    for i in range(0, len(vetor) - 1):
        for j in range(0, len(vetor) - 1 - i):
            if vetor[j + 1] < vetor[j]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor

def main():
    vetor = [5, 3, 8, 4, 6]
    print(vetor)
    print(bubble_sort(vetor))

if __name__ == "__main__":
    main()