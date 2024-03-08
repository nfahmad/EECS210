'''
Name of program contained in the file: EECS210_Assignment2.py
Brief description of the program: This program's objective is to prove (true) or disprove (false) six different assertions for the domain of {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
                                  This program's objective is to also find the truth values of P(x,y): x * y = 1. 
                                  The domain of x and y is {1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1}.
Inputs: None
Output: Print out of the name and number of each exercise, followed by the exercise’s output
All collaborators: Omar Mohammed
Other Sources for the Code: Stack Overflow, Real Python, "Predicates and Quantifiers" Canvas Slides
Author's full name: Nabeel Ahmad
Creation date: 09/10/2023
'''

'''
This function will iterate through the given domain and determine if there is a value that is less than 2.
If there is a value less than 2 then the assertion is correct because there is at least a value that proves it correct.
Author: Combination
'''
def question1a():
    #Prints a line telling the user what assertion is being proven
    print('1.a) ∃x P(x), where P(x) is the statement "x<2"\n')

    #This is the given domain
    domain = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    #Creates a target to identify the number that proves the assertion
    target = None

    #Creates a for-loop to iterate through the domain
    for x in domain:
        #Creates a key identifier to determine whether the assertion is correct for the domain
        if x < 2:
            #Reassigns the target to the variable that either proves or disproves the assertion
            target = x

            #Breaks the loop
            break
    
    #If the target has changed, then the assertion has been proven
    if target != None:
        #Prints a line telling the user why the assertion is true
        print(f"This is true, because {target} is less than 2")

        #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
        print("_"*50)
    
    #If the target has not changed, then the assertion has been disproven
    else:
        #Prints a line telling the user the assertion is false
        print(f"This is false")

        #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
        print("_"*50)

'''
This function will iterate through the given domain and determine if there is a value that is greater than 2.
If there is a value greater than 2 then the assertion is false because there is at least a value that proves it incorrect.
Author: Combination
'''
def question1b():
    #Prints a line telling the user what assertion is being proven
    print('1.b) ∀x P(x), where P(x) is the statement "x<2"\n')

    #This is the given domain
    domain = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    #Creates a target to identify the number that disproves the assertion
    target = None

    #Creates a for-loop to iterate through the domain
    for x in domain:
        #Creates a key identifier to determine whether the assertion is correct for the domain
        if x > 2:
            #Reassigns the target to the variable that either proves or disproves the assertion
            target = x

            #Breaks the loop
            break
    
    #If the target has changed, then the assertion has been disproven
    if target != None:
        #Prints a line telling the user why the assertion is false
        print(f"This is false, because {target} is greater than 2")

        #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
        print("_"*50)
    
    #If the target has not changed, then the assertion has been proven
    else:
        #Prints a line telling the user the assertion is true
        print(f"This is true")

        #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
        print("_"*50)

'''
This function will iterate through the given domain and determine if there is a value that is less than 2 or if there is a value greater than 7.
If there is a value less than 2 or greater than 7 then the assertion is true because there is at least a value that proves it correct.
Author: Combination
'''
def question1c():
    #Prints a line telling the user what assertion is being proven
    print('1.c) ∃x (P(x) ∨ Q(x)) where P(x) is the statement "x<2" and where Q(x) is the statement "x>7"\n')

    #This is the given domain
    domain = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    #Creates a target to identify the number that proves the assertion
    target = None

    #Creates a for-loop to iterate through the domain
    for x in domain:
        #Creates a key identifier to determine whether the assertion is correct for the domain
        if x < 2 or x > 7:
            #Reassigns the target to the variable that either proves or disproves the assertion
            target = x

            #Breaks the loop
            break
    
    #If the target has changed, then the assertion has been proven
    if target != None:
        #Prints a line telling the user why the assertion is true
        print(f"This is true, because {target} is either less than 2 or it is greater than 7")

        #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
        print("_"*50)

    #If the target has not changed, then the assertion has been disproven
    else:
        #Prints a line telling the user the assertion is false
        print(f"This is false")

        #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
        print("_"*50)

