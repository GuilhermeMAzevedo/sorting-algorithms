def shell_sort(vetor):
    gap = len(vetor) // 2
    while gap >= 1:
        for i in range(gap, len(vetor)):
            chave = vetor[i]
            j = i
            while j >= gap and vetor[j - gap] > chave:
                vetor[j] =  vetor[j - gap]
                j -= gap
            vetor[j] = chave
        gap //= 2
    return vetor

def main():
    vetor = [80, 93, 60, 12, 42, 30, 68, 85, 10]
    print(shell_sort(vetor))

if __name__ == "__main__":
    main()
        

