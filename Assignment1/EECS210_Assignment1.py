'''
Name of program contained in the file: EECS210_Assignment1.py
Brief description of the program: This program's objective is to print out truth tables for six propositions to show their logical equivalence. 
                                  The truth tables included are of De Morgan's First Law, De Morgan's Second Law, the First Associative Law, and Second Associative Law. 
                                  And [(p + q) * (p -> r) * (q -> r)] -> r = T as well as p <-> q = (p -> q) * (q -> p).
Inputs: None
Output: Print out of the name and number of each exercise, followed by the exercise’s truth table output
All collaborators: Omar Mohammed
Other Sources for the Code: Stack Overflow, Real Python, "Propositional Logic" Canvas Slides
Author's full name: Nabeel Ahmad
Creation date: 08/30/2023
'''

'''
Creates a function definition for De Morgan's First Law with two variables. 
This truth table proves that if two variables are AND'ed together and then negated, it is equivalent to OR'ing the two negated variables.
This function also contains a nested for loop because a nested for loop allows for the iteration of every possible True, False combination
Author: Combination
'''
def dMorgFirst():
    #Prints a line telling the user what table is being shown
    print("1. De Morgan’s First Law")

    #Prints the table header row to separate between columns
    print("|   p   |   q   |   !p   |   !q   |  p * q  |  !(p * q)  |  !p + !q  |")

    '''
    Start of a nested for loop where the outer loop (for p in (True, False):) will run after the inner loop has been iterated through. 
    This will help create the "p" column of the truth table and allow for use in the boolean expression within
    '''
    for p in (True, False):
        '''
        The inner loop (for q in (True, False):) will iterate many times before progressing to the outer loop. 
        This will help create the "q" column of the truth table and allow for use in the boolean expression within
        '''
        for q in (True, False):
            #Boolean expression that has been assigned a variable name. The boolean expression is "not p", which is the same as "!p"
            not_p = not p

            #Boolean expression that has been assigned a variable name. The boolean expression is "not q", which is the same as "!q"
            not_q = not q

            #Boolean expression that has been assigned a variable name. The boolean expression is "p and q", which is the same as "p * q"
            p_and_q = p and q

            #Boolean expression that has been assigned a variable name. The boolean expression is "not (p and q)", which is the same as "!(p * q)"
            not_p_and_not_q = not (p and q)

            #Boolean expression that has been assigned a variable name. The boolean expression is "not p or not q", which is the same as "!p + !q"
            not_p_or_not_q = not_p or not_q
            
            #Prints the table row by row segmented by each important step to proving De Morgan's First Law correct
            print(f"|{p}   |{q}   |{not_p}   |{not_q}   |{p_and_q}     |{not_p_and_not_q}       |{not_p_or_not_q}      |")

'''
Creates a function definition for De Morgan's Second Law with two variables. 
This truth table proves that if two variables are OR'ed together and then negated, it is equivalent to AND'ing the two negated variables.
This function also contains a nested for loop because a nested for loop allows for the iteration of every possible True, False combination
Author: Combination
'''
def dMorgSecond():
    #Prints a line telling the user what table is being shown
    print("2. De Morgan’s Second Law")

    #Prints the table header row to separate between columns
    print("|   p   |   q   |   !p   |   !q   |  p + q  |  !(p + q)  |  !p * !q  |")

    '''
    Start of a nested for loop where the outer loop (for p in (True, False):) will run after the inner loop has been iterated through. 
    This will help create the "p" column of the truth table and allow for use in the boolean expression within
    '''
    for p in (True, False):
        '''
        The inner loop (for q in (True, False):) will iterate many times before progressing to the outer loop. 
        This will help create the "q" column of the truth table and allow for use in the boolean expression within
        '''
        for q in (True, False):
            #Boolean expression that has been assigned a variable name. The boolean expression is "not p", which is the same as "!p"
            not_p = not p

            #Boolean expression that has been assigned a variable name. The boolean expression is "not q", which is the same as "!q"
            not_q = not q

            #Boolean expression that has been assigned a variable name. The boolean expression is "p or q", which is the same as "p + q"
            p_or_q = p or q
            
            #Boolean expression that has been assigned a variable name. The boolean expression is "not (p or q)", which is the same as "!(p + q)"
            not_p_or_not_q = not (p or q)

            #Boolean expression that has been assigned a variable name. The boolean expression is "not p and not q", which is the same as "!p * !q"
            not_p_and_not_q = not_p and not_q

            #Prints the table row by row segmented by each important step to proving De Morgan's Second Law correct
            print(f"|{p}   |{q}   |{not_p}   |{not_q}   |{p_or_q}     |{not_p_or_not_q}       |{not_p_and_not_q}      |")

