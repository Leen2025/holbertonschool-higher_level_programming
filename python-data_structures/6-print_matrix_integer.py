#!/usr/bin/python3
# 6-print_matrix_integer.py
# Leen Alsaleh <10693@holbertonschool.com>


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")
