"""Super ASCII String Checker
    A string "S" is said to super ascii string if and only if count of each
    character in the string is equal to its ascii value. Where ASCII code of
    'a' is 1, 'b' is 2 ...'z' is 26. """


def super_ascii(input_string):

    input_string = input_string.lower()
    alpha_list = map(chr, range(97, 123))
    try:
        while input_string[0]:
            char = input_string[0]
            count = input_string.count(char)

            if count is not (alpha_list.index(char) + 1):
                return False
            else:
                input_string = input_string.replace(char, '')

    except IndexError:
        return True

if __name__ == '__main__':
    user_input = raw_input('Enter s String for SUPER ASCII check\n')
    if super_ascii(user_input):
        print('String is SUPER ASCII')
    else:
        print('String is not SUPER ASCII')

