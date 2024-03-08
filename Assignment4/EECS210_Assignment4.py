'''
Name of program contained in the file: EECS210_Assignment4.py
Brief description of the program: Determines if a relation (R) of ordered pairs is reflexive or not & then if it is not, finds the reflexive closure of R (R*).
                                  Determines if a relation (R) of ordered pairs is symmetric or not & then if it is not, finds the symmetric closure of R (R*).
                                  Determines if a relation (R) of ordered pairs is transitive or not & then if it is not, finds the transitive closure of R (R*) using Warshall’s Algorithm.
                                  Determines if a relation (R) of ordered pairs is an equivalence relation or not and the reason why.
                                  Determines if a relation (R) of ordered pairs is a poset of the set (S) or not and the reason why.
Inputs: None
Output: Print out the exercise number followed by the exercise’s output
All collaborators: Omar Mohammed, Humza Qureshi, Aniketh Aatipamula
Other Sources for the Code: Stack Overflow, Reintech Media, "Properties of Relations" Canvas Slides, "Closure & Equivalence Relations" Canvas Slides
Author's full name: Nabeel Ahmad
Creation date: 10/11/2023
'''

'''
This method involves determining whether R is reflexive or not for two different relations and their corresponding sets.
And if R is not reflexive, it will adjust the relation to make it reflexive.
Author: Combination
'''
def question1():
    #This is the given set for question 1.d
    given_set1D = {1,2,3,4}
    #This is the given set for question 1.e
    given_set1E = {"a","b","c","d"}
    #This is the given relation for question 1.d
    R1D = {(1,1),(4,4),(2,2),(3,3)}
    #This is the given relation for question 1.e
    R1E = {("a","a"),("c","c")}
    #Creates a set where reflexive closure can be completed if needed for the relation in question 1.d
    reflexiveClosure1D = set(R1D)
    #Creates a set where reflexive closure can be completed if needed for the relation in question 1.e
    reflexiveClosure1E = set(R1E)
    #Creates a for loop to run through the values in the given set
    for value in given_set1D:
        #If there exists a pair of the same value in the relation, then it is reflexive
        if (value,value) in R1D:
            #Assigns a boolean value to the variable
            determineReflexive1D = True
        #If there does not exist a pair of the same value in the relation, then it is not reflexive
        else:
            #Assigns a boolean value to the variable
            determineReflexive1D = False
    #Creates a for loop to run through the values in the given set
    for value in given_set1D:
        #This will add values to the set that make the relation reflexive
        reflexiveClosure1D.add((value,value))
    #Prints the relation
    print("1.a) R = {(1,1),(4,4),(2,2),(3,3)}")
    #If the relation is reflexive, this will run
    if determineReflexive1D == True:
        #Prints a statement stating the relation is reflexive
        print("1.b) R is reflexive")
        #Prints a statement stating that reflexive closure is not required
        print("1.c) Reflexive Closure is not required")
        #Prints the relation which confirms reflexivity
        print(f"1.d) R = {R1D}\n")
    #If the relation is not reflexive, this will run
    else:
        #Prints a statement stating the relation is not reflexive
        print("1.b) R is not reflexive")
        #Prints a statement stating that reflexive closure is required
        print("1.c) Reflexive Closure is required")
        #Prints the relation where reflexive closure is completed
        print(f"1.d) Reflexive Closure of the relation: R = {reflexiveClosure1D}\n")
    #Creates a for loop to run through the values in the given set
    for value in given_set1E:
        #If there exists a pair of the same value in the relation, then it is reflexive
        if (value,value) in R1E:
            #Assigns a boolean value to the variable
            determineReflexive1E = True
        #If there does not exist a pair of the same value in the relation, then it is not reflexive
        else:
            #Assigns a boolean value to the variable
            determineReflexive1E = False
    #Creates a for loop to run through the values in the given set
    for value in given_set1E:
        #This will add values to the set that make the relation reflexive
        reflexiveClosure1E.add((value,value))
    #Prints the relation
    print("1.a) R = {(a,a),(c,c)}")
    #If the relation is reflexive, this will run
    if determineReflexive1E == True:
        #Prints a statement stating the relation is reflexive
        print("1.b) R is reflexive")
        #Prints a statement stating that reflexive closure is not required
        print("1.c) Reflexive Closure is not required")
        #Prints the relation which confirms reflexivity
        print(f"1.d) R = {R1E}\n")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)
    #If the relation is not reflexive, this will run
    else:
        #Prints a statement stating the relation is not reflexive
        print("1.b) R is not reflexive")
        #Prints a statement stating that reflexive closure is required
        print("1.c) Reflexive Closure is required")
        #Prints the relation where reflexive closure is completed
        print(f"1.e) Reflexive Closure of the relation: R = {reflexiveClosure1E}")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)

