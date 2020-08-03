def plusMinus(arr, n) :
    zeros = 0
    natural = 0
    negative = 0 
    for ar in arr :
        if ar == 0:
            zeros += 1
        elif ar > 0:
            natural += 1
        else:
            negative += 1
    print(natural / n)
    print(negative / n)
    print(zeros / n)


def main():
    n = int(input(''))
    numbers = str(input(''))
    numbers = numbers.split()
    for number in range(len(numbers)):
        numbers[number] = int(numbers[number])
    
    plusMinus(numbers, n)


if __name__ == "__main__":
    main()