#!/usr/bin/python

import os
import sys


def longest_common_substring(S, T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return list(lcs_set)


def label_determine(lop):
    i = 0
    ilop = lop.copy()
    list_of_lcs = list()
    size = len(ilop)
    filik = open("debug.txt", 'a')
    filik.write("========LABEL=======\n")
    while len(ilop) != 0:
        comp = ilop[0]
        filik.write(comp + "\n")
        ilop.pop(0)
        for item in ilop:
            list_of_lcs = list_of_lcs + longest_common_substring(comp, item)
        i = i + 1
    label = max(set(list_of_lcs), key=list_of_lcs.count)
    filik.close()
    return label


def label_pop(label, lop):
    i = -1
    for item in lop:
        i = item.find(label)
        if i != -1:
            break
    print(i)
    lop1 = lop.copy()
    lop.clear()
    n = 0
    for n in range(len(lop1)):
        lop.append(lop1[n][:i] + lop1[n][len(label)+i:])
    return lop


def type_pop(typep, lop):
    i = -1
    for item in lop:
        i = item.find(label)
        if i != -1:
            break
    print(i)
    lop1 = lop.copy()
    lop.clear()
    n = 0
    for n in range(len(lop1)):
        lop.append(lop1[n][:i] + lop1[n][len(label)+i:])
    return lop


if __name__ == "__main__":
    with open('Test_data.txt', 'r') as f:
        list_of_packet = f.readlines()
    list_of_packet = [x[:-1] for x in list_of_packet]
    label = label_determine(list_of_packet)
    list_of_packet = label_pop(label, list_of_packet)
    print("label of packets:", label)
    for i in range(100):
        label = label_determine(list_of_packet)
        print(list_of_packet)
        input()
        list_of_packet = type_pop(label, list_of_packet)
        print("label of packets:",label)
