# coding: utf-8

def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise TypeError
    # if not 0 < input < 4000:
    #     raise ValueError
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)


def roman_to_int(input):
    """ Convert a Roman numeral to an integer.
    """
    if not isinstance(input, type("")):
        raise TypeError
    input = input.upper(  )
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]
            # If the next place holds a larger number, this value is negative
            if i+1 < len(input) and nums[input[i+1]] > value:
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
