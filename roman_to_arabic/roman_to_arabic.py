# coding: utf-8

def get_number_by_value(value):

    if value == 'M':
        return 1000
    elif value == 'D':
        return 500
    elif value == 'C':
        return 100
    elif value == 'L':
        return 50
    elif value == 'X':
        return 10
    elif value == 'V':
        return 5
    elif value == 'I':
        return 1
    else:
        return None

def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise TypeError

    result = []

    count = int(input/1000)
    result.append('M'*count)
    input -= 1000 * count
    count = int(input/900)
    result.append('CM'*count)
    input -= 900 * count
    count = int(input/500)
    result.append('D'*count)
    input -= 900 * count
    count = int(input/400)
    result.append('CD'*count)
    input -= 400 * count
    count = int(input/100)
    result.append('C'*count)
    input -= 100 * count
    count = int(input/90)
    result.append('XC'*count)
    input -= 90 * count
    count = int(input/50)
    result.append('L'*count)
    input -= 50 * count
    count = int(input/40)
    result.append('XL'*count)
    input -= 40 * count
    count = int(input/10)
    result.append('X'*count)
    input -= 10 * count
    count = int(input/9)
    result.append('IX'*count)
    input -= 9 * count
    count = int(input/5)
    result.append('V'*count)
    input -= 5 * count
    count = int(input/4)
    result.append('IV'*count)
    input -= 4 * count
    count = int(input/1)
    result.append('I'*count)
    input -= 1* count
    return ''.join(result)


def roman_to_int(input):
    """ Convert a Roman numeral to an integer.
    """
    if not isinstance(input, type("")):
        raise TypeError
    input = input.upper(  )
   
    sum = 0
    for i in range(len(input)):
        try:
            value = get_number_by_value(input[i])
            # If the next place holds a larger number, this value is negative
            if i+1 < len(input) and get_number_by_value(input[i+1]) > value:
                sum -= value
            else: sum += value
        except KeyError:
            raise ValueError

    if sum >= 4000:
        raise Exception('number is more than 4000')

    # easiest test for validity...
    if int_to_roman(sum) == input:
        return sum
    else:
        raise ValueError


def read_input():
    data = input('Введите последовательность с точкой на конце: ')
    return data[:len(data)-1]

if __name__ == '__main__':
    try:
        value = roman_to_int(read_input())
        print('Является числом - {}'.format(value))
    except:
        print('Не является числом < 4000')
