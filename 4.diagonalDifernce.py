def diagonalDif(matrix): 
    right = 0
    left = 0
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                right += matrix[i][j]
    i = len(matrix) - 1
    while i >= 0:
        j = len(matrix[i])
        while j >= 0:
            if j+i == (len(matrix) - 1):
                left += matrix[i][j]
            j -=1
        i -= 1

    #print(right,' ',left)
    res = abs(right-left)   
    return res


def main():
    n = int(input(''))
    array = [] 
    for sub_n in range(n):
        array.append(1)

    for arr in range(len(array)):
        sub = str(input(''))
        sub = sub.split()
        for n in range(len(sub)):
            sub[n] = int(sub[n])
        array[arr] = sub

    res = diagonalDif(array)
    print(res)


if __name__ == '__main__':
    main()