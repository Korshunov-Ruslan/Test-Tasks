TEN = 10
FIVE = 5
ONE = 1
requested_number = int(input('Введите сумму:\n'))


def main():
    count_of_ten = requested_number // TEN
    if count_of_ten == 0:
        count_of_five = 0
    else:
        count_of_five = (requested_number-count_of_ten*10) // FIVE
    count_of_one = (requested_number % FIVE) // ONE
    print(f'{count_of_ten} раз(а) номиналом -{TEN}-, '
          f'{count_of_five} раз(а) номиналом  -{FIVE}-, '
          f'{count_of_one} раз(а) номиналом -{ONE}-')


if __name__ == '__main__':
    main()
