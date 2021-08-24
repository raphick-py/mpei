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
    index = 0
    while (len(ASCII) - index) != 0:
        comp = ASCII[index]
        ASCII_code.pop(0)
        for item in ASCII_code:
            residual.append([x - y for x, y in zip(comp, item)])
        ASCII_code.append(comp)
        index = index + 1
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
    m = -1
    start_k = 0
    mass_len = length - 1
    while length != 0:
        start_k = start_k + m + 1
        list_of = []
        for i in range(mass_len):
            list_of.append(sum(ASCII_code[i+start_k]))
        if list_of:
            min_value = max(list_of)
            min_index = list_of.index(min_value)
            result.append(ASCII_code[start_k+min_index])
            m = i
        length = length - 1
    return result


def apply_mask(ASCII_code, mask):
    for k in range(len(ASCII_code)):
        ASCII_code[k] = [a*b for a, b in zip(list(map(int, ASCII_code[k])), mask[k])]
        ASCII_code[k] = [i for i in ASCII_code[k] if i != 0]
    return ASCII_code


if __name__ == "__main__":
    with open('Test_data.txt', 'r') as f:
        list_of_packet = f.readlines()
    list_of_packet = [x[:-1] for x in list_of_packet]  # deleting \n character
    length = len(list_of_packet)
    ASCII_code = Convert_to_ASCII(list_of_packet)
    res = comparasion(ASCII_code)
    normalize = normalization(res)
    mask = counter(normalize, length)
    umask_ASCII = apply_mask(ASCII_code, mask)
    print(Decode_from_ASCII(umask_ASCII))