'''
Creates a function definition for the First Associative Law.
This truth table proves that when you AND any three variables together, no matter the grouping of two variables the result will be the same.
This function also contains a nested for loop because a nested for loop allows for the iteration of every possible True, False combination
Author: Combination
'''
def firstAssociative():
    #Prints a line telling the user what table is being shown
    print("3. First Associative Law")

    #Prints the table header row to separate between columns
    print("|   p   |   q   |   r   | (p * q) * r | p * (q * r) |")

    '''
    Start of a nested for loop where the outer loop (for p in (True, False):) will run after the inner loop has been iterated through. 
    This will help create the "p" column of the truth table and allow for use in the boolean expression within
    '''
    for p in (True, False):
        '''
        The inner loop (for q in (True, False):) will iterate many times before progressing to the outer loop. 
        This will help create the "q" column of the truth table and allow for use in the boolean expression within
        '''
        for q in (True, False):
            '''
            The inner inner loop (for r in (True, False):) will iterate many times before progressing to the next loop.
            This will help create the "r" column of the truth table and allow for use in the boolean expression within.
            '''
            for r in (True, False):
                #Boolean expression that has been assigned a variable name. The boolean expression is "(p and q) and r", which is the same as "(p * q) * r"
                p_and_q_then_and_r = (p and q) and r

                #Boolean expression that has been assigned a variable name. The boolean expression is "p and (q and r)", which is the same as "p * (q * r)"
                q_and_r_then_and_p = p and (q and r)

                #Prints the table row by row segmented by each important step to proving the First Associative Law correct
                print(f"|{p}   |{q}   |{r}   |{p_and_q_then_and_r}         |{q_and_r_then_and_p}         |")

'''
Creates a function definition for the Second Associative Law.
This truth table proves that when you OR any three variables together, no matter the grouping of two variables the result will be the same.
This function also contains a nested for loop because a nested for loop allows for the iteration of every possible True, False combination
Author: Combination
'''
def secondAssociative():
    #Prints a line telling the user what table is being shown
    print("4. Second Associative Law")

    #Prints the table header row to separate between columns
    print("|   p   |   q   |   r   | (p + q) + r | p + (q + r) |")

    '''
    Start of a nested for loop where the outer loop (for p in (True, False):) will run after the inner loop has been iterated through. 
    This will help create the "p" column of the truth table and allow for use in the boolean expression within
    '''
    for p in (True, False):
        '''
        The inner loop (for q in (True, False):) will iterate many times before progressing to the outer loop. 
        This will help create the "q" column of the truth table and allow for use in the boolean expression within
        '''
        for q in (True, False):
            '''
            The inner inner loop (for r in (True, False):) will iterate many times before progressing to the next loop.
            This will help create the "r" column of the truth table and allow for use in the boolean expression within.
            '''
            for r in (True, False):
                #Boolean expression that has been assigned a variable name. The boolean expression is "(p or q) or r", which is the same as "(p + q) + r"
                p_or_q_then_or_r = (p or q) or r

                #Boolean expression that has been assigned a variable name. The boolean expression is "p or (q or r)", which is the same as "p + (q + r)"
                q_or_r_then_or_p = p or (q or r)

                #Prints the table row by row segmented by each important step to proving the Second Associative Law correct
                print(f"|{p}   |{q}   |{r}   |{p_or_q_then_or_r}         |{q_or_r_then_or_p}         |")

'''
Creates a function definition for the proposition [(p + q) * (p -> r) * (q -> r)] -> r = T.
This truth table proves that the three conditions of if p or q, if p then r, and if q then r AND'ed together then r yields True.
Therefore, [(p + q) * (p -> r) * (q -> r)] -> r should yield True for all rows of the truth table.
This function also contains a nested for loop because a nested for loop allows for the iteration of every possible True, False combination
Author: Combination
'''
def numberFive():
    #Prints a line telling the user what table is being shown
    print("5. [(p + q) * (p -> r) * (q -> r)] -> r = T")

    #Prints the table header row to separate between columns
    print("|   p   |   q   |   r   |  (p + q)  |  (p -> r)  |  (q -> r)  |(p + q) * (p -> r) * (q -> r)|(p + q) * (p -> r) * (q -> r) -> r|   T   |")

    '''
    Start of a nested for loop where the outer loop (for p in (True, False):) will run after the inner loop has been iterated through. 
    This will help create the "p" column of the truth table and allow for use in the boolean expression within
    '''
    for p in (True, False):
        '''
        The inner loop (for q in (True, False):) will iterate many times before progressing to the outer loop. 
        This will help create the "q" column of the truth table and allow for use in the boolean expression within
        '''
        for q in (True, False):
            '''
            The inner inner loop (for r in (True, False):) will iterate many times before progressing to the next loop.
            This will help create the "r" column of the truth table and allow for use in the boolean expression within.
            '''
            for r in (True, False):
                #Boolean expression that has been assigned a variable name. The boolean expression is "p or q", which is the same as "p + q"
                p_or_q = p or q

                '''
                Boolean expression that has been derived from the conversion of "p -> r" into "!p + r".
                This is the same as converting if "p then r" into "not p or r".
                This conversion was found on slide 29 of the Propositional Logic slides on Canvas
                '''
                if_p_then_r = not p or r

                '''
                Boolean expression that has been derived from the conversion of "q -> r" into "!q + r".
                This is the same as converting if "q then r" into "not q or r".
                This conversion was found on slide 29 of the Propositional Logic slides on Canvas
                '''
                if_q_then_r = not q or r

                '''
                Boolean expression that has been assigned a variable name.
                This involves taking the three boolean expressions above ((p or q), (not p or r), (not q or r)) and AND'ing them together
                '''
                and_three = p_or_q and if_p_then_r and if_q_then_r

                '''
                Boolean expression that has been assigned a variable name.
                This involves taking the result of the three boolean expressions AND'ed together (the variable "and_three") and negating them to OR with r
                '''
                not_and_three_then_or_r = not and_three or r

                '''
                Variable that will print "True" in last column. 
                This will allow you to check whether the left side and right side of the equation match
                '''
                variable_true = True

                #Prints the table row by row segmented by each important step to proving the proposition [(p + q) * (p -> r) * (q -> r)] -> r = T correct
                print(f"|{p}   |{q}   |{r}   |{p_or_q}       |{if_p_then_r}        |{if_q_then_r}        |{and_three}                         |{not_and_three_then_or_r}                              |{variable_true}   |")

