#!/usr/bin/python
import os

def func1():

    file = os.open("test_case1.txt", os.O_RDWR)
    os.write(file, "Hello World \n")
    os.close(file)

def func2():
    file = open("../tests/test_case1.txt", "r")
    data = file.read()
    file.close()

def func3():
    file = os.open("test_case1.txt", os.O_RDWR)
    data = os.read(file, 1000)
    os.close(file)

if __name__ == '__main__':

    func1()
    func2()
   # func3()