'''
This method involves determining whether R is symmetric or not for two different relations and their corresponding sets.
And if R is not symmetric, it will adjust the relation to make it symmetric.
Author: Combination
'''
def question2():
    #This is the given set for question 2.d
    given_set2D = {1,2,3,4}
    #This is the given set for question 2.e
    given_set2E = {1,2,3,4}
    #This is the given relation for question 2.d
    R2D = {(1,2),(4,4),(2,1),(3,3)}
    #This is the given relation for question 2.e
    R2E = {(1,2),(3,3)}
    #Creates a set where symmetric closure can be completed if needed for the relation in question 2.d
    symmetricClosure2D = set(R2D)
    #Creates a set where symmetric closure can be completed if needed for the relation in question 2.e
    symmetricClosure2E = set(R2E)
    #Creates a for loop to run through the ordered pairs in the given set
    for ordered_pair in R2D:
        #If there does not exist an ordered pair in the relation then it is not symmetric
        if ordered_pair[0] and ordered_pair[1] in R2D:
            #Assigns a boolean value to the variable
            determineSymmetric2D = True
        #If there exists an ordered pair that exists in the relation then it is symmetric
        else:
            #Assigns a boolean value to the variable
            determineSymmetric2D = False
    #Creates a for loop to run through the ordered pairs in the given set
    for ordered_pair in R2D:
        #This will add values to the set that make the relation symmetric
        symmetricClosure2D.add((ordered_pair[1],ordered_pair[0]))
    #Prints the relation
    print("2.a) R = {(1,2),(4,4),(2,1),(3,3)}")
    #If the relation is not symmetric, this will run
    if determineSymmetric2D == True:
        #Prints a statement stating the relation is not symmetric
        print("2.b) R is not symmetric")
        #Prints a statement stating that symmetric closure is required
        print("2.c) Symmetric Closure is required")
        #Prints the relation where symmetric closure is completed
        print(f"2.d) R = {symmetricClosure2D}\n")
    #If the relation is symmetric, this will run
    else:
        #Prints a statement stating the relation is symmetric
        print("2.b) R is symmetric")
        #Prints a statement stating that symmetric closure is not required
        print("2.c) Symmetric Closure is not required")
        #Prints the relation which confirms the relation is symmetric 
        print(f"2.d) R = {R2D}\n")
    #Creates a for loop to run through the ordered pairs in the given set
    for ordered_pair in R2E:
        #If there exists an ordered pair that exists in the relation then it is symmetric
        if ordered_pair[0] and ordered_pair[1] in R2E:
            #Assigns a boolean value to the variable
            determineSymmetric2E = True
        #If there does not exist an ordered pair in the relation then it is not symmetric
        else:
            #Assigns a boolean value to the variable
            determineSymmetric2E = False
    #Creates a for loop to run through the ordered pairs in the given set
    for ordered_pair in R2E:
            #This will add values to the set that make the relation symmetric
            symmetricClosure2E.add((ordered_pair[1],ordered_pair[0]))
    #Prints the relation
    print("2.a) R = {(1,2),(3,3)}")
    #If the relation is symmetric, this will run
    if determineSymmetric2E == True:
        #Prints a statement stating the relation is symmetric
        print("2.b) R is symmetric")
        #Prints a statement stating that symmetric closure is not required
        print("2.c) Symmetric Closure is not required")
        #Prints the relation which confirms the relation is symmetric
        print(f"2.e) R = {R2E}")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)
    #If the relation is not symmetric, this will run
    else:
        #Prints a statement stating the relation is not symmetric
        print("2.b) R is not symmetric")
        #Prints a statement stating that symmetric closure is required
        print("2.c) Symmetric Closure is required")
        #Prints the relation where symmetric closure is completed
        print(f"2.e) R = {symmetricClosure2E}")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)

