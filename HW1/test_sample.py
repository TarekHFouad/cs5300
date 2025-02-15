import pytest
from task1 import printHelloWorld
from task2 import varTypes
from task3 import *
from task4 import *
from task5 import *
import io
import sys

# Task 1 test
def test_output_task1():
    output_captured = io.StringIO() # Creates something to store the output
    sys.stdout = output_captured # This rederects all print statments to the var

    printHelloWorld()
    sys.stdout = sys.__stdout__ #Resets
    assert output_captured.getvalue().strip() == "Hello World!"

# Task 2 test
def test_var_types():
    int_return, float_return, string_return, bool_return = varTypes()
    assert isinstance(int_return, int)
    assert isinstance(float_return, float)
    assert isinstance(string_return, str)
    assert isinstance(bool_return, bool)

    # Task 3 test
def test_task3():
    assert numPosNeg(5) == "Positive" and numPosNeg(0) == "Zero" and numPosNeg(-1) == "Negitive"

    assert primeFinder() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    assert sumTo100() == 5050

    # Task 4 test
def test_task4():
    assert calculate_discount(100, 10) == 90.00
    assert calculate_discount(500, 22) == 390.00
    assert calculate_discount(523, 22.5) == 405.32
    
def test_task5():

    expected_books = [
        ["The Fault in Our Stars", "John Green"],
        ["Far from the Madding Crowd", "Thomas Hardy"],
        ["A Thousand Splendid Suns", "Khaled Hosseini"]
    ]

    assert favBooks() == print(expected_books)