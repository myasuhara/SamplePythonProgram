"""
WEEK1 
"""

# Probelem1

# This prints the result of multiplying 234*456
print("234 * 456 =")
print(234*456)


================
output
===============
C:\Users\Yasuhara\AppData\Local\Programs\Python\Python36-32\python.exe C:/Foothill/Python/Assignment/1/Assignment11.py
234 * 456 =
106704

Process finished with exit code 0


# Problem2

# Assigunment # 1
# caluculate of Pai

def func_pi(n:int):
	result = 0
	for i in range(1,2*n,4):
		result = result + 1/i - 1/(i+2)
		# Pai/4 = 1 - 1/3 + 1/5 - 1/7  + 1/9 - 1/11
	return result

print(func_pi(1000)*4)


=============
Output
=============
C:\Users\Yasuhara\AppData\Local\Programs\Python\Python36-32\python.exe "C:\Program Files\JetBrains\PyCharm 2017.1.1\helpers\pydev\pydevd.py" --multiproc --qt-support --client 127.0.0.1 --port 60554 --file C:/Foothill/Python/Assignment/1/Test.py
pydev debugger: process 8972 is connecting

Connected to pydev debugger (build 171.4163.6)
3.140592653839794


import unittest

"""
Week 2 - 2 Assignment

Write a function that takes the list range(1,10000) and returns the sum of the elements 
that are perfect squares + the sum of the odd numbers + double every number. 
Remember a perfect square is a number whose square root is an integer.
"""

def perfect_squares(n:int):
    # caluculate perfect square
    root = n**(1/2)
    if root==int(root):
        return(n)
    else:
        return(0)

def add_odd_numer(n:int):
    # caluculate odd number
    if (n%2)==1:
        return(n)
    else:
        return(0)

def double_every_numer(n:int):
    # caluculate double every numer
    return(n*2)

def sum_of_3_elements(l:list):
    #
    # add three elements
    #
    s = 0
    for i in range(len(l)):
        m = int(l[i])
        s = s + perfect_squares(m) + add_odd_numer(m) + double_every_numer(m)
    return (s)

class Validation(unittest.TestCase):
    def test_function(self):
        self.assertEqual(perfect_squares(4),4)
        self.assertEqual(add_odd_numer(4),0)
        self.assertEqual(double_every_numer(4),8)

if __name__ == "__main__":
    # execute only if run as a script
    l = list(range(1, 10000))
    # l = list(range(1,5))
    print('Total: ', sum_of_3_elements(l))
    unittest.main()
	
Results:
	
C:\Users\Yasuhara\AppData\Local\Programs\Python\Python36-32\python.exe C:/Foothill/Python/Assignment/Assign2-2.py
.
Total:  125318350
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

Process finished with exit code 0




import re
import csv

"""
Week 2 From the file CSV_Database_of_Last_Names.csv , count the number of Last Names ignoring the
first letter, that have an "a" followed by any number of characters including 0 and 
then followed by an "e" followed by 1 or more characters
"""

def processFile(list_lines):

#
# Last Names ignoring the first letter, that have an "a" followed by any number of characters 
# including 0 and then followed by an "e" followed by 1 or more characters.
# 
# Mach regular expression and cound the number.
#

    count = 0
    for i in range(len(list_lines)):
        m = re.match('^.+a.*e.+', list_lines[i])
        if m:
            count = count + 1

    return count

if __name__== "__main__":
    f = open("CSV_Database_of_Last_Names.csv","r")
    lines = f.readlines()
    f.close()
    print('Total matching number: ',  processFile(lines))
	


import re
import csv

"""
Week 3

From the file CSV_Database_of_Last_Names.csv , count the number of Last Names ignoring the
first letter, that have an "a" followed by any number of characters including 0 and 
then followed by an "e" followed by 1 or more characters
"""

def processFile(list_lines):

#
# Last Names ignoring the first letter, that have an "a" followed by any number of characters 
# including 0 and then followed by an "e" followed by 1 or more characters.
# 
# Mach regular expression and cound the number.
#

    count = 0
    for i in range(len(list_lines)):
        m = re.match('^.+a.*e.+', list_lines[i])
        if m:
            count = count + 1

    return count

if __name__== "__main__":
    f = open("CSV_Database_of_Last_Names.csv","r")
    lines = f.readlines()
    f.close()
    print('Total matching number: ',  processFile(lines))
	


"""
Week4 - 1st assignment
Reads a sequence of integer inputs (data) from the user and then prints the following results:
1.the total of all the inputs
2.the smallest of the inputs
3.the largest of the inputs
4.the number of even inputs
5.the number of odd inputs
6.the average of all of the inputs

You do not know how many numbers the user will want to type in, so you must ask her each time if she has another
number to add to the sequence.
"""

