def counting_sort(vetor):
    count = [0] * (max(vetor) + 1)
    for x in vetor:
        count[x] += 1
    i = 0
    for v in range(len(count)):
        while count[v] > 0:
            vetor[i] = v
            i += 1
            count[v] -= 1
    return vetor

def main():
    vetor = [1, 3, 7, 8, 1, 1, 3]
    print(counting_sort(vetor))

if __name__ == "__main__":
    main()
                