'''
This function will iterate through the given domain and determine if there is a value that is greater than 2 or if there is a value less than 7.
If there is a value greater than 2 or less than 7 then the assertion is false because there is at least a value that proves it incorrect.
Author: Combination
'''
def question1d():
    #Prints a line telling the user what assertion is being proven
    print('1.d) ∀x (P(x) ∨ Q(x)) where P(x) is the statement "x<2" and where Q(x) is the statement "x>7"\n')

    #This is the given domain
    domain = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    #Creates a target to identify the number that disproves the assertion
    target = None

    #Creates a for-loop to iterate through the domain
    for x in domain:
        #Creates a key identifier to determine whether the assertion is correct for the domain
        if x > 2 and x < 7:
            #Reassigns the target to the variable that either proves or disproves the assertion
            target = x
            
            #Breaks the loop
            break
    
    #If the target has changed, then the assertion has been disproven
    if target != None:
        #Prints a line telling the user why the assertion is false
        print(f"This is false, because {target} is greater than 2 and less than 7")

        #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
        print("_"*50)

    #If the target has not changed, then the assertion has been proven
    else:
        #Prints a line telling the user the assertion is true
        print(f"This is true")

        #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
        print("_"*50)

'''
This function will iterate through the given domain and determine if there is a value that is less than 5.
Then it will determine, through De Morgan's Law for the existential quantifier, if ¬∃x P(x) = ∀x ¬P(x).
Where a negation of the left side of the equation (¬∃x P(x)),
will create an instance where the function has to check if x is greater than or equal to 5 for the right side of the equation (∀x ¬P(x)).
Author: Combination
'''
def question1e():
    #Prints a line telling the user what assertion is being proven
    print('1.e) Prove De Morgan’s Law for the Existential Quantifier where P(x) is the statement "x<5"')
    
    #Prints a line telling the user how De Morgan's Law for the Existential Quantifier looks
    print('     Where ¬∃x P(x) = ∀x ¬P(x)\n')

    #This is the given domain
    domain = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    #Creates a list to check for the existential side of the equation
    existentialList = []

    #Creates a list to check for the universal side of the equation
    universalList = []

    #Since the function is proving this law to be true, there is a print statement to be followed up by the evidence
    print("This is true because:\n")

    #Creates a for-loop to iterate through the domain
    for x in domain:
        #Creates a key identifier to determine whether the assertion is correct for the domain
        if x < 5:
            #Appends false to the existential list if x is less than 5, since this proves it to be false
            existentialList.append(False)
        
        #If the x is less than 5, then the assertion is true for the existential side
        else:
            #Appends true to the existential list if x is not less than 5, since this proves it to be true
            existentialList.append(True)
        
        #Creates a key identifier to determine whether the assertion is correct for the domain
        if x >= 5:
            #Appends true to the universal list if x is greater than or equal to 5, since this proves it to be true
            universalList.append(True)

        #If the x is less than 5, then the assertion is false for the universal side
        else:
            #Appends false to the universal list if x is less than 5, since this proves it to be false
            universalList.append(False)
    
    #If both sides are equal to each other this will run
    if existentialList == universalList:
        #The domain is 10 variables long, therefore the range is 10
        for x in range(10):
            #Prints a line telling the user why the assertion is true
            print(f"For x = {x + 1}, ¬∃x P(x) is {existentialList[x]} and ∀x ¬P(x) is {universalList[x]}")
    
    #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
    print("_"*50)

