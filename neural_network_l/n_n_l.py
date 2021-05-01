import numpy as np

def basic():
    ### ELEMENTS
    elem = 15
    ### ROW
    row = 3
    ### COLUMN
    column = 5
    a = np.arange(elem).reshape(row, column)
    print(a)

    print(a.shape)
    print(a.ndim)
    print(a.dtype.name)
    print(a.itemsize)
    print(a.size)
    print(type(a))

    print('Array named b')
    b = np.array([6, 7, 8])
    print(b)
    print(type(b))

def dimensional():
    ### ONE DIMENSIONAL
    a = np.arange(6)
    ### TWO DIMENSIONAL
    b = np.arange(12).reshape(4, 3)
    ### THREE DIMENSIONAL
    c = np.arange(24).reshape(2, 3, 4)

    print('ONE DIMENSIONAL')
    print(a)
    print('TWO DIMENSIONAL')
    print(b)
    print('THREE DIMENSIONAL')
    print(c)