'''
Creates a function definition for the proposition p <-> q = (p -> q) * (q -> p).
This truth table proves that "p if and only if q" is the same as "if p then q and if q then p"
Therefore, p <-> q should yield the same result as (p -> q) * (q -> p) for all rows of the truth table.
This function also contains a nested for loop because a nested for loop allows for the iteration of every possible True, False combination
Author: Combination
'''
def numberSix():
    #Prints a line telling the user what table is being shown
    print("6. p <-> q = (p -> q) * (q -> p)")

    #Prints the table header row to separate between columns
    print("|   p   |   q   |  (p -> q)  |  (q -> p)  |(p -> q) * (q -> p)|  p <-> q  |")

    '''
    Start of a nested for loop where the outer loop (for p in (True, False):) will run after the inner loop has been iterated through. 
    This will help create the "p" column of the truth table and allow for use in the boolean expression within
    '''
    for p in (True, False):
        '''
        The inner loop (for q in (True, False):) will iterate many times before progressing to the outer loop. 
        This will help create the "q" column of the truth table and allow for use in the boolean expression within
        '''
        for q in (True, False):
            '''
            Boolean expression that has been derived from the conversion of "p -> q" into "!p + q".
            This is the same as converting if "p then q" into "not p or q".
            This conversion was found on slide 29 of the Propositional Logic slides on Canvas
            '''
            if_p_then_q = not p or q

            '''
            Boolean expression that has been derived from the conversion of "q -> p" into "!q + p".
            This is the same as converting if "q then p" into "not q or p".
            This conversion was found on slide 29 of the Propositional Logic slides on Canvas
            '''
            if_q_then_p = not q or p

            '''
            Boolean expression that has been assigned a variable name.
            This involves taking the two boolean expressions above ((not p or q), (not q or p)) and AND'ing them together
            '''
            andTwo = if_p_then_q and if_q_then_p

            '''
            Boolean expression that has been derived from the conversion of "p <-> q" into "(!p + q) * (!q + p)".
            This is the same as converting if "p if and only if q" into "(not p or q) and (not q or p)".
            This conversion was found on slide 29 of the Propositional Logic slides on Canvas
            '''
            p_if_and_only_if_q = (not p or q) and (not q or p)
                
            #Prints the table row by row segmented by each important step to proving the proposition p <-> q = (p -> q) * (q -> p) correct
            print(f"|{p}   |{q}   |{if_p_then_q}        |{if_q_then_p}        |{andTwo}               |{p_if_and_only_if_q}       |")

#Prints a blank line to allow for better spacing between truth tables
print(" ")

#Prints out the truth table showcasing De Morgan's First Law
dMorgFirst()

#Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 150 repeats the underscore 150 times in the print line
print("_"*150)

#Prints a blank line to allow for better spacing between truth tables
print(" ")

#Prints out the truth table showcasing De Morgan's Second Law
dMorgSecond()

#Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 150 repeats the underscore 150 times in the print line
print("_"*150)

#Prints a blank line to allow for better spacing between truth tables
print(" ")

#Prints out the truth table showcasing the First Associative Law
firstAssociative()

#Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 150 repeats the underscore 150 times in the print line
print("_"*150)

#Prints a blank line to allow for better spacing between truth tables
print(" ")

#Prints out the truth table showcasing the Second Associative Law
secondAssociative()

#Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 150 repeats the underscore 150 times in the print line
print("_"*150)

#Prints a blank line to allow for better spacing between truth tables
print(" ")

#Prints out the truth table showcasing the proposition [(p + q) * (p -> r) * (q -> r)] -> r = T
numberFive()

#Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 150 repeats the underscore 150 times in the print line
print("_"*150)

#Prints a blank line to allow for better spacing between truth tables
print(" ")

#Prints out the truth table showcasing the proposition p <-> q = (p -> q) * (q -> p)
numberSix()

#Prints a separation line to allow for better distinguishing of truth tables. One underscore multiplied by 150 repeats the underscore 150 times in the print line
print("_"*150)

#Prints a blank line to allow for better spacing between truth tables
print(" ")