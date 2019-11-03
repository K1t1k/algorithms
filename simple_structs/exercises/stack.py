from basic.stack import Stack

def revers_string(mystr):
    stack = Stack()
    for i in mystr:
        stack.push(i)
    result = ''
    while not stack.isEmpty():
        result += stack.pop()
    return result


def par_checker(seq):
    stack = Stack()
    for i in seq:
        if i == '(':
            stack.push(i)
        elif i == ')' and stack.isEmpty():
            return False
        elif i == ')':
            stack.pop()
    return True if stack.isEmpty() else False


def par_checker2(seq):
    stack = Stack()
    open_ = '([{'
    close_ = ')]}'
    for i in seq:
        if stack.isEmpty() and i in close_:
            return False
        elif i in open_:
            stack.push(i)
        elif i in close_ and open_.index(stack.peek()) == close_.index(i):
            stack.pop()
        else:
            stack.push(i)
    return True if stack.isEmpty() else False


def convert_2(x):
    dec = x
    stack = Stack()
    while dec > 0:
        stack.push(dec % 2)
        dec = dec // 2
    result = ''
    while not stack.isEmpty():
        result += str(stack.pop())
    return result


def base_convert(x, base):
    digits = '0123456789ABCDEF'
    dec = x
    stack = Stack()
    while dec > 0:
        stack.push(dec % base)
        dec = dec // base
    result = ''
    while not stack.isEmpty():
        result += digits[stack.pop()]
    return result
