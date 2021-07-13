#!/usr/bin/python
import re


def find_sum(str1):
    return sum(map(int, re.findall(('\d+', str1))))


def Convert_to_ASCII(lop):
    ASCII_code = []
    for packet in lop:
        ASCII = [ord(character) for character in packet]
        ASCII_code.append(ASCII)
    return ASCII_code


def Decode_from_ASCII(ASCII):
    begin = []
    for line in ASCII:
        line1 = [chr(character) for character in line]
        begin.append("".join(line1))

    return begin


def comparasion(ASCII):
    residual = list()
    ASCII_code = ASCII.copy()
    while len(ASCII_code) != 0:
        comp = ASCII_code[0]
        ASCII_code.pop(0)
        for item in ASCII_code:
             residual.append([x - y for x, y in zip(comp, item)])
    return residual


def normalization(ASCII_code):
    for item in ASCII_code:
        for index, character in enumerate(item):
            if character != 0:
                item[index] = 0
            elif character == 0:
                item[index] = 1
    return ASCII_code


def counter(ASCII_code, length):
    result = list()
    i = 0
    m = 0
    while length != 0:
        start_k = m
        list_of = []
        for i in range(length-1):
            list_of.append(sum(ASCII_code[i]))
        if list_of:
            min_value = max(list_of)
            min_index = list_of.index(min_value)
            result.append(ASCII_code[start_k+min_index])
            m = i
        length = length - 1
    return result


def apply_mask(ASCII_code, mask):
    for k in range(len(ASCII_code)):
        ASCII_code[k] = [a*b for a, b in zip(list(map(int, ASCII_code[k])), mask[k-1])]
        print("==========",ASCII_code)
        ASCII_code[k] = [i for i in ASCII_code[k] if i != 0]
    return ASCII_code


if __name__ == "__main__":
    with open('Test_data.txt', 'r') as f:
        list_of_packet = f.readlines()
    list_of_packet = [x[:-1] for x in list_of_packet]  # deleting \n character
    length = len(list_of_packet)
    ASCII_code = Convert_to_ASCII(list_of_packet)
#    print(ASCII_code)
    res = comparasion(ASCII_code)
#    print(res)
    normalize = normalization(res)
#    print(normalize)
    mask = counter(normalize, length)
#    print("========mask=============")
    print(mask)
    umask_ASCII = apply_mask(ASCII_code, mask)
    print("========final=============")
    print(umask_ASCII)
#    print("=======decode=============")
    print(Decode_from_ASCII(umask_ASCII))
