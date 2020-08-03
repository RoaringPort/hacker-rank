def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
    return unaLista


def main() :
    arr = input('')
    arr = arr.split()
    maxnum = []
    minnum = []
    for ar in range(len(arr)) :
        arr[ar] = int(arr[ar])
    arr = ordenamientoBurbuja(arr)
    for ar in range(len(arr)) :
        if ar == 0:
            minnum.append(arr[ar])
        elif ar == 1:
            maxnum.append(arr[ar])
            minnum.append(arr[ar])
        elif ar == 2:
            maxnum.append(arr[ar])
            minnum.append(arr[ar])
        elif ar == 3:
            maxnum.append(arr[ar])
            minnum.append(arr[ar])
        elif ar == 4:
            maxnum.append(arr[ar])
    print(sum(minnum), sum(maxnum))

if __name__ == "__main__" :
    main()