def comparesTriplets(a, b):
    i=0
     #     a b
    alice = 0
    bob = 0
    while(i<3):
        if (a[i] == 0 or b[i] == 0) and (a[i] <= 100 or b[i]):
            print('Error')
        else:
            if a[i] > b[i]:
                alice=alice+1
                #print("alice recive")
            elif a[i] < b[i]:
                bob=bob+1
                #print("bob recive")
            else:
                pass
                #print("no one recive")
        i += 1
    return f'{alice} {bob}'


def main():
    res_a = input()
    res_a = res_a.split()
    i=0
    a=[0,0,0]
    for sub_a in res_a:
        a[i] = int(sub_a)
        i += 1
    res_b = input()
    res_b = res_b.split()
    i=0
    b=[0,0,0]
    for sub_b in res_b:
        b[i] = int(sub_b)
        i += 1

    res = comparesTriplets(a, b)
    print(res)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("keyboard interrupt")