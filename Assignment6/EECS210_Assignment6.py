'''
Name of program contained in the file: EECS210_Assignment6.py
Brief description of the program: Given a partially completed Sudoku puzzle, 
                                  this program will fill in the remaining spaces and solve the puzzle using depth-first search with backtracking.
Inputs: puzzle1.txt, puzzle2.txt, puzzle3.txt, puzzle4.txt, puzzle5.txt
Output: Print out the exercise number followed by the exercise’s output
All collaborators: N/A
Other Sources for the Code: Stack Overflow, W3Schools, GeeksForGeeks
Author's full name: Nabeel Ahmad
Creation date: 11/06/2023
'''

'''
This function will print the current sudoku board
Author: Combination
'''
def printSudoku(board):
    #This will iterate through every row on the board
    for row in board:
        #This will print the board in an easy and readable format
        print(" ".join(row))

'''
This function will return a boolean value after determining if the attempted move is valid
Author: Combination
'''
def determineValidMove(board, row, column, potentialNum):
    #This will check if the potential number is already in the spot by iterating through the board
    for i in range(9):
        #If the potential number is already in the current row or current column, it will return false
        if board[row][i] == potentialNum or board[i][column] == potentialNum:
            return False
    #This will check if the number is already in the 3x3 block's row
    blockRow = 3 * (row // 3)
    #This will check if the number is already in the 3x3 block's column
    blockColumn = 3 * (column // 3)
    '''
    Start of a nested for loop where the outer loop (for i in range(3):) will run after the inner loop has been iterated through.
    This will help to identify if the attempted move is valid
    '''
    for i in range(3):
        '''
        The inner loop (for j in range(3):) will iterate before progressing to the outer loop. 
        This will help to identify if the attempted move is valid
        '''
        for j in range(3):
            #If the number is in the block, then it will return false
            if board[blockRow + i][blockColumn + j] == potentialNum:
                return False
    return True

'''
This function will add the missing values to the sudoku board using depth-first search with backtracking
Author: Combination
'''
def solveSudoku(board):
    '''
    Start of a nested for loop where the outer loop (for row in range(9):) will run after the inner loop has been iterated through.
    This will help to add the missing values to the sudoku board
    '''
    for row in range(9):
        '''
        The inner loop (for column in range(9):) will iterate before progressing to the outer loop. 
        This will help to add the missing values to the sudoku board
        '''
        for column in range(9):
            #If the current spot is empty, then it will try using potential numbers from 1 to 9
            if board[row][column] == "_":
                #Initiates a for loop to determine if the potential number is valid to be placed in the current spot
                for num in map(str, range(1, 10)):
                    #If the move is valid, it will put the number in the spot
                    if determineValidMove(board, row, column, num):
                        board[row][column] = num
                        #This will recursively call the solveSudoku function for the next spot on the board
                        if solveSudoku(board):
                            return True
                        #If there is no solution, it will return the spot to empty with an underscore
                        board[row][column] = "_"
                return False
    return True

'''
This function opens the file and makes it usable in the program, and also prints the results for each puzzle
Author: Combination
'''
def main(input_file):
    #This will open the incoming file
    with open(input_file, 'r') as file:
        #This will return all lines in the file, as a list where each line is an item in the list object
        lines = file.readlines()
        #This will create a list and remove the spaces 
        board = [list(line.strip().replace(" ", "")) for line in lines]
        #Prints a line to tell the user the puzzle below is unsolved
        print("Unsolved Sudoku puzzle:")
        #This will print the unsolved sudoku puzzle
        printSudoku(board)
        #Prints a space for readability purposes
        print(" ")
    #If the sudoku board has a solution, the solution is printed
    if solveSudoku(board):
        #Prints a line to tell the user the puzzle below is solved
        print("Solved Sudoku puzzle:")
        #This will print the solved sudoku board
        printSudoku(board)
    #If the sudoku board has no solution, then it prints a line indicating so
    else:
        #Prints an indication telling the user there was no solution found
        print("No solution found")

'''
This function will pass the input files to the main function for all puzzles.
This function will also structure the output in the correct format
Author: Combination
'''
def inputs():
    #Assigns input1 to the first puzzle
    input1 = "puzzle1.txt"
    #Assigns input2 to the second puzzle
    input2 = "puzzle2.txt"
    #Assigns input3 to the third puzzle
    input3 = "puzzle3.txt"
    #Assigns input4 to the fourth puzzle
    input4 = "puzzle4.txt"
    #Assigns input5 to the fifth puzzle
    input5 = "puzzle5.txt"
    #This will print an indication of what puzzle is being solved
    print("puzzle1.txt\n")
    #This will pass the puzzle1.txt file into the main function
    main(input1)
    #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)
    #This will print an indication of what puzzle is being solved
    print("puzzle2.txt\n")
    #This will pass the puzzle2.txt file into the main function
    main(input2)
    #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)
    #This will print an indication of what puzzle is being solved
    print("puzzle3.txt\n")
    #This will pass the puzzle3.txt file into the main function
    main(input3)
    #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)
    #This will print an indication of what puzzle is being solved
    print("puzzle4.txt\n")
    #This will pass the puzzle4.txt file into the main function
    main(input4)
    #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)
    #This will print an indication of what puzzle is being solved
    print("puzzle5.txt\n")
    #This will pass the puzzle5.txt file into the main function
    main(input5)
    #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)

#This will run the inputs function which will then run the main function using the corresponding input files
inputs()
