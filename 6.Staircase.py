def main():
    n = int(input(''))
    for sub in range(1, n):
        if sub == 0:
            pass
        else:
            print((n - sub -1) * ' ', sub * '#')
    print('#' * n)

if __name__ == '__main__':
    main()