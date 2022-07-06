#!/usr/bin/python3

from unittest import result


def uniq_add(my_list=[]):
    result = 0
    for x in set(my_list):
        result += x

    return (result)
