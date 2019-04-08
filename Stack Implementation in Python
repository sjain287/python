'''
Stack Program
# p push
# o pop
# l list
# k peek
'''


def isEmpty(lst):
    if len(lst) == 0:
        return True


def push(lst, elem):
    lst.append(elem)


def pop(lst):
    if isEmpty(lst):
        print('Stack is empty')
    else:
        return lst.pop()


def list_elem(lst):
    if isEmpty(lst):
        print("Stack is Empty")
    else:
        for i in lst:
            print(i, end=" ")
        print()


def peek(lst):
    if isEmpty(lst):
        print("Stack is Empty")
    else:
        return lst[-1]


stack = []
flag = True

while flag:
    print('List of stack operation'.center(80, '*'))
    print('p-Push'.center(50, ' '))
    print('o-Pop'.center(50, ' '))
    print('l-List'.center(50, ' '))
    print('k-Peek'.center(50, ' '))
    print('q-Quit'.center(50, ' '))
    ip = input('Enter your choice: ')

    if ip == 'p':
        elem = input("Enter an element to push to the stack: ")
        push(stack, elem)
    elif ip == 'o':
        elem = pop(stack)
        print(f'Poped element is {elem}')
    elif ip == 'l':
        print('Elements in stack:')
        list_elem(stack)
    elif ip == 'k':
        print(f'Peek value is {peek(stack)}')
    elif ip == 'q':
        print('Bye!')
        break
    else:
        print('Invalid input')
        break
