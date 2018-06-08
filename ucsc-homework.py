'''
Question 1

Use the formula

Pn = P0*(1+r)^n

where P0 is the principal amount, Pn is the compounded principal,  
r is the rate of interest and n is the number of year.

Assume r = 10% and n = 1 to 20, create a Python list that will store 
the value of (1+r)^n where n = 1 to 20.  Subsequently, take an input from 
the command line for the value of P0 and calculate Pn all values of n.  
Repeat this process until a special key is used to quit the program. 
'''
r = 10/100.0 # Divide by float, to avoid integer division
n = range(1, 20)
nr = [pow(1+r, i) for i in n]
print nr
while True:
    P0 = raw_input('Enter the initial principal: ')
    if P0.lower() == 'q':
        break
    P0 = float(P0)
    P = [P0*i for i in nr]
    print P
	
	
'''
Homework 1 - Question 2

Implement an encoding scheme.

A string 
WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW 
has 67 characters. Write a Python program 
with a function called getcompressed to convert this string to 
12W1B12W3B24W1B14W. The new string is created
by calculating the number of times a characters appears consecutively and
placing the character next to it. The new string only needs 18 character,
thus compressing the original string by 73%.
'''

orig_string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

def getcompressedstring(inputstring):
    firstitem = orig_string[0]
    #print firstitem
    count = 0
    finalstring = []
    for i in range(len(orig_string)-1):
        if orig_string[i] == firstitem:
            count = count+1 
        else:
            newstring = '%d%s'%(count,firstitem)
            finalstring.append(newstring)
            firstitem = orig_string[i]
            #print newstring, firstitem
            count = 1
    
    count = count+1 
    newstring = '%d%s'%(count,firstitem)
    finalstring.append(newstring)
    return ''.join(finalstring)

print getcompressedstring(orig_string)


'''
Homework 2 - Question 1

Create a base/parent class called 'InterestCalculator'. Create a child class 
called 'CICalculator'. CI stands for compound interest.  The 'CICalculator' 
class will have only one parent, the 'InterestCalculator'. Create a child 
class called 'SICalculator'. The 'SI' class will have only one parent, 
the 'InterestCalculator'. SI stands for simple interest. 
The parent class needs to have an __init__ method, 
that will initialize all the values needed for calculating and storing interest.

The child class 'CICalculator' and 'SICalculator' must implement 
'calcfinalval' method that will calculate the final value for each case.


Once all classes have been defined, the call to calculate and print 
the final value must follow the code below.

The arguments to the __init__ method are: number of years, interest rate 
and initial principal.

c = CICalculator(2,0.1,1000)
c.calcfinalval()
print c.finalval

s = SICalculator(2,0.1,1000)
s.calcfinalval()
print s.finalval
'''

class InterestCalculator:
    def __init__(self,years,rate,initialval):
        self.years = years
        self.rate = rate
        self.initialval = initialval
        self.finalval = 0 

# finalval = initialval(1 + rate*years)
class SICalculator(InterestCalculator):
    def calcfinalval(self):
        self.finalval = self.initialval *(1+self.rate*self.years)

class CICalculator(InterestCalculator):
    def calcfinalval(self):
        self.finalval = self.initialval *((1+self.rate)**self.years)

c = CICalculator(2,0.1,1000)
c.calcfinalval()
print c.finalval

s = SICalculator(2,0.1,1000)
s.calcfinalval()
print s.finalval

'''
Homework Question 2

A stack follows LIFO (last-in, first-out). LIFO is the case where the last  
element added is the first element that can be retrieved. 
Consider a list with values [4,6,9]. Create a class called Sclass with 
functions sadd and sretrieve to add and pop elements from the list 
in LIFO order respectively. After each function call, print the contents 
of the list. Add 12 to the queue and then follow the LIFO rules and 
pop elements until the list is empty. 
'''

class Sclass:    
    def __init__(self,a):
        self.a = a
        
    def sadd(self,b):
        self.a.extend([b])
        
    def sretrieve(self):
        while(len(self.a) > 0):
            print self.a.pop(-1)
            print self.a
                                     
a = [4,6,9]
c = Sclass(a)
c.sadd(12)
c.sretrieve()

"""
Homework 3 - 1
"""
class Quadratic(object):

    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c      

    def __str__(self):
        return ('%dx^2 + %dx + %d' % (self.a, self.b, self.c))

    def __add__(self,other):
        sumA = self.a + other.a
        sumB = self.b + other.b
        sumC = self.c + other.c
        return(Quadratic(sumA, sumB, sumC))
    
    def __sub__(self,other):
        diffA = self.a - other.a 
        diffB = self.b - other.b
        diffC = self.c - other.c 
        return(Quadratic(diffA, diffB, diffC))

    def __eq__(self,other):
        return(self.a == other.a and self.b == other.b and self.c == other.c)

Q1 = Quadratic(3,8,-5)
Q2 = Quadratic(2,3,7)
quadsum = Q1 + Q2
quaddiff = Q1 - Q2
print('quadsum  = Q1 + Q2 = ', quadsum)
print('quaddiff = Q1 - Q2 = ', quaddiff)
print(Q1 == Q1)
print(Q1 == Q2)

"""
Homework 3 - 2

Create a class called WordCounter with the following methods.

def __init__(self,filename) where filename is the name of the text file, 'red-headed-league.txt'. 
This function should read the text file

def removepunctuation(self) must remove all the punctuations and leave only alphabets 
and numbers in each word

def findcount(self) must count the frequency of each word and store it in a instance 
variable called countdict

def writecountfile(self,csvfilename) writes the content of the countdict variable to 
a csv file with two columns. The first column is the word and second column is the count.
"""
import csv

class WordCounter(object):
    
    textG = ''
    countdictG = {}
    
    def __init__(self,filename):
        self.filename = filename

    def removepunctuation(self):
        with open(self.filename, "r") as f:
            text = f.read()
            # remove punctuation
            for char in '-.,\n':
                text = text.replace(char, ' ')
            text = text.lower()
            
            WordCounter.textG = text
            
            return text

    def findcount(self):
        word_list = WordCounter.textG.split()
        
        countdict = {}
        
        # cound words and add them in dictionary
        for word in word_list:
            if word not in countdict :
                countdict [word] = 0 
            countdict [word] += 1
        
        WordCounter.countdictG = countdict
        
        return countdict
    
    def writecountfile(self,csvfilename):

        with open(csvfilename, 'w') as fo:
            wo = csv.writer(fo)    
            wo.writerows(WordCounter.countdictG.items()) 
    
a = WordCounter('red-headed-league.txt')
print (a.removepunctuation())
print (a.findcount())
a.writecountfile('wordcount.csv')