'''
This function will iterate through the given domain and determine if there is a value that is less than 5.
Then it will determine, through De Morgan's Law for the existential quantifier, if ∀x ¬P(x) = ¬∃x P(x).
Where a negation of the left side of the equation (∀x ¬P(x)),
will create an instance where the function has to check if x less than 5 for the right side of the equation (¬∃x P(x)).
Author: Combination
'''
def question1f():
    #Prints a line telling the user what assertion is being proven
    print('1.f) Prove De Morgan’s Law for the Universal Quantifier where P(x) is the statement "x<5"')

    #Prints a line telling the user how De Morgan's Law for the Universal Quantifier looks
    print('     Where ∀x ¬P(x) = ¬∃x P(x)\n')

    #This is the given domain
    domain = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    #Creates a list to check for the existential side of the equation
    existentialList = []

    #Creates a list to check for the universal side of the equation
    universalList = []

    #Since the function is proving this law to be true, there is a print statement to be followed up by the evidence
    print("This is true because:\n")

    #Creates a for-loop to iterate through the domain
    for x in domain:
        #Creates a key identifier to determine whether the assertion is correct for the domain
        if x < 5:
            #Appends false to the existential list if x is less than 5, since this proves it to be false
            existentialList.append(False)

        #If the x is less than 5, then the assertion is true for the existential side
        else:
            #Appends true to the existential list if x is not less than 5, since this proves it to be true
            existentialList.append(True)
        
        #Creates a key identifier to determine whether the assertion is correct for the domain
        if x >= 5:
            #Appends true to the existential list if x is not less than 5, since this proves it to be true
            universalList.append(True)

        #If the x is less than 5, then the assertion is false for the universal side
        else:
            #Appends false to the universal list if x is less than 5, since this proves it to be false
            universalList.append(False)
    
    #If both sides are equal to each other this will run
    if existentialList == universalList:
        #The domain is 10 variables long, therefore the range is 10
        for x in range(10):
            #Prints a line telling the user why the assertion is true
            print(f"For x = {x + 1}, ∀x ¬P(x) is {universalList[x]} and ¬∃x P(x) is {existentialList[x]}")

    #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
    print("_"*50)

#Prints the output showcasing question 1.a
question1a()

#Prints the output showcasing question 1.b
question1b()

#Prints the output showcasing question 1.c
question1c()

#Prints the output showcasing question 1.d
question1d()

#Prints the output showcasing question 1.e
question1e()

#Prints the output showcasing question 1.f
question1f()

'''
This function will iterate through the given domain for x and y and determine if there is a pair where x * y does not equal 1.
This will prove whether this assertion is true or false.
Author: Combination
'''
def question2a():
    #Prints a line telling the user what assertion is being proven
    print("2.a) Prove whether ∀x∀yP(x,y) is true or false")

    #Tells the user the rule for P(x, y)
    print("     Where P(x, y): x * y = 1\n")

    #This is the given domain
    domain = {1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1}

    #Creates a target to identify the number that disproves the assertion
    targetx = None

    #Creates a target to identify the number that disproves the assertion
    targety = None

    #Creates a nested for-loop to iterate through the domain
    for x in domain:
        #Creates a for-loop to iterate through the domain
        for y in domain:
            #Creates a key identifier to determine whether the assertion is correct for the domain
            if x * y != 1:
                #Stores the value as targetx in order to identify the number that disproves the assertion
                targetx = x

                #Stores the value as targety in order to identify the number that disproves the assertion
                targety = y

                #Breaks the loop
                break
    
    #This will identify whether the assertion is true or false
    if targetx != None and targety != None:
        #Prints a line telling the user why the assertion is false
        print(f"The assertion is false because {targetx} * {targety} does not equal 1")
    
    #This will run if the assertion is true
    else:
        #Prints a line telling the user why the assertion is true
        print(f"The assertion is true because {targetx} * {targety} equal 1")
    
    #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
    print("_"*50)

