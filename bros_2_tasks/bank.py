TEN = 10
FIVE = 5
ONE = 1
requested_number = int(input('Введите сумму:\n'))


def main():
    count_of_ten = requested_number // TEN  # Считаем нужное кол-во купюр номиналом 10
    if count_of_ten == 0:
        count_of_five = 0
    else:
        count_of_five = (requested_number-count_of_ten*10) // FIVE  # Считаем нужное кол-во купюр номиналом 5
    count_of_one = (requested_number % FIVE) // ONE  # Считаем нужное кол-во купюр номиналом 1
    print(f'{count_of_ten} раз(а) номиналом -{TEN}-, '
          f'{count_of_five} раз(а) номиналом  -{FIVE}-, '
          f'{count_of_one} раз(а) номиналом -{ONE}-')


if __name__ == '__main__':
    main()
