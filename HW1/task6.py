import pytest

testfiles = ["task6_read_me.txt", "task6_read_me2%5.txt"
]

def wordCount(filename):
    with open(filename, "r") as file:
        return len(file.read().split())

print("Word Count:", wordCount("/home/student/cs5300/HW1/task6_read_me.txt"))

@pytest.mark.parametrize("filename", testfiles)
def testWordCountDynamic(filename):
    try:
        tempString = filename.split("%")
        
        print(tempString)
        if tempString[0] != None:
            tempString = tempString[1].split(".")
            print(f"{wordCount(filename)} == {tempString}")
    except:
        assert wordCount(filename) > 0

#testWordCountDynamic(filename) 