end_of_input = int(0)
first_time = int(1)

total_count = int(0)
min_number = int(0)
max_number = int(0)
accum_number = int(0)
ave_number = int(0)
odd_number = int(0)
even_number = int(0)

def process():

    global total_count
    global min_number
    global max_number
    global accum_number
    global ave_number
    global odd_number
    global even_number
    end_of_input = 0
    first_time = 1

    while end_of_input == 0:
        input_integer = int(input("Please type a number: "))

        if first_time == 1:             # first_time: switch to read the first input to cal min and max value
            min_number = input_integer
            max_number = input_integer
            first_time = 0
        else:
            if min_number > input_integer:
                min_number = input_integer
            if max_number < input_integer:
                max_number = input_integer

        total_count += 1
        accum_number = accum_number + input_integer

        if input_integer%2 == 1:
            odd_number = odd_number + 1
        else:
            even_number = even_number + 1

        ask_end = str(input("Do you have another number to enter (Y or N)?: "))
        if ask_end == 'N':
            end_of_input = 1

    ave_number = float(accum_number)/float(total_count)

process()

if __name__ == "__main__":
    # execute only if run as a script

    print("The total of all the inputs: ", total_count)
    print("The smallest of the inputs: ", min_number)
    print("The largest of the inputs: ", max_number)
    print("The number of even inputs: ", even_number)
    print("The number of odd inputs: ", odd_number)
    print("The average of all the inputs: ", ave_number)




"""
Assignment 4 - 2
In class we saw the maximum of a list formulated recursively now write a function that recursively does the minimum. 

Include at least 3 test cases for each problem, for problem 2 you can create multiple test cases by changing the range.

Hint: some operations just need to be reversed and now use the largest integer possible is given by: sys.maxsize
"""
        
def min(ls:list)->int:
    if len(ls)==0:
        return None
    elif len(ls)==1:
        return ls[0]
    elif len(ls)==2:
        if ls[0]< ls[1]:
            return ls[0]
        else:
            return ls[1]
    else:
        first = ls[0]
        min_of_the_rest = min(ls[1:])#recursive call
        if first < min_of_the_rest:
            return first
        else:
            return min_of_the_rest

if __name__=="__main__":

    print(min([24,12, 14, 29,1, 27]))







"""

Assignment # 6, which includes 6 functions

"""
import random

def swapFirstAndLast(input_list:list):

    # Takes a Python list as parameter and modifies the list parameter
    # by swapping its first and last elements. Does not return anything.
    # Input parameter: a list
    # Returned value: an updated list
    # no input/output

    first_char = input_list[0]
    last_char = input_list[len(input_list) - 1]
    input_list[0] = last_char
    input_list[len(input_list) - 1] = first_char
    return input_list

def shiftRight(input_list:list):

    # Takes a Python list as parameter and modifies the list parameter by shifting
    # all elements in the list to the right and putting the last (rightmost) element
    # in the zeroth position of the list. Does not return anything.
    # Input parameter: a list
    # Returned value: an updated list
    # no input/output

    updated_list = list(input_list)

    for i in range(len(input_list)):

        if i < len(input_list)-1:
            updated_list[i+1]=input_list[i]                 # process far right of the list
        elif i == (len(input_list)-1):
            updated_list[0] = input_list[len(input_list)-1] # right shift

    return updated_list


def double(input_list:list):

    # Takes a Python list as parameter and modifies the list parameter by doubling the value
    # of each element in the list. Does not return anything.
    # Input parameter: a list
    # Returned value: an updated list
    # no input/output

    for i in range(len(input_list)):
        input_list[i] = input_list[i]*2    #  double number

    return input_list

def isSorted(input_list:list):

    # Takes a Python list as parameter and returns True if the list parameter is in sorted order,
    # returns False otherwise. You can assume that the list parameter has only numbers in it.
    # Input parameter: a list
    # Returned value: True or False
    # no input/output

    sorted_list=list(input_list)
    sorted_list.sort()

    if sorted_list==input_list:     # compere sorted list and original one
        return True
    else:
        return False

def replaceEvens(input_list:list):

    # Takes a Python list as parameter and replaces any even elements of the list parameter with a zero.
    # Input parameter: a list
    # Returned value: an updated list
    # no input/output

    for i in range(len(input_list)):

        try:
            if (input_list[i]%2)==0:  # check if a value is even number
                input_list[i] = 0
        except TypeError:
            print(input_list[i], ' is not number')
            continue

    return input_list


