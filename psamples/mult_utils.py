#!/usr/bin/env python

''' allmult.py - multiply each element in an array by all others'''


def mult_half(data):
    result = [1] * len(data)

    for i in range(1, len(data) - 1):
        result[i] *= data[i - 1]
        for j in range(i + 1, len(data) - 1):
            result[j] = result[i]

    return result


def all_mult(data):
    ''' return a list where each element is the product of all others '''
    if data == None or len(data) <= 1:
        return data

    result1 = mult_half(data)
    result2 = mult_half(data[::-1])[::-1]

    return [result1[i] * result2[i] for i in range(len(result1))]

