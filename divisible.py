
if __name__ == '__main__':
    output = []
    for number in range(2000, 3201):
        if number % 7 == 0 and number % 5 != 0:
            output.append(number)
    print(*output, sep=",")