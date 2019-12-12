from simple_structs.basic.stack import Stack


def list_sum(list_num):
    if len(list_num) == 1:
        return list_num[0]
    else:
        return list_num[0] + list_sum(list_num[1:])


def to_string(x, base):
    convert_string = "0123456789ABCDEF"
    stack = Stack()
    if x < base:
        return convert_string[x]
    else:
        return convert_string[x % base] + to_string(x // base, base)


def remove_white(seq):
    replace_list = [' ', ',', '.', ':', '!', '?', '']
    for i in replace_list:
        seq = seq.replace(i, '')

    return seq


def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


if __name__ == '__main__':
    print(list_sum([1, 2, 3, 4, 5, 6]))
    print(to_string(123456, 10)[::-1])
    print(is_palindrome(remove_white('radar')))
    print(is_palindrome(remove_white('pen')))
    print(is_palindrome(remove_white('reviled did i live, said i, as evil i did deliver')))