'''
This function will iterate through the given domain for x and y and determine if there is a pair where x * y does not equal 1.
This will prove whether this assertion is true or false.
Author: Combination
'''
def question2b():
    #Prints a line telling the user what assertion is being proven
    print("2.b) Prove whether ∀x∃yP(x,y) is true or false")

    #Tells the user the rule for P(x, y)
    print("     Where P(x, y): x * y = 1\n")

    #This is the given domain
    domain = {1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1}

    #Creates a list to store the value pairs that are true
    true_values = []

    #Creates a list to store the value pairs that are false
    false_values = []

    #Creates a list to store whether the assertion is true or false
    true_or_false = []

    #Creates a nested for-loop to iterate through the domain
    for x in domain:
        #Creates a for-loop to iterate through the domain
        for y in domain:
            #Creates a key identifier to determine whether the assertion is correct for the domain
            if x * y == 1:
                #Appends the true values list with the true values
                true_values.append((x,y))

                #Appends the true or false list with true
                true_or_false.append(True)

            #Runs if assertion is false for this pair
            else:
                #Appends the false values list with the false values
                false_values.append((x,y))

                #Appends the true or false list with false
                true_or_false.append(False)
    
    #This will identify whether the assertion is true or false
    if any(true_or_false) == False:
        #Prints a line telling the user the assertion is false
        print("The assertion is false for (x,y) values:\n")

        #Creates a for loop to iterate through the false_values list
        for values in false_values:
            #Prints the list of values
            print(values)
    
    #If the true_or_false list has true, this will run
    else:
        #Prints a line telling the user the assertion is true
        print("The assertion is true for (x,y) values:\n")

        #Creates a for loop to iterate through the true_values list
        for values in true_values:
            #Prints the list of values
            print(values)

    #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
    print("_"*50)

'''
This function will iterate through the given domain for x and y and determine if there is a pair where x * y does not equal 1.
This will prove whether this assertion is true or false.
Author: Combination
'''
def question2c():
    #Prints a line telling the user what assertion is being proven
    print("2.c) Prove whether ∀y∃xP(x,y) is true or false")

    #Tells the user the rule for P(x, y)
    print("     Where P(x, y): x * y = 1\n")

    #This is the given domain
    domain = {1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1}

    #Creates a list to store the value pairs that are true
    true_values = []

    #Creates a list to store the value pairs that are false
    false_values = []

    #Creates a list to store whether the assertion is true or false
    true_or_false = []

    #Creates a nested for-loop to iterate through the domain
    for y in domain:
        #Creates a for-loop to iterate through the domain
        for x in domain:
            #Creates a key identifier to determine whether the assertion is correct for the domain
            if y * x == 1:
                #Appends the true values list with the true values
                true_values.append((y,x))

                #Appends the true or false list with true
                true_or_false.append(True)

            else:
                #Appends the false values list with the false values
                false_values.append((x,y))

                #Appends the true or false list with false
                true_or_false.append(False)

    #This will identify whether the assertion is true or false
    if any(true_or_false) == False:
        print("The assertion is false for (x,y) values:\n")

        #Creates a for loop to iterate through the false_values list
        for values in false_values:
            #Prints the list of values
            print(values)
    
    else:
        print("The assertion is true for (x,y) values:\n")

        #Creates a for loop to iterate through the true_values list
        for values in true_values:
            #Prints the list of values
            print(values)

    #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
    print("_"*50)

'''
This function will iterate through the given domain for x and y and determine if there is a pair where x * y does not equal 1.
This will prove whether this assertion is true or false.
Author: Combination
'''
def question2d():
    #Prints a line telling the user what assertion is being proven
    print("2.d) Prove whether ∃x∀yP(x,y) is true or false")

    #Tells the user the rule for P(x, y)
    print("     Where P(x, y): x * y = 1\n")

    #This is the given domain
    domain = {1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1}

    #Creates a list to store the value pairs that are false
    false_values = []

    #Creates a list to store the
    targetxy = []

    #Creates a nested for-loop to iterate through the domain
    for x in domain:
        #Creates a for-loop to iterate through the domain
        for y in domain:
            #Creates a key identifier to determine whether the assertion is correct for the domain
            if x * y != 1:
                #Appends the false values list with the false values
                false_values.append((x,y))

                #Appends the targetxy list
                targetxy.append(x)

                #Breaks the loop
                break

    #This will identify whether the assertion is true or false
    if targetxy == domain:
        #Prints a line telling the user the assertion is true
        print("The assertion is true for (x,y) values:\n")
    
    else:
        #Prints a line telling the user the assertion is false
        print("The assertion is false for (x,y) values:\n")

        #Creates a for loop to iterate through the false_values list
        for values in false_values:
            #Prints the list of values
            print(values)

    #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
    print("_"*50)

