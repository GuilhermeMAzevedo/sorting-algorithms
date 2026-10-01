def merge_sort(vetor):
    if len(vetor) == 1:
        return vetor
    else:
        meio = len(vetor) // 2
        esquerdo = merge_sort(vetor[:meio])
        direito = merge_sort(vetor[meio:])
        return merge(esquerdo, direito)

def merge(esquerdo, direito):
    resultado = []
    while len(esquerdo) != 0 and len(direito) != 0:
        if esquerdo[0] <= direito[0]:
            resultado.append(esquerdo[0])
            esquerdo.remove(esquerdo[0])
        else:
            resultado.append(direito[0])
            direito.remove(direito[0])
    resultado.extend(esquerdo)
    resultado.extend(direito)
    return resultado

def main():
    vetor = [38, 27, 43, 3, 9, 82, 10]
    print(vetor)
    print(merge_sort(vetor))

if __name__ == "__main__":
    main()