#!/usr/bin/python
import sys

def InputTwoList():
    first_list = list(map(int, input("1st list: ").replace('[', ' ').replace(']', ' ').replace(',', ' ').strip().split()))
    second_list = list(map(int, input("2nd list: ").replace('[', ' ').replace(']', ' ').replace(',', ' ').strip().split()))
    return first_list, second_list

def union(first_list, second_list):
    result_list = list(set(first_list) | set(second_list))

    print("=> union ", result_list)

def intersection(first_list, second_list):
    result_list = list(set(first_list) & set(second_list))

    print("=> intersection ", result_list)