'''
This function will iterate through the given domain for x and y and determine if there is a pair where x * y does not equal 1.
This will prove whether this assertion is true or false.
Author: Combination
'''
def question2e():
    #Prints a line telling the user what assertion is being proven
    print("2.e) Prove whether ∃y∀xP(x,y) is true or false")

    #Tells the user the rule for P(x, y)
    print("     Where P(x, y): x * y = 1\n")

    #This is the given domain
    domain = {1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1}

    #Creates a list to store the value pairs that are false
    false_values = []

    targetxy = []

    #Creates a nested for-loop to iterate through the domain
    for y in domain:
        #Creates a for-loop to iterate through the domain
        for x in domain:
            #Creates a key identifier to determine whether the assertion is correct for the domain
            if y * x != 1:
                #Appends the false values list with the false values
                false_values.append((y,x))

                #Appends the targetxy list
                targetxy.append(y)

                #Breaks the loop
                break
    
    #This will identify whether the assertion is true or false
    if targetxy == domain:
        #Prints a line telling the user the assertion is true
        print("The assertion is true for (x,y) values:\n")
    
    else:
        #Prints a line telling the user the assertion is false
        print("The assertion is false for (x,y) values:\n")

        #Creates a for loop to iterate through the false_values list
        for values in false_values:
            #Prints the list of values
            print(values)

    #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
    print("_"*50)

'''
This function will iterate through the given domain for x and y and determine if there is a pair where x * y does not equal 1.
This will prove whether this assertion is true or false.
Author: Combination
'''
def question2f():
    #Prints a line telling the user what assertion is being proven
    print("2.f) Prove whether ∃x∃yP(x,y) is true or false")

    #Tells the user the rule for P(x, y)
    print("     Where P(x, y): x * y = 1\n")

    #This is the given domain
    domain = {1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1}

    #Creates a list to store the value pairs that are true
    true_values = []

    #Creates a list to store the value pairs that are false
    false_values = []

    #Creates a list to store whether the assertion is true or false
    true_or_false = []

    #Creates a nested for-loop to iterate through the domain
    for x in domain:
        #Creates a for-loop to iterate through the domain
        for y in domain:
            #Creates a key identifier to determine whether the assertion is correct for the domain
            if x * y == 1:
                #Appends the true values list with the true values
                true_values.append((x,y))
                
                #Appends the true_or_false list with true
                true_or_false.append(True)

            else:
                #Appends the false values list with the false values
                false_values.append((x,y))
                
                #Appends the true_or_false list with false
                true_or_false.append(False)
    
    #This will identify whether the assertion is true or false
    if any(true_or_false) == False:
        #Prints a line telling the user the assertion is false
        print("The assertion is false for (x,y) values:\n")

        #Creates a for loop to iterate through the false_values list
        for values in false_values:
            #Prints the list of values
            print(values)
    
    #Runs if the assertion is true
    else:
        #Prints a line telling the user the assertion is true
        print("The assertion is true for (x,y) values:\n")

        #Creates a for loop to iterate through the false_values list
        for values in true_values:
            #Prints the list of values
            print(values)

    #Prints a separation line. One underscore multiplied by 50 repeats the underscore 50 times in the print line
    print("_"*50)

#Prints the output showcasing question 2.a
question2a()

#Prints the output showcasing question 2.b
question2b()

#Prints the output showcasing question 2.c
question2c()

#Prints the output showcasing question 2.d
question2d()

#Prints the output showcasing question 2.e
question2e()

#Prints the output showcasing question 2.f
question2f()