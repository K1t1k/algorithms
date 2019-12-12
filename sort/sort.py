import numpy as np


def quick_sort(seq):
    if len(seq) < 2:
        return seq
    else:
        center = seq[0]
        less = [item for item in seq[1:] if item <= center]
        greater = [item for item in seq[1:] if item > center]
        return quick_sort(less) + [center] + quick_sort(greater)


if __name__ == '__main__':
    seq = np.random.randint(0, 100, 10)
    print(seq)
    print(quick_sort(seq))