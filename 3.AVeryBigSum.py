def aVeryBigSum(arr):
    res = 0
    for elem in arr:
        res += elem 
    return res   


def main():
    input('')
    arr=input('')
    arr=arr.split()
    i=0
    for ele in arr:
        arr[i] = int(arr[i])
        i += 1 
    res=aVeryBigSum(arr)
    print(res)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("keyboard interrupt")