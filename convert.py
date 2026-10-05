digit_to_value = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

value_to_digit = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


def repToDecimal(representation, base):
    decimal_value = 0
    power = 0
    for digit in reversed(representation.upper()):
        value = digit_to_value[digit]
        decimal_value += value * (base ** power)
        power += 1
    return decimal_value


def decimalToRep(number, base):
    if number == 0:
        return '0'
    result = []
    while number > 0:
        remainder = number % base
        result.append(value_to_digit[remainder])
        number = number // base
    return ''.join(reversed(result))


def main():
    print("Testing repToDecimal:")
    print('repToDecimal("10", 8) =', repToDecimal("10", 8))
    print('repToDecimal("10", 16) =', repToDecimal("10", 16))
    print('repToDecimal("A", 16) =', repToDecimal("A", 16))
    print('repToDecimal("FF", 16) =', repToDecimal("FF", 16))
    print('repToDecimal("1010", 2) =', repToDecimal("1010", 2))

    print("\nTesting decimalToRep:")
    print('decimalToRep(8, 8) =', decimalToRep(8, 8))
    print('decimalToRep(16, 16) =', decimalToRep(16, 16))
    print('decimalToRep(10, 16) =', decimalToRep(10, 16))
    print('decimalToRep(255, 16) =', decimalToRep(255, 16))
    print('decimalToRep(10, 2) =', decimalToRep(10, 2))


if __name__ == "__main__":
    main()
