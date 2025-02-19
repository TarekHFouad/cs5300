# All file and pytest imports
import pytest
from task1 import *
from task2 import *
from task3 import *
from task4 import *
from task5 import *
from task6 import *
from task7 import *
import io
import sys

# Task 1 test
def testTask1():
    output_captured = io.StringIO() # Creates something to store the output
    sys.stdout = output_captured # This rederects all print statments to the var

    printHelloWorld()
    sys.stdout = sys.__stdout__ #Resets
    assert output_captured.getvalue().strip() == "Hello World!"

# Task 2 test
def testTask2():
    int_return, float_return, string_return, bool_return = varTypes()
    assert isinstance(int_return, int)
    assert isinstance(float_return, float)
    assert isinstance(string_return, str)
    assert isinstance(bool_return, bool)

    # Task 3 test
def testTask3():
    assert numPosNeg(5) == "Positive" and numPosNeg(0) == "Zero" and numPosNeg(-1) == "Negitive"

    assert primeFinder() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    assert sumTo100() == 5050

    # Task 4 test
def testTask4():
    assert calculate_discount(100, 10) == 90.00
    assert calculate_discount(500, 22) == 390.00
    assert calculate_discount(523, 22.5) == 405.32
    
# Task 5 Test
def testTask5():

    expected_books = [
        ["The Fault in Our Stars", "John Green"],
        ["Far from the Madding Crowd", "Thomas Hardy"],
        ["A Thousand Splendid Suns", "Khaled Hosseini"]
    ]

    assert favBooks() == print(expected_books)

    student_dict = studentDatabase()

    assert "Bob" in student_dict
    assert student_dict["Bob"] == 1
    assert student_dict["Tarek"] == 2


#task 6
testfiles = ["task6_read_me.txt" , "task6_read_me2%6.txt"
]
@pytest.mark.parametrize("filename", testfiles)
def testTask6Dynamic(filename):
    try:
        tempString = filename.split("%")
        
        print(tempString)
        if tempString[0] != None:
            tempString = tempString[1].split(".")
            assert wordCount(filename) == tempString
    except:
        assert wordCount(filename) > 0

#Task 7 
def testTask7(): 
    correctOrder = [1, 3, 4, 5, 8, 9]
    assert sortArray() == correctOrder