from basic.deque import Deque


def isPalindrom(word):
    deque = Deque()
    for w in word:
        deque.addFront(w)
    while deque.size()>=2:
        f, r = deque.removeFront(), deque.removeRear()
        if f != r:
            return False
    return True
