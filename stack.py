"""Stack Implementation Using List"""


class Stack:

    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        try:
            return self.stack_list.pop()
        except IndexError:
            return '\nStack is Empty, nothing to pop\n'

    def is_empty(self):
        if len(self.stack_list):
            return False
        else:
            return True

    def size(self):
        return len(self.stack_list)

if __name__ == '__main__':
    obj = Stack()
    while True:

        print('\nPress numbers for operation')
        user_input = input('1 : push 2: pop 3 : is empty?? 4: size 5 : exit\n')

        if user_input is 1:
            obj.push(input('\nEnter a value to push to stack\n'))

        elif user_input is 2:
            print(obj.pop())

        elif user_input is 3:

            if obj.is_empty():
                print('Stack is Empty')
            else:
                print('Stack is not Empty')

        elif user_input is 4:
            print('\nSize = %d' % obj.size())

        elif user_input is 5:
            break

        else:
            print('\nInvalid input, try again\n')