def permuteList(input_list: list):

    # Takes a python list as a parameter and returns a random permutation of that list. You can use
    # the algorithm in:Knuth random permutation algorithm
    # (Links to an external site.)Links to an external site.

        population = input_list
        random.seed(a=None, version=2)
        permuted_value = random.sample(population, len(input_list))

        return permuted_value

if __name__== "__main__":

    test1=[1, 2, 3, 4]
    print('swapFirstAndLast Test: ', swapFirstAndLast(test1))

    test2=[1, 2, 3, 4]
    print('shiftRight: ', shiftRight(test2))

    test3=['a', 2, 3, 4]
    print('double test: ', double(test3))

    test4=[4, 2, 3, 1]
    print('isSorted test: ', isSorted(test4))

    test5=['a', 4, 3, 3]
    print('replaceEvens test: ', replaceEvens(test5))

    test6=[1, 2, 3, 4, 5, 6]
    print(permuteList(test6))
    test6=[1, 2, 3, 4, 5, 6]
    print(permuteList(test6))


"""

Assignment # 7-1

Write a program that asks the user for a filename, opens the file and reads through the file just once before 
reporting back to the user the number of characters (including spaces and end of line characters), 
the number of words, and the number of lines in the file.

If the user enters the name of a file that doesn't exist, your program should give her as many 
tries as she needs in order to type a valid filename. Obtaining a valid filename from the 
user is a common operation, so start by writing a separate, reusable function that repeatedly 
asks the user for a filename until she types in a file that your program is able to open. 
This separate, reusable function will then return the opened file as its returned value. 
You will be able to reuse this function later in the quarter.

"""

def space_count(lines):
    # Count space
    spc_count=0
    for line in lines:
        if line.isspace():
            spc_count += 1
    return spc_count

def eol_count(lines):
    # Count end of line character
    eol_count=0
    for line in lines:
        if line[-1] == '\n':
            eol_count += 1
    return eol_count

def words_count(x):
    # Count line number
    return len(x.split())

def line_count(x):
    # Couont line number
    return len(x.splitlines())

def input_validation():
    # Prompt to enter a file name with its extension
    loop_continue=True
    while loop_continue:
        input_file_name = input('Enter test file name including its extension: ')
        if input_file_name == filename:
            loop_continue = False
        else:
            print("A specified file name does not exist.")

def read_file(filename):
    f = open(filename)
    x = f.read()
    f.close()
    return x

if __name__== "__main__":

    filename = "data71.txt"

    input_validation()
    x=read_file(filename)

    print("========================================")
    print("Word count is " + str(words_count(x)) + ".")
    print("Line count is " + str(line_count(x)) + ".")
    print("Space count is " + str(space_count(x)) + ".")
    print("End of line count is " + str(eol_count(x)) + ".")


"""
Results:

------------------------------------------------------------------------------------------------------------
C:\ProgramData\Anaconda3\python.exe C:/Users/myasuhara/Documents/Foothill/Python/Assignment/7/assignment71.py
Enter test file name including its extension: data71.txt
========================================
Word count is 6.
Line count is 4.
Space count is 6.
End of line count is 3.

Process finished with exit code 0
------------------------------------------------------------------------------------------------------------

Logic:

1. a test file, data71.txt exists in the same directory as of the program
2. prompt to enter file name
3. check if the file name matches with data71.txt
4. read data71.txt
5. calucuate counters and print them


"""



"""
Assignment # 7-2

Now expand the program to be object Oriented, create a file class that contains variables/properties for 
number of characters, number of spaces, lines, words etc.

• The file class should implement all these properties/variables
• The file should also implement the necessary methods to read the number of characters, number of words, spaces, lines etc.
• Create a directory class that will contain a list of file objects, with an appropriate variable name.
• The directory class will be initialised/or have a constructor which accepts the directory path
• The directory class will contain a method/function called scan directory that will return the list of file 
objects in directory initialised by the path above. With the file objects properties/variables being 
filled with the number of lines, spaces, characters words etc.

class directory
  def inputValidate: validate path entered by user
class fileProcess
  def read_file: read input file
  def space_count: Count space number
  def eol_count: Count end of line character
  def words_count: Count line number
  def line_count: Couont line number
"""

import os

class Directory():
    def __int__(self):
        self.input_path=''

    def inputValidate(self):    # prompt to enter path
        loop_continue = True
        while loop_continue:
            self.input_path = input('Enter the path: ')
            #print(self.input_path)
            if os.path.exists(self.input_path):
                print('Input path exists!!!')
                loop_continue = False
            else:               # if the path does not exist
                print('The specified path does not exist.')
        return self.input_path