'''
This method involves determining whether R is an equivalence relation or not for two different relations and their corresponding sets.
Author: Combination
'''
def question4():
    #This is the given set for question 4.d
    given_set4D = {1,2,3}
    #This is the given set for question 4.e
    given_set4E = {"a","b","c"}
    #This is the given relation for question 4.d
    R4D = {(1,1),(2,2),(2,3)}
    #This is the given relation for question 4.e
    R4E = {("a","a"),("b","b"),("c","c"),("b","c"),("c","b")}
    #Creates a for loop to run through the values in the given set
    for value in given_set4D:
        #If there exists a pair of the same value in the relation, then it is reflexive
        if (value,value) in R4D:
            #Assigns a boolean value to the variable
            determineReflexive4D = True
        #If there does not exist a pair of the same value in the relation, then it is not reflexive
        else:
            #Assigns a boolean value to the variable
            determineReflexive4D = False
    #Creates a for loop to run through the ordered pairs in the given set
    for ordered_pair in R4D:
        #If there exists an ordered pair that exists in the relation then it is symmetric
        if ordered_pair[0] and ordered_pair[1] in R4D:
            #Assigns a boolean value to the variable
            determineSymmetric4D = True
        #If there does not exist an ordered pair in the relation then it is not symmetric
        else:
            #Assigns a boolean value to the variable
            determineSymmetric4D = False
    '''
    Start of a nested for loop where the outer loop (for (value1,value2) in R4D:) will run after the inner loop has been iterated through.
    This will help to identify the pairs of components that are applicable to determine if it is transitive.
    '''
    for (value1,value2) in R4D:
        '''
        The inner loop (for (value3,value4) in R4D:) will iterate many times before progressing to the outer loop. 
        This will help to identify the pairs of components that are applicable to determine if it is transitive.
        '''
        for (value3,value4) in R4D:
            #If the second value of the outer loop is equal to the first value in the inner loop, the next line will run a check
            if value2 == value3:
                #Where if the first value of the outer loop paired with the second value of the inner loop is in the ordered pair, then it is true
                if (value1,value4) in R4D:
                    #Assigns determineTransitive a True to signify it is transitive
                    determineTransitive4D = True
                #Where if the first value of the outer loop paired with the second value of the inner loop is not in the ordered pair, then it is false
                else:
                    #Assigns determineTransitive a False to signify it is not transitive
                    determineTransitive4D = False
    #Prints the relation
    print("4.a) R = {(1,1),(2,2),(2,3)}")
    #If all cases are true, then it is an equivalence relation
    if determineReflexive4D and determineSymmetric4D and determineTransitive4D == True:
        #Prints a statement stating R is an equivalence relation
        print("4.b) R is an equivalence relation")
        #Shows why it is an equivalence relation
        print("4.c) The relation is an equivalence relation because it is reflexive, transitive, and symmetric\n")
    #If one case is false, then it is not an equivalence relation
    else:
        #Prints a statement stating R is not an equivalence relation
        print("4.b) R is not an equivalence relation")
        #Shows why it is not an equivalence relation
        print(f"4.c) The relation is not an equivalence relation because reflexive = {determineReflexive4D}, transitive = {determineTransitive4D}, and symmetric = {determineSymmetric4D}\n")
    #Creates a for loop to run through the values in the given set
    for value in given_set4E:
        #If there exists a pair of the same value in the relation, then it is reflexive
        if (value,value) in R4E:
            #Assigns a boolean value to the variable
            determineReflexive4E = True
        #If there does not exist a pair of the same value in the relation, then it is not reflexive
        else:
            #Assigns a boolean value to the variable
            determineReflexive4E = False
    #Creates a for loop to run through the ordered pairs in the given set
    for ordered_pair in R4E:
        #If there does not exist an ordered pair in the relation then it is not symmetric
        if ordered_pair[0] and ordered_pair[1] in R4E:
            #Assigns a boolean value to the variable
            determineSymmetric4E = False
        #If there exists an ordered pair that exists in the relation then it is symmetric
        else:
            #Assigns a boolean value to the variable
            determineSymmetric4E = True
    '''
    Start of a nested for loop where the outer loop (for (value1,value2) in R4E:) will run after the inner loop has been iterated through.
    This will help to identify the pairs of components that are applicable to determine if it is transitive.
    '''
    for (value1,value2) in R4E:
        '''
        The inner loop (for (value3,value4) in R4E:) will iterate many times before progressing to the outer loop. 
        This will help to identify the pairs of components that are applicable to determine if it is transitive.
        '''
        for (value3,value4) in R4E:
            #If the second value of the outer loop is equal to the first value in the inner loop, the next line will run a check
            if value2 == value3:
                #Where if the first value of the outer loop paired with the second value of the inner loop is in the ordered pair, then it is true
                if (value1,value4) in R4E:
                    #Assigns determineTransitive a True to signify it is transitive
                    determineTransitive4E = True
                #Where if the first value of the outer loop paired with the second value of the inner loop is not in the ordered pair, then it is false
                else:
                    #Assigns determineTransitive a False to signify it is not transitive
                    determineTransitive4E = False
    #Prints the relation
    print("4.a) R = {(a,a),(b,b),(c,c),(b,c),(c,b)}")
    #If all cases are true, then it is an equivalence relation
    if determineReflexive4E and determineSymmetric4E and determineTransitive4E == True:
        #Prints a statement stating R is an equivalence relation
        print("4.b) R is an equivalence relation")
        #Shows why it is an equivalence relation
        print("4.c) The relation is an equivalence relation because it is reflexive, transitive, and symmetric")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)
    #If one case is false, then it is not an equivalence relation
    else:
        #Prints a statement stating R is not an equivalence relation
        print("4.b) R is not an equivalence relation")
        #Shows why it is not an equivalence relation
        print(f"4.c) The relation is not an equivalence relation because reflexive = {determineReflexive4E}, transitive = {determineTransitive4E}, and symmetric = {determineSymmetric4E}")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)

