#!/usr/bin/python

from dataset_properties import *
import uuid
import random


class Dataset(object):
    """Here will be description"""
    def __init__(self):
        self.package = packet_label[0] + random.choice(packet_type) + str(uuid.uuid4())


def file_creation():
    myfile = open('Test_data.txt', 'w')
    myfile.truncate()
    for i in range(100):
        test = Dataset()
        myfile.write(test.package + "\n")
    myfile.close()
file_creation()
