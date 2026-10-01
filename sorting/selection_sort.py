def selection_sort(vetor):
    for i in range(0, len(vetor) - 1):
        menor = i
        for j in range(i, len(vetor)):
            if vetor[j] < vetor[menor]:
                menor = j
        vetor[i], vetor[menor] = vetor[menor], vetor[i]
    return vetor

def main():
    vetor = [29, 72, 98, 13, 87, 66, 52, 51, 36]
    print(vetor)
    print(selection_sort(vetor))

if __name__ == "__main__":
    main()
            