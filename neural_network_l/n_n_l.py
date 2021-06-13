import numpy as np

def basic():
    ### Elements
    elem = 15
    ### Row
    row = 3
    ### Column
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
    ### One dimensional
    a = np.arange(6)
    ### Two dimensional
    b = np.arange(12).reshape(4, 3)
    ### Three dimensional
    c = np.arange(24).reshape(2, 3, 4)

    print('ONE DIMENSIONAL')
    print(a)
    print('TWO DIMENSIONAL')
    print(b)
    print('THREE DIMENSIONAL')
    print(c)