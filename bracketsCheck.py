"""Program takes a set of brackets as input and it will print
    whether the brackets are balanced or not"""


from a import Stack


def checking(input_string):
    s = Stack()
    brackets = [('(', ')'), ('[', ']'), ('{', '}')]

    for char in input_string:
        for br in brackets:
            if char is br[0]:
                s.push(char)
            elif char is br[1]:
                if s.is_empty():
                    return False
                else:
                    temp = s.pop()
                    if temp is not br[0]:
                        return False

    if s.is_empty():
        return True
    else:
        return False

if __name__ == '__main__':
    user_input = raw_input('Enter a series of brackets\n')
    if checking(user_input):
        print('Brackets are balanced\n')
    else:
        print('Brackets are imbalanced\n')

