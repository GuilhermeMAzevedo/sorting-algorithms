def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave
    return vetor

def main():
    vetor = [85, 12, 59, 45, 72, 51]
    print(vetor)
    print(insertion_sort(vetor))

if __name__ == "__main__":
    main()