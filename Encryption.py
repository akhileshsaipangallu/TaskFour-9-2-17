""" Simple encryption library
    Support only English alphabets for encryption. Other characters cannot be
    encrypted. For a given letter, this algorithm will replace that letter
    with a letter that is 3 places further back in the alphabet. """


def encryption(input_string):
    input_string = input_string.upper()
    result = ''
    alpha_list = map(chr, range(65, 91))
    for char in input_string:
        if char in alpha_list:
            result += alpha_list[alpha_list.index(char) - 3]
        else:
            result += char
    return result

if __name__ == '__main__':
    user_input = raw_input('Enter a word to Encript\n')
    encripted_result = encryption(user_input)
    print(encripted_result)

