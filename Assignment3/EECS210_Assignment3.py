'''
Name of program contained in the file: EECS210_Assignment3.py
Brief description of the program: This program's objective is to perform various set operations on the relations R1 = {(1,1), (2,2), (3,3)} and R2 = {(1,1), (1,2), (1,3), (1,4)} and print them.
                                  This program's objective is to find a composition of two relations. Where, R is the relation from A = {1, 2, 3} to B = {1, 2, 3, 4} 
                                  with R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}. And, S is the relation from B = {1, 2, 3, 4} to C = {0, 1, 2} 
                                  with S = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)}. And print the composition.
                                  This program's objective is to also find a composition of R^2 for R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}. And print the composition.
                                  And determine if for the relation R = {(x, y) | x + y = 0} on the set {-10, ..., -1, 0, 1, ..., 10}, R is reflexive, symmetric, antisymmetric, and transitive.
                                  And also show R as an ordered pair.
Inputs: None
Output: Print out the exercise number along with a description of the exercise, followed by the exercise’s output
All collaborators: Omar Mohammed
Other Sources for the Code: Stack Overflow, GeeksforGeeks, Coding Ninjas, "Sets & Set Operations" Canvas Slides, "Relations" Canvas Slides, "Properties of Relations" Canvas Slides
Author's full name: Nabeel Ahmad
Creation date: 09/27/2023
'''

'''
This method involves the operation R1 ∪ R2 and determining the set of relations that are unique from both R1 and R2 and printing them.
Author: Combination
'''
def question1a():
    #Prints a line describing to the user what the operation is demonstrating
    print("1.a) Union of R1 and R2\n")
    #This is the given set for R1
    R1 = {(1,1),(2,2),(3,3)}
    #This is the given set for R2
    R2 = {(1,1),(1,2),(1,3),(1,4)}
    #Prints a line telling the user what operation is being shown followed by the output of the operation
    print("R1 ∪ R2 =", R1.union(R2))
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)

'''
This method involves the operation R1 ∩ R2 and determining the set of relations that are in both R1 and R2 and printing them.
Author: Combination
'''
def question1b():
    #Prints a line describing to the user what the operation is demonstrating
    print("1.b) Intersection of R1 and R2\n")
    #This is the given set for R1
    R1 = {(1,1),(2,2),(3,3)}
    #This is the given set for R2
    R2 = {(1,1),(1,2),(1,3),(1,4)}
    #Prints a line telling the user what operation is being shown followed by the output of the operation
    print("R1 ∩ R2 =", R1.intersection(R2))
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)

'''
This method involves the operation R1 - R2 and determining the set of relations that are in R1 and not in R2 and printing them.
Author: Combination
'''
def question1c():
    #Prints a line describing to the user what the operation is demonstrating
    print("1.c) Difference of R1 and R2\n")
    #This is the given set for R1
    R1 = {(1,1),(2,2),(3,3)}
    #This is the given set for R2
    R2 = {(1,1),(1,2),(1,3),(1,4)}
    #Prints a line telling the user what operation is being shown followed by the output of the operation
    print("R1 - R2 =", R1.difference(R2))
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)

'''
This method involves the operation R2 - R1 and determining the set of relations that are in R2 and not in R1 and printing them.
Author: Combination
'''
def question1d():
    #Prints a line describing to the user what the operation is demonstrating
    print("1.d) Difference of R2 and R1\n")
    #This is the given set for R1
    R1 = {(1,1),(2,2),(3,3)}
    #This is the given set for R2
    R2 = {(1,1),(1,2),(1,3),(1,4)}
    #Prints a line telling the user what operation is being shown followed by the output of the operation
    print("R2 - R1 =", R2.difference(R1))
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)

#Prints the output showcasing question 1.a
question1a()
#Prints the output showcasing question 1.b
question1b()
#Prints the output showcasing question 1.c
question1c()
#Prints the output showcasing question 1.d
question1d()

'''
Creates a method for taking the composite of two relations.
Taking the composite of two relations uses a Boolean form of matrix multiplication, called the Boolean product, to find the composite of two relations.
Author: Combination
'''
def compositionMethod(R, S):
    #creates an empty set in preparation of the incoming composition
    result = set()
    '''
    Start of a nested for loop where the outer loop (for a, b in R:) will run after the inner loop has been iterated through.
    This will help to identify the pairs of components that are applicable for the composition.
    '''
    for a, b in R:
        '''
        The inner loop (for b_intersection, c in S:) will iterate many times before progressing to the outer loop. 
        This will help to identify the pairs of components that are applicable for the composition.
        '''
        for b_intersection, c in S:
            #Determines if the second component in the current R is equivalent to the first component in the current S
            if b == b_intersection:
                '''
                If the second component in the current R is equivalent to the first component in the current S,
                then the first component of the current R will be paired to the second component of the current S and added to the set.
                '''
                result.add((a, c))
    #Returns the set for printing
    return result

'''
This method involves the operation S ◦ R and determining the set of relations that result from their composition.
Author: Combination
'''
def question2():
    #Prints a line describing to the user what the operation is demonstrating
    print("2.) Composition of S and R\n")
    #This is the given set for R
    R = {(1,1),(1,4),(2,3),(3,1),(3,4)}
    #This is the given set for S
    S = {(1,0),(2,0),(3,1),(3,2),(4,1)}
    #Prints a line telling the user what operation is being shown followed by the output of the operation
    print("S ◦ R =", compositionMethod(R, S))
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)

