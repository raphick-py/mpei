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


with open('Test_data.txt', 'r') as f:
    list_of_packet = f.readlines()
comp = list_of_packet[0]        # Proceeding list of possible labels
remain = list_of_packet.pop(0)  # First item comparing to all other
list_of_lcs = list()		# most common from lsc will be label
for i in list_of_packet:
    list_of_lcs = list_of_lcs + longest_common_substring(comp, i)
label = max(set(list_of_lcs), key=list_of_lcs.count)
print("label of packets:", label)