class FileProcess():

    def __int__(self, file_path_name):
        self.lines=''
        self.file_path_name=file_path_name

    def read_file(self, self_file_path_name):   # read file
        originals=list(self_file_path_name)
        updated_list=[]
        updated_string=''
        for original in originals:
            if original=="\\":
                updated_list.append('\\')
                updated_list.append('\\')
            else:
                updated_list.append(original)
        updated_string=''.join(updated_list)    # updated_string inclues like "c:\\temp"

        f = open(updated_string)                # read file
        self.lines = f.read()
        f.close()

    def space_count(self):
        # Count space
        spc_count=0
        for line in self.lines:
            if line.isspace():
                spc_count += 1
        print("  Space count is " + str(spc_count) + ".")

    def eol_count(self):
        # Count end of line character
        eol_count=0
        for line in self.lines:
            if line[-1] == '\n':
                eol_count += 1
        print("  End of line count is " + str(eol_count) + ".")

    def words_count(self):
            # Count line number
            print("  Word count is " + str(len(self.lines.split())) + ".")

    def line_count(self):
            # Couont line number
            print("  Line count is " + str(len(self.lines.splitlines())) + ".")

if __name__== "__main__":
    my_dir=Directory()
    input_path=my_dir.inputValidate()
    for filename in os.listdir(input_path):
        file_path_name = os.path.join(input_path, filename)
        my_file = FileProcess()
        print('============================================')
        print("File path and name: " + file_path_name)
        print('============================================')
        my_file.read_file(file_path_name)
        my_file.space_count()
        my_file.eol_count()
        my_file.words_count()
        my_file.line_count()

"""
Test Results:

-------------------------------------------------------------------------------------------------------------
C:\ProgramData\Anaconda3\python.exe C:/Users/myasuhara/Documents/Foothill/Python/Assignment/7/assignment74.py
Enter the path: c:\temp
Input path exists!!!
============================================
File path and name: c:\temp\data710.txt
============================================
  Space count is 6.
  End of line count is 3.
  Word count is 6.
  Line count is 4.
============================================
File path and name: c:\temp\data711.txt
============================================
  Space count is 10.
  End of line count is 1.
  Word count is 11.
  Line count is 2.

Process finished with exit code 0

--------------------------------------------------------------------------------
Explain the logic:

1. when prompted, enter 'c:\temp', where two text files, data710.txt and data711.txt, exist
2. read each file
2. print space, eof, word, and line counts

"""


"""

Assignment #9

"""

class PlayingCard(object):
    # a class where one object of the class represents one playing card.
    # Input parameter: rank as init and suit as string for input parameter.
    # rank is a number in the range 1-13 indicating the ranks Ace through King,
    # and suit is a single character "d" "c", "h", or "s" indicating the suit
    # (diamonds, clubs, hearts, or spades). This method creates a card of rank and suit.

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_full = ''
        self.suit_full = ''
        self.bjvalue = ''

    def __str__(self):
        # Output: concatenate rank and suit

        rep = self.rank_full + ' of ' + self.suit_full
        return rep

    def getRank(self):
        # input as rank (init type), and convert it to word

        rank_Conversion = {
            1:  'Ace',
            2:  'Two',
            3:  'Three',
            4:  'Four',
            5:  'Five',
            6:  'Six',
            7:  'Seven',
            8:  'Eight',
            9:  'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
        }

        for num, self.rank_full in rank_Conversion.items():
            if num == self.rank:
                break

        return self.rank_full

    def getSuit(self):
        # input as suit, and convert to full word

        suit_Conversion = {
            'd':  'Diamonds',
            'c':  'Clubs',
            'h':  'Hearts',
            's':  'Spades',
        }

        for sui, self.suit_full in suit_Conversion.items():
            if sui == self.suit:
                break

        return self.suit_full

    def bjValue(self):
        # input as rank, and convert to black jack value

        if self.rank >= 1 and self.rank <= 10:
            self.bjvalue = str(self.rank)
        elif self.rank >= 11 and self.rank <= 13:
            self.bjvalue = '10'
        else:
            pass

        return self.bjvalue

if __name__== "__main__":

    c1 = PlayingCard(rank=5, suit="c")
    print('--------------------------------------------')
    print(c1.getRank())
    print(c1.getSuit())
    print(c1.bjValue())
    print(c1)

    c2 = PlayingCard(rank=13, suit="h")
    print('--------------------------------------------')
    print(c2.getRank())
    print(c2.getSuit())
    print(c2.bjValue())
    print(c2)

"""
Test Results:

C:\ProgramData\Anaconda3\python.exe C:/Users/myasuhara/Documents/Foothill/Python/Assignment/9/assignment91.py
--------------------------------------------
Five
Clubs
5
Five of Clubs
--------------------------------------------
Thirteen
Hearts
10
Thirteen of Hearts

Process finished with exit code 0
"""