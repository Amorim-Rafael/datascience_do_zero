# VECTORS-----------------------------------------------------
import re, math, random # regexes, math functions, random numbers
# import matplotlib.pyplot as plt # pyplot
from collections import defaultdict, Counter
from functools import partial, reduce

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    # result = vectors[0]
    # for vector in vectors[1:]:
    #     result = vector_add(result, vector)
    # return result
    # or
    # return reduce(lambda x, y: x+y, vector)
    # or
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    """c é um numero, v é um vetor"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """acumula o vetor cujo o i-esimo elemento seja a media dos 
       i-esimos elementos dos vetores inclusos"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# if __name__ == '__main__':
#     v1 = [2, 1]
#     v2 = [1, 2]
#     v3 = vector_add(v1, v2)
#     print(v3)

# MATRIX-----------------------------------------------------

A = [[1,2,3],
    [4,5,6]]

B = [[1,2],
    [3,4],
    [5,6]]

def shape(M):
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols


def get_row(M, i):
    return M[i]
    

def get_column(M, j):
    return [M_i[j] for M_i in M]

# entry_fn é o nome da função no qual vai ser chamada, passando cada item da linha e coluna
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) 
            for j in range(num_cols)]
            for i in range(num_rows)]

def is_diagonal(i, j):
    return 1 if i == j else 0

if __name__ == '__main__':
    # print(shape(A))
    # print(get_row(A, 0))
    # print(get_column(B, 1))
    print(make_matrix(5, 5, is_diagonal))