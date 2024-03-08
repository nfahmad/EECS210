'''
Name of program contained in the file: EECS210_Assignment7.py
Brief description of the program: This is a program for counting the number of ways to distribute distinguishable
                                  objects into distinguishable boxes as per the instructions for Assignment 7.
Inputs: N/A
Output: Print out the exercise number followed by the exercise’s output
All collaborators: Omar Mohammed, Arnav Jain
Other Sources for the Code: Stack Overflow, W3Schools, extr3metech, GeeksForGeeks, "Permutations & Combinations" Canvas Slides
Author's full name: Nabeel Ahmad
Creation date: 11/21/2023
'''

#This module provides access to the mathematical functions defined by the C standard
import math

'''
This function operates with the combination function from the imported math module. 
This function finds the number of ways distinguishable objects can go into distinguishable boxes
Author: Combination
'''
def dOdB(value1,value2):
    #This will return the number of ways a certain number of objects can go into a certain number of boxes
    return math.comb(value1,value2)

'''
This function operates with the combination function from the imported math module. 
This function finds the number of ways indistinguishable objects can go into distinguishable boxes
Author: Combination
'''
def iOdB(value1,value2):
    #This will return the number of ways a certain number of objects can go into a certain number of boxes
    return math.comb(value1+value2-1,value1)

'''
This function operates with the stirling number generation function.
This function finds the number of ways distinguishable objects can go into indistinguishable boxes
Author: Combination
'''
def dOiB(value1,value2):
    #Start of a counter to keep track of the number of ways found
    counter=0
    '''
    This function finds a stirling number of the second kind.
    S(n, k) is the number of ways of splitting “n” items in “k” non-empty sets
    Author: Combination
    '''
    def stirling(value1,value2):
        #If the number of objects is 0 and the number of boxes is 0, return 1
        if value1==0 and value2==0:
            return 1
        #If the number of objects is 0, return 0
        if value1==0:
            return 0
        #If the number of boxes is 0, return 0
        if value2==0:
            return 0
        #If the number of objects equals the number of boxes, return 1
        if value1==value2:
            return 1
        #If the number of objects is less than the number of boxes, return 0
        if value1<value2:
            return 0
        #This will loop through the stirling function through recursion 
        return value2*stirling(value1-1,value2)+stirling(value1-1,value2-1)
    '''
    While the number of boxes is greater than 1, the counter will increase with each way found to put the distinguishable objects into the indistinguishable boxes.
    The number of boxes will also decrease by one every time.
    '''
    while (value2>=1):
        counter+=stirling(value1,value2)
        value2-=1
    #Return the counter value, which returns the number of ways
    return counter

'''
This function operates with the recursive algorithm function found in the "Permutations & Combinations" Canvas Slides.
This function finds the number of ways indistinguishable objects can go into indistinguishable boxes
Author: Combination
'''
def iOiB(value1,value2):
    '''
    This function operates with the recursive algorithm function found in the "Permutations & Combinations" Canvas Slides.
    This function finds the number of ways indistinguishable objects can go into indistinguishable boxes
    Author: Combination
    '''
    def recursiveAlgorithm(value1,value2):
        #If the number of objects equals 0, return 1
        if value1==0:
            return 1
        #If the number of boxes equals 0 or the number of objects is less than 0, return 0
        if value2==0 or value1<0:
            return 0
        #This will loop through the recursiveAlgorithm function through recursion 
        return recursiveAlgorithm(value1-value2,value2)+recursiveAlgorithm(value1,value2-1)
    #This will return the number of ways that were found
    return recursiveAlgorithm(value1,value2)

'''
This function will perform question 1.a
Author: Combination
'''
def question1a():
    #Start of a counter to keep track of the number of ways found
    counter=1
    #For every value in the range specified, the counter will increase based on the number of ways found using the dOdB function
    for value in range(0,4):
        counter*=dOdB(52-5*value,5)
    #Prints the question
    print(f"1.a) How many ways are there to deal 5-card poker hands from a 52-card deck to each of four players?")
    #Return the counter value, which returns the number of ways
    print(f"     {counter} ways")

'''
This function will perform question 1.b
Author: Combination
'''
def question1b():
    #Start of a counter to keep track of the number of ways found
    counter=1
    #For every value in the range specified, the counter will increase based on the number of ways found using the dOdB function
    for value in range(0,4):
        counter*=dOdB(40-10*value,10)
    #Prints the question
    print(f"1.b) A professor packs her collection of 40 issues of a mathematics journal in four boxes with 10 issues per box. How many ways can she distribute the journals if each box is numbered, so that they are distinguishable?")
    #Return the counter value, which returns the number of ways
    print(f"     {counter} ways")

'''
This function will perform question 2.a
Author: Combination
'''
def question2a():
    #Runs the iOdB function and assigns the number of ways found to a variable
    ways=iOdB(10,8)
    #Prints the question
    print(f"2.a) How many ways are there to place 10 indistinguishable balls into 8 distinguishable bins?")
    #Return the ways value, which returns the number of ways
    print(f"     {ways} ways")

'''
This function will perform question 2.b
Author: Combination
'''
def question2b():
    #Runs the iOdB function and assigns the number of ways found to a variable
    ways=iOdB(12,6)
    #Prints the question
    print(f"2.b) How many ways are there to distribute 12 indistinguishable balls into six distinguishable bins?")
    #Return the ways value, which returns the number of ways
    print(f"     {ways} ways")

'''
This function will perform question 3.a
Author: Combination
'''
def question3a():
    #Runs the dOiB function and assigns the number of ways found to a variable
    ways=dOiB(4,3)
    #Prints the question
    print(f"3.a) How many ways can Anna, Billy, Caitlin, and Danny be placed into three indistinguishable homerooms?")
    #Return the ways value, which returns the number of ways
    print(f"     {ways} ways")

'''
This function will perform question 3.b
Author: Combination
'''
def question3b():
    #Runs the dOiB function and assigns the number of ways found to a variable
    ways=dOiB(5,4)
    #Prints the question
    print(f"3.b) How many ways are there to put five temporary employees into four identical offices?")
    #Return the ways value, which returns the number of ways
    print(f"     {ways} ways")

'''
This function will perform question 4.a
Author: Combination
'''
def question4a():
    #Runs the iOiB function and assigns the number of ways found to a variable
    ways=iOiB(6,4)
    #Prints the question
    print(f"4.a) How many ways can you pack six copies of the same book into four identical boxes?")
    #Return the ways value, which returns the number of ways
    print(f"     {ways} ways")

'''
This function will perform question 4.b
Author: Combination
'''
def question4b():
    #Runs the iOiB function and assigns the number of ways found to a variable
    ways=iOiB(5,3)
    #Prints the question
    print(f"4.b) How many ways are there to distribute five indistinguishable objects into three indistinguishable boxes?")
    #Return the ways value, which returns the number of ways
    print(f"     {ways} ways")

#This will run the question1a function
question1a()
#This will run the question1b function
question1b()
#Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
print("_"*120)
#This will run the question2a function
question2a()
#This will run the question2b function
question2b()
#Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
print("_"*120)
#This will run the question3a function
question3a()
#This will run the question3b function
question3b()
#Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
print("_"*120)
#This will run the question4a function
question4a()
#This will run the question4b function
question4b()
