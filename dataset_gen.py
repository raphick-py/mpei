#!/usr/bin/python

from dataset_properties import *
import uuid
import random
import string


def get_random_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        return result_str

class Dataset(object):
    """Here will be description"""
    def __init__(self):
        self.package = packet_label[0] + random.choice(packet_type) + get_random_string(46)


def file_creation():
    myfile = open('Test_data.txt', 'w')
    myfile.truncate()
    for i in range(300):
        test = Dataset()
        myfile.write(test.package + "\n")
    myfile.close()
file_creation()