#Prints the output showcasing question 2
question2()

'''
This method involves the operation R ◦ R, or (R^2), and determining the set of relations that result from their composition.
Author: Combination
'''
def question3():
    #Prints a line describing to the user what the operation is demonstrating
    print("3.) Composition of R and R\n")
    #This is the given set for R
    R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}
    #Prints a line telling the user what operation is being shown followed by the output of the operation
    print("R ◦ R =", compositionMethod(R, R))
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)

#Prints the output showcasing question 3
question3()

'''
This method involves turning the relation R = {(x, y) | x + y = 0} on the set {-10, ..., -1, 0, 1, ..., 10} into a set of ordered pairs.
This method also involves showing whether R is reflexive or not, symmetric or not, antisymmetric or not, and transitive or not.
Author: Combination
'''
def question4all():
    #creates an empty set in preparation of the incoming set output
    ordered_pair = set()
    '''
    Start of a nested for loop where the outer loop (for valueOuter in range(-10,11):) will run after the inner loop has been iterated through.
    This will help to identify the pairs of components that are applicable for the set output.
    '''
    for valueOuter in range(-10, 11):
        '''
        The inner loop (for valueInner in range(-10,11):) will iterate many times before progressing to the outer loop. 
        This will help to identify the pairs of components that are applicable for the set output.
        '''
        for valueInner in range(-10, 11):
            #If the iteration value of the outer loop plus the iteration value of the inner loop equals zero the next line will run
            if valueOuter + valueInner == 0:
                #Adds the two values to the set
                ordered_pair.add((valueInner, valueOuter))
    #Prints a line describing to the user what the operation is demonstrating
    print("4.a) R as a set of ordered pairs\n")
    #Prints a line telling the user what operation is being shown followed by the output of the operation
    print("Set of ordered pairs =", ordered_pair)
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)
    #Returns either true or false if the values in the specified range are reflexive. Where if it contains (x,x) for every x ∈ X it is reflexive.
    determineReflexive = all(((x,x) in ordered_pair) for x in range(-10,11))
    #Returns either true or false if the values in the specified range are symmetric. Where if it contains (x,y) and also contains (y,x) for x ∈ X and y ∈ X it is symmetric.
    determineSymmetric = all(((y,x) in ordered_pair) for (x,y) in ordered_pair if x != y)
    #Returns either true or false if the values in the specified range are antisymmetric. Where if it contains (x,y), but not (y,x) for x ∈ X and y ∈ X it is antisymmetric.
    determineAntisymmetric = all(((y,x) not in ordered_pair) for (x,y) in ordered_pair if x != y)
    '''
    Start of a nested for loop where the outer loop (for s,t in ordered_pair:) will run after the inner loop has been iterated through.
    This will help to identify the pairs of components that are applicable to determine if it is transitive.
    '''
    for s,t in ordered_pair:
        '''
        The inner loop (for x,y in ordered_pair:) will iterate many times before progressing to the outer loop. 
        This will help to identify the pairs of components that are applicable to determine if it is transitive.
        '''
        for x,y in ordered_pair:
            #If the second value of the outer loop is equal to the first value in the inner loop, the next line will run a check
            if t == x:
                #Where if the first value of the outer loop paired with the second value of the inner loop is not in the ordered pair, then it is false
                if (s,y) not in ordered_pair:
                    #Assigns determineTransitive a False to signify it is not transitive
                    determineTransitive = False
                    #Breaks the loop
                    break
                #Where if the first value of the outer loop paired with the second value of the inner loop is in the ordered pair, then it is true
                else:
                    #Assigns determineTransitive a True to signify it is transitive
                    determineTransitive = True
    #If the output of the specified variable is assigned True, then it will print a statement signifying so
    if determineReflexive == True:
        #Prints a line describing to the user what the operation is demonstrating
        print("4.b) R is Reflexive")
    #If the output of the specified variable is assigned False, then it will print a statement signifying so
    else:
        #Prints a line describing to the user what the operation is demonstrating
        print("4.b) R is not Reflexive")
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)
    #If the output of the specified variable is assigned True, then it will print a statement signifying so
    if determineSymmetric == True:
        #Prints a line describing to the user what the operation is demonstrating
        print("4.c) R is Symmetric")
    #If the output of the specified variable is assigned False, then it will print a statement signifying so
    else:
        #Prints a line describing to the user what the operation is demonstrating
        print("4.c) R is not Symmetric")
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)
    #If the output of the specified variable is assigned True, then it will print a statement signifying so
    if determineAntisymmetric == True:
        #Prints a line describing to the user what the operation is demonstrating
        print("4.d) R is Antisymmetric")
    #If the output of the specified variable is assigned False, then it will print a statement signifying so
    else:
        #Prints a line describing to the user what the operation is demonstrating
        print("4.d) R is not Antisymmetric")
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)
    #If the output of the specified variable is assigned True, then it will print a statement signifying so
    if determineTransitive == True:
        #Prints a line describing to the user what the operation is demonstrating
        print("4.e) R is Transitive")
    #If the output of the specified variable is assigned False, then it will print a statement signifying so
    else:
        #Prints a line describing to the user what the operation is demonstrating
        print("4.e) R is not Transitive")
    #Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*100)
    
#Prints the output showcasing question 4
question4all()