'''
This method involves determining whether R is a poset or not for two different relations and their corresponding sets.
Author: Combination
'''
def question5():
    #This is the given set for question 5.d
    given_set5D = {1, 2, 3, 4}
    #This is the given set for question 5.e
    given_set5E = {0, 1, 2, 3}
    #This is the given relation for question 5.d
    R5D = {(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)}
    #This is the given relation for question 5.e
    R5E = {(0, 0), (0, 1), (0, 2), (0, 3), (1,0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)}
    #Creates a for loop to run through the values in the given set
    for value in given_set5D:
        #If there exists a pair of the same value in the relation, then it is reflexive
        if (value,value) in R5D:
            #Assigns a boolean value to the variable
            determineReflexive5D = True
        #If there does not exist a pair of the same value in the relation, then it is not reflexive
        else:
            #Assigns a boolean value to the variable
            determineReflexive5D = False
    #Creates a for loop to run through the values in the given relation
    for ordered_pair in R5D:
        #If the ordered pairs do not follow the statement, then it is not antisymmetric
        if ordered_pair[0] != ordered_pair[1] and ((ordered_pair[1], ordered_pair[0]) in R5D):
            #Assigns a boolean value to the variable
            determineAnti5D = False
        #Otherwise it is antisymmetric
        else:
            #Assigns a boolean value to the variable
            determineAnti5D = True
    '''
    Start of a nested for loop where the outer loop (for (value1,value2) in R4E:) will run after the inner loop has been iterated through.
    This will help to identify the pairs of components that are applicable to determine if it is transitive.
    '''
    for (value1,value2) in R5D:
        '''
        The inner loop (for (value3,value4) in R4E:) will iterate many times before progressing to the outer loop. 
        This will help to identify the pairs of components that are applicable to determine if it is transitive.
        '''
        for (value3,value4) in R5D:
            #If the second value of the outer loop is equal to the first value in the inner loop, the next line will run a check
            if value2 == value3:
                #Where if the first value of the outer loop paired with the second value of the inner loop is in the ordered pair, then it is true
                if (value1,value4) in R5D:
                    #Assigns determineTransitive a True to signify it is transitive
                    determineTransitive5D = True
                #Where if the first value of the outer loop paired with the second value of the inner loop is not in the ordered pair, then it is false
                else:
                    #Assigns determineTransitive a False to signify it is not transitive
                    determineTransitive5D = False
    #Prints the relation
    print("5.a) R = {(1,1),(1,2),(2,2),(3,3),(4,1),(4,2),(4,4)}")
    #Prints the set
    print("5.b) S = {1,2,3,4}")
    #If all cases are true, then it is an equivalence relation
    if determineReflexive5D and determineAnti5D and determineTransitive5D == True:
        #Prints a statement stating R is a poset
        print("5.c) R is a poset")
        #Shows why it is a poset
        print("5.e) The relation is a poset because it is reflexive, transitive, and antisymmetric\n")
    #If one case is false, then it is not a poset
    else:
        #Prints a statement stating R is not a poset
        print("5.c) R is not a poset")
        #Shows why it is not a poset
        print(f"5.e) The relation is not a poset because reflexive = {determineReflexive5D}, transitive = {determineTransitive5D}, and antisymmetric = {determineAnti5D}\n")
    #Creates a for loop to run through the values in the given set
    for value in given_set5E:
        #If there exists a pair of the same value in the relation, then it is reflexive
        if (value,value) in R5E:
            #Assigns a boolean value to the variable
            determineReflexive5E = True
        #If there does not exist a pair of the same value in the relation, then it is not reflexive
        else:
            #Assigns a boolean value to the variable
            determineReflexive5E = False
    #Creates a for loop to run through the values in the given relation
    for ordered_pair in R5E:
        #If the ordered pairs do not follow the statement, then it is not antisymmetric
        if ordered_pair[0] != ordered_pair[1] and ((ordered_pair[1], ordered_pair[0]) in R5E):
            #Assigns a boolean value to the variable
            determineAnti5E = False
        #Otherwise it is antisymmetric
        else:
            #Assigns a boolean value to the variable
            determineAnti5E = True
    '''
    Start of a nested for loop where the outer loop (for (value1,value2) in R4E:) will run after the inner loop has been iterated through.
    This will help to identify the pairs of components that are applicable to determine if it is transitive.
    '''
    for (value1,value2) in R5E:
        '''
        The inner loop (for (value3,value4) in R4E:) will iterate many times before progressing to the outer loop. 
        This will help to identify the pairs of components that are applicable to determine if it is transitive.
        '''
        for (value3,value4) in R5E:
            #If the second value of the outer loop is equal to the first value in the inner loop, the next line will run a check
            if value2 == value3:
                #Where if the first value of the outer loop paired with the second value of the inner loop is in the ordered pair, then it is true
                if (value1,value4) in R5E:
                    #Assigns determineTransitive a False to signify it is not transitive
                    determineTransitive5E = False
                #Where if the first value of the outer loop paired with the second value of the inner loop is not in the ordered pair, then it is false
                else:
                    #Assigns determineTransitive a True to signify it is transitive
                    determineTransitive5E = True
    #Prints the relation
    print("5.a) R = {(0, 0), (0, 1), (0, 2), (0, 3), (1,0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)}")
    #Prints the set
    print("5.b) S = {0, 1, 2, 3}")
    #If all cases are true, then it is an equivalence relation
    if determineReflexive5E and determineAnti5E and determineTransitive5E == True:
        #Prints a statement stating R is a poset
        print("5.c) R is a poset")
        #Shows why it is a poset
        print("5.f) The relation is a poset because it is reflexive, transitive, and antisymmetric\n")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)
    #If one case is false, then it is not a poset
    else:
        #Prints a statement stating R is not a poset
        print("5.c) R is not a poset")
        #Shows why it is not a poset
        print(f"5.f) The relation is not a poset because reflexive = {determineReflexive5E}, transitive = {determineTransitive5E}, and antisymmetric = {determineAnti5E}")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)

'''
This method involves determining whether R is transitive or not for two different relations and their corresponding sets.
And if R is not transitive, it will adjust the relation to make it transitive.
Author: Combination
'''
def question3():
    #This is the given set for question 3.d
    given_set3D = {"a","b","c","d"}
    #This is the given set for question 3.e
    given_set3E = {1,2,3}
    #This is the given relation for question 3.d
    R3D = {("a","b"),("d","d"),("b","c"),("a","c")}
    #This is the given set for question 3.e
    R3E = {(1,1),(1,3),(2,2),(3,1),(3,2)}
    '''
    Start of a nested for loop where the outer loop (for (value1,value2) in R4E:) will run after the inner loop has been iterated through.
    This will help to identify the pairs of components that are applicable to determine if it is transitive.
    '''
    for (value1,value2) in R3D:
        '''
        The inner loop (for (value3,value4) in R4E:) will iterate many times before progressing to the outer loop. 
        This will help to identify the pairs of components that are applicable to determine if it is transitive.
        '''
        for (value3,value4) in R3D:
            #If the second value of the outer loop is equal to the first value in the inner loop, the next line will run a check
            if value2 == value3:
                #Where if the first value of the outer loop paired with the second value of the inner loop is in the ordered pair, then it is true
                if (value1,value4) in R3D:
                    #Assigns determineTransitive a False to signify it is not transitive
                    determineTransitive3D = False
                #Where if the first value of the outer loop paired with the second value of the inner loop is not in the ordered pair, then it is false
                else:
                    #Assigns determineTransitive a True to signify it is transitive
                    determineTransitive3D = True
    #Creates a set where reflexive closure can be completed if needed for the relation in question 3.d
    transitiveClosure3D = set(R3D)
    #Creates a while true loop
    while True:
        #Initializes a new set
        new = set()
        '''
        Start of a nested for loop where the outer loop (for value1,value2 in transitiveClosure3D:) will run after the inner loop has been iterated through.
        This will help to identify the pairs of components that are applicable to determine if it is transitive.
        '''
        for value1,value2 in transitiveClosure3D:
            '''
            Start of a nested for loop where the outer loop (for value3,value4 in transitiveClosure3D:) will run after the inner loop has been iterated through.
            This will help to identify the pairs of components that are applicable to determine if it is transitive.
            '''
            for value3,value4 in transitiveClosure3D:
                #If the second value of the outer loop is equal to the first value in the inner loop, the next line will run a check
                if value2 == value3 and (value1,value4) not in transitiveClosure3D:
                    #This will add values to the set that make the relation transitive
                    new.add((value1,value4))
        #Otherwise
        if not new:
            #The loop will break
            break
        #This will add values to the set that make the relation transitive
        transitiveClosure3D.add(new)
    #Prints the relation
    print("3.a) R = {(a,b), (d,d), (b,c), (a,c)}")
    #If it is transitive it will run this
    if determineTransitive3D == False:
        #Prints a statement stating that it is transitive
        print("3.b) R is transitive")
        #Prints a statement stating that transitive closure is not required
        print("3.c) Transitive Closure is not required\n")
    #If it is not transitive this will run
    else:
        #Prints a statement stating that it is not transitive
        print("3.b) R is not transitive")
        #Prints a statement stating that reflexive closure is required
        print("3.c) Transitive Closure is required\n")
        print(f"3.d) R = {transitiveClosure3D}")
    '''
    Start of a nested for loop where the outer loop (for (value1,value2) in R4E:) will run after the inner loop has been iterated through.
    This will help to identify the pairs of components that are applicable to determine if it is transitive.
    '''
    for (value1,value2) in R3E:
        '''
        The inner loop (for (value3,value4) in R4E:) will iterate many times before progressing to the outer loop. 
        This will help to identify the pairs of components that are applicable to determine if it is transitive.
        '''
        for (value3,value4) in R3E:
            #If the second value of the outer loop is equal to the first value in the inner loop, the next line will run a check
            if value2 == value3:
                #Where if the first value of the outer loop paired with the second value of the inner loop is in the ordered pair, then it is true
                if (value1,value4) in R3E:
                    #Assigns determineTransitive a False to signify it is not transitive
                    determineTransitive3E = False
                #Where if the first value of the outer loop paired with the second value of the inner loop is not in the ordered pair, then it is false
                else:
                    #Assigns determineTransitive a True to signify it is transitive
                    determineTransitive3E = True
    #Creates a set where reflexive closure can be completed if needed for the relation in question 3.d
    transitiveClosure3E = set(R3E)
    #Creates a while true loop
    while True:
        #Initializes a new set
        new = set()
        '''
        Start of a nested for loop where the outer loop (for (value1,value2) in R4E:) will run after the inner loop has been iterated through.
        This will help to identify the pairs of components that are applicable to determine if it is transitive.
        '''
        for value1,value2 in transitiveClosure3E:
            '''
            The inner loop (for (value3,value4) in R4E:) will iterate many times before progressing to the outer loop. 
            This will help to identify the pairs of components that are applicable to determine if it is transitive.
            '''
            for value3,value4 in transitiveClosure3E:
                #If the second value of the outer loop is equal to the first value in the inner loop, the next line will run a check
                if value2 == value3 and (value1,value4) not in transitiveClosure3E:
                    #This will add values to the set that make the relation transitive
                    new.add((value1,value4))
        #Otherwise
        if not new:
            #Breaks the loop
            break
        #Creates a set where reflexive closure can be completed if needed for the relation in question 3.d
        transitiveClosure3E.update(new)
    #Prints the relation
    print("R = {(1,1),(1,3),(2,2),(3,1),(3,2)}")
    #If it is transitive this will run
    if determineTransitive3E == True:
        #Prints a statement stating that it is transitive
        print("3.b) R is transitive")
        #Prints a statement stating that transitive closure is not required
        print("3.c) Transitive Closure is not required")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)
    #If it is not transitive this will run
    else:
        #Prints a statement stating that it is not transitive
        print("3.b) R is not transitive")
        #Prints a statement stating that reflexive closure is required
        print("3.c) Transitive Closure is required")
        #Prints the updated relation
        print(f"3.d) R = {transitiveClosure3D}")
        #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
        print("_"*100)

#Prints the output showcasing question 1
question1()
#Prints the output showcasing question 2
question2()
#Prints the output showcasing question 3
question3()
#Prints the output showcasing question 4
question4()
#Prints the output showcasing question 5
question5()
