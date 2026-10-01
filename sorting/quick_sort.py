def quick_sort(vetor, lo, hi):
    if lo >= hi:
        return
    pivot = vetor[hi]
    i = lo
    for j in range(lo, hi):
        if vetor[j] < pivot:
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
    vetor[i], vetor[hi] = vetor[hi], vetor[i]
    quick_sort(vetor, lo, i - 1)
    quick_sort(vetor, i + 1, hi)
    return vetor

def main():
    vetor = [19, 7, 15, 12, 16, 18, 4, 11, 13]
    print(vetor)
    print(quick_sort(vetor, 0, len(vetor) - 1))

if __name__ == "__main__":
    main()
