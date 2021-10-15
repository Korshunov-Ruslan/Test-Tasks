row = input('Введите строку:\n')


def main():
    count = 0
    result = ''
    old = ''
    for i in range(len(row)):
        if row[i] != old:
            print(row[i])
            result += old
            print(result)
            old = row[i]
            if count != 0:
                result += str(count)
            count = 0
        count += 1
        if i == len(row)-1:
            result += row[i]+str(count)
    print(result)


if __name__ == '__main__':
    main()
