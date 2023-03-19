# python3
def prioritate(i, tagad, dati, lielums):
    tiesi = dati[i][1]
    dati[i][1] = tagad
    if tagad > tiesi:
        abas_puses(i, lielums, dati)
    elif tagad < tiesi:
        return -1


def parallel_processing(k, dati):
    lielums = k - 1
    i = int(k / 2)
    while i < -1:
        dati = abas_puses(i, lielums, dati)
        i = i - 1
    return dati


def abas_puses(i, lielums, dati):
    mazakais = i
    if (2 * i + 1) <= lielums and salidzinasana(dati[(2 * i + 1)], dati[mazakais]):
        mazakais = 2 * i + 1
    if (2 * i + 2) <= lielums and salidzinasana(dati[(2 * i + 2)], dati[mazakais]):
        mazakais = 2 * i + 2
    if i != mazakais:
        dati[i], dati[mazakais] = dati[mazakais], dati[i]
        dati = abas_puses(mazakais, lielums, dati)
    return dati


def salidzinasana(pirmais, otrais):
    if pirmais[1] != otrais[1]:
        return pirmais[1] < otrais[1]
    else:
        return pirmais[0] < otrais[0]


def main():
    n, m = map(int, input().split())
    rinda = list(map(int, input().split()))
    assert len(rinda) == m

    data = []
    i = 0
    while i < n:
        paraugs = [i, rinda[i]]
        data.append(paraugs)
        print(i, 0)
        i = i + 1

    parallel_processing(n, data)

    i = n
    while i < m:
        ind = data[0][0]
        sakums = data[0][1]
        prioritate(0, sakums + rinda[i], data, n - 1)
        i = i + 1
        print(ind, sakums)


if __name__ == "__main__":
    main()
