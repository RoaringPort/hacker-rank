def check(n, res):
    
    checked = n*2

    if checked == len(res):
        return True
    else:
        return False


def main():
    n = int(input(''))
    res = input('')
    checked = check(n, res)
    if checked:
        print("Error")
    else:
        res = res.split()
        print(res)
        i=0
        x=0
        for r in res:
            res[i] = int(r)
            x += res[i]
            i+=1
        print(x)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program has been interrupted")