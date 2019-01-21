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

import re, math, random # regexes, math functions, random numbers
import matplotlib.pyplot as plt # pyplot

if __name__ == '__main__':
    v1 = [2, 1]
    v2 = [1, 2]
    v3 = vector_add(v1, v2)
    print(v3)