'''
Name of program contained in the file: EECS210_Assignment5.py
Brief description of the program: Determines whether the given relation is a function or not, and if it is a function, whether it is injective, surjective,
                                  or bijective, and if it is bijective, what is the inverse function.
                                  Determines the greatest common divisor of two integers, gcd(a,b) using the Euclidean Algorithm.
                                  Expresses gcd(a, b) as a linear combination: gcd(a, b) = sa + tb, where s and t are Bézout coefficients of a and b,
                                  using the Euclidean Algorithm (Method 1).
                                  Expresses gcd(a, b) as a linear combination: gcd(a, b) = sa + tb, where s and t are Bézout coefficients of a and b,
                                  using the extended Euclidean Algorithm (Method 2).
Inputs: None
Output: Print out the exercise number followed by the exercise’s output
All collaborators: Omar Mohammed, Arnav Jain, Yaeesh Mukadam
Other Sources for the Code: Stack Overflow, W3Schools, GeeksForGeeks "Functions" Canvas Slides
Author's full name: Nabeel Ahmad
Creation date: 10/24/2023
'''

'''
Creates the set of inputs A for use in determining if the relation is a function,
if it is surjective, injective, or bijective. And if it is bijective, if it is inverse
'''
oneaA = {"a","b","c","d"}
onebA = {"a","b","c","d"}
onecA = {"a","b","c","d"}
onedA = {"a","b","c","d"}
oneeA = {"a","b","c"}
onefA = {"a","b","c","d"}
onegA = {"a","b","c","d"}
onehA = {"a","b","c","d"}
oneiA = {"a","b","c"}

'''
Creates the set of inputs B for use in determining if the relation is a function,
if it is surjective, injective, or bijective. And if it is bijective, if it is inverse
'''
oneaB = {"v","w","x","y","z"}
onebB = {"x","y","z"}
onecB = {"w","x","y","z"}
onedB = {1,2,3,4,5}
oneeB = {1,2,3,4}
onefB = {1,2,3}
onegB = {1,2,3,4}
onehB = {1,2,3,4}
oneiB = {1,2,3,4}

'''
Creates the set of relations f for use in determining if the relation is a function,
if it is surjective, injective, or bijective. And if it is bijective, if it is inverse
'''
oneaf = {("a","z"),("b","y"),("c","x"),("d","w")}
onebf = {("a","z"),("b","y"),("c","x"),("d","z")}
onecf = {("a","z"),("b","y"),("c","x"),("d","w")}
onedf = {("a",4),("b",5),("c",1),("d",3)}
oneef = {("a",3),("b",4),("c",1)}
oneff = {("a",2),("b",1),("c",3),("d",2)}
onegf = {("a",4),("b",1),("c",3),("d",2)}
onehf = {("a",2),("b",1),("c",2),("d",3)}
oneif = {("a",2),("b",1),("a",4),("c",3)}

#Creates the ordered pairs for use in determining the greatest common divisor
twoa = (414,662)
twob = (6,14)
twoc = (24,36)
twod = (12,42)
twoe = (252,198)

'''
This function will run through an empty domain set,
and determine if the relation is a function. If it is a function,
it will add it to the domain set
Author: Combination
'''
def determineFunction(f):
    domain = set()
    #Iterate through every pair in the relation
    for pair in f:
        value1, value2 = pair
        #Check if the first element is already in the domain
        if value1 in domain:
            return False
        #Add that first element to the domain set
        domain.add(value1)
    #If every first element is unique, it is a function
    return True

'''
This function will run through an empty set of possible values,
and determine if the function is injective. If it is injective,
it will add it to the set of possible values
Author: Combination
'''
def determineInjective(f):
    possibleValues = set()
    #Iterate through every pair in the relation
    for pair in f:
        value1, value2 = pair
        #Check if the second element is already a possible value
        if value2 in possibleValues:
            return False
        #Add that second element to the set of possible values
        possibleValues.add(value2)
    #If every second element is unique, it is injective
    return True

'''
This function will run through a set of possible values that contains the second elements of the relation,
and determine if the function is surjective. If it is surjective it will return True
Author: Combination
'''
def determineSurjective(f,B):
    #Creates a set to store the second elements of the relation
    possibleValues = {pair[1] for pair in f}
    #Return a statement where the possible values of the second element is equal to the second elements B
    return possibleValues == B

'''
This function will run through the three previously defined function and if all return True for those three functions,
then the passed through function is bijective
Author: Combination
'''
def determineBijective(f,A,B):
    #Check if the relation is a function, injective, and surjective
    return determineFunction(f) and determineInjective(f) and determineSurjective(f,B)

'''
This function will find the inverse relation of the passed in relation.
This will only run in the case of determineBijective returning True
Author: Combination
'''
def findInverse(f):
    #This will swap the elements in each pair to create the inverse relation
    inverse = [(pair[1], pair[0]) for pair in f]
    #Returns the inverse relation
    return inverse

'''
This function will perform question 1.a
Author: Combination
'''
def question1a():
    print(f"1.a) A = {oneaA}, B = {oneaB}, f = {oneaf}")
    #If the passed in relation is a function, then it will state so
    if determineFunction(oneaf) == True:
        print("a) The relation is a function")
    else:
        print("a) The relation is not a function")
    #Determines if the function is injective
    oneInjective = determineInjective(oneaf)
    #Determines if the function is surjective
    oneSurjective = determineSurjective(oneaf,oneaB)
    #Determines if the function is bijective
    oneBijective = determineBijective(oneaf,oneaA,oneaB)
    #If the passed in function is injective, then it will state so
    if oneInjective == True:
        print("b) The function is injective")
    else:
        print("b) The function is not injective")
    #If the passed in function is surjective, then it will state so
    if oneSurjective == True:
        print("   The function is surjective")
    else:
        print("   The function is not surjective")
    #If the passed in function is bijective, then it will state so
    if oneBijective == True:
        print("   The function is bijective")
    else:
        print("   The function is not bijective")
    #If the passed in function is bijective, then it will display the inverse
    if oneBijective == True:
        print(f"c) The function is bijective, therefore the inverse function is {findInverse(oneaf)}")
    else:
        print("c) The function is not bijective, therefore there is no inverse")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 1.b
Author: Combination
'''
def question1b():
    print(f"1.b) A = {onebA}, B = {onebB}, f = {onebf}")
    #If the passed in relation is a function, then it will state so
    if determineFunction(onebf) == True:
        print("a) The relation is a function")
    else:
        print("a) The relation is not a function")
    #Determines if the function is injective
    oneInjective = determineInjective(onebf)
    #Determines if the function is surjective
    oneSurjective = determineSurjective(onebf,onebB)
    #Determines if the function is bijective
    oneBijective = determineBijective(onebf,onebA,onebB)
    #If the passed in function is injective, then it will state so
    if oneInjective == True:
        print("b) The function is injective")
    else:
        print("b) The function is not injective")
    #If the passed in function is surjective, then it will state so
    if oneSurjective == True:
        print("   The function is surjective")
    else:
        print("   The function is not surjective")
    #If the passed in function is bijective, then it will state so
    if oneBijective == True:
        print("   The function is bijective")
    else:
        print("   The function is not bijective")
    #If the passed in function is bijective, then it will display the inverse
    if oneBijective == True:
        print(f"c) The function is bijective, therefore the inverse function is {findInverse(onebf)}")
    else:
        print("c) The function is not bijective, therefore there is no inverse")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 1.c
Author: Combination
'''
def question1c():
    print(f"1.c) A = {onecA}, B = {onecB}, f = {onecf}")
    #If the passed in relation is a function, then it will state so
    if determineFunction(onecf) == True:
        print("a) The relation is a function")
    else:
        print("a) The relation is not a function")
    #Determines if the function is injective
    oneInjective = determineInjective(onecf)
    #Determines if the function is surjective
    oneSurjective = determineSurjective(onecf,onecB)
    #Determines if the function is bijective
    oneBijective = determineBijective(onecf,onecA,onecB)
    #If the passed in function is injective, then it will state so
    if oneInjective == True:
        print("b) The function is injective")
    else:
        print("b) The function is not injective")
    #If the passed in function is surjective, then it will state so
    if oneSurjective == True:
        print("   The function is surjective")
    else:
        print("   The function is not surjective")
    #If the passed in function is bijective, then it will state so
    if oneBijective == True:
        print("   The function is bijective")
    else:
        print("   The function is not bijective")
    #If the passed in function is bijective, then it will display the inverse
    if oneBijective == True:
        print(f"c) The function is bijective, therefore the inverse function is {findInverse(onecf)}")
    else:
        print("c) The function is not bijective, therefore there is no inverse")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 1.d
Author: Combination
'''
def question1d():
    print(f"1.d) A = {onedA}, B = {onedB}, f = {onedf}")
    #If the passed in relation is a function, then it will state so
    if determineFunction(onedf) == True:
        print("a) The relation is a function")
    else:
        print("a) The relation is not a function")
    #Determines if the function is injective
    oneInjective = determineInjective(onedf)
    #Determines if the function is surjective
    oneSurjective = determineSurjective(onedf,onedB)
    #Determines if the function is bijective
    oneBijective = determineBijective(onedf,onedA,onedB)
    #If the passed in function is injective, then it will state so
    if oneInjective == True:
        print("b) The function is injective")
    else:
        print("b) The function is not injective")
    #If the passed in function is surjective, then it will state so
    if oneSurjective == True:
        print("   The function is surjective")
    else:
        print("   The function is not surjective")
    #If the passed in function is bijective, then it will state so
    if oneBijective == True:
        print("   The function is bijective")
    else:
        print("   The function is not bijective")
    #If the passed in function is bijective, then it will display the inverse
    if oneBijective == True:
        print(f"c) The function is bijective, therefore the inverse function is {findInverse(onedf)}")
    else:
        print("c) The function is not bijective, therefore there is no inverse")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 1.e
Author: Combination
'''
def question1e():
    print(f"1.e) A = {oneeA}, B = {oneeB}, f = {oneef}")
    #If the passed in relation is a function, then it will state so
    if determineFunction(oneef) == True:
        print("a) The relation is a function")
    else:
        print("a) The relation is not a function")
    #Determines if the function is injective
    oneInjective = determineInjective(oneef)
    #Determines if the function is surjective
    oneSurjective = determineSurjective(oneef,oneeB)
    #Determines if the function is bijective
    oneBijective = determineBijective(oneef,oneeA,oneeB)
    #If the passed in function is injective, then it will state so
    if oneInjective == True:
        print("b) The function is injective")
    else:
        print("b) The function is not injective")
    #If the passed in function is surjective, then it will state so
    if oneSurjective == True:
        print("   The function is surjective")
    else:
        print("   The function is not surjective")
    #If the passed in function is bijective, then it will state so
    if oneBijective == True:
        print("   The function is bijective")
    else:
        print("   The function is not bijective")
    #If the passed in function is bijective, then it will display the inverse
    if oneBijective == True:
        print(f"c) The function is bijective, therefore the inverse function is {findInverse(oneef)}")
    else:
        print("c) The function is not bijective, therefore there is no inverse")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 1.f
Author: Combination
'''
def question1f():
    print(f"1.f) A = {onefA}, B = {onefB}, f = {oneff}")
    #If the passed in relation is a function, then it will state so
    if determineFunction(oneff) == True:
        print("a) The relation is a function")
    else:
        print("a) The relation is not a function")
    #Determines if the function is injective
    oneInjective = determineInjective(oneff)
    #Determines if the function is surjective
    oneSurjective = determineSurjective(oneff,onefB)
    #Determines if the function is bijective
    oneBijective = determineBijective(oneff,onefA,onefB)
    #If the passed in function is injective, then it will state so
    if oneInjective == True:
        print("b) The function is injective")
    else:
        print("b) The function is not injective")
    #If the passed in function is surjective, then it will state so
    if oneSurjective == True:
        print("   The function is surjective")
    else:
        print("   The function is not surjective")
    #If the passed in function is bijective, then it will state so
    if oneBijective == True:
        print("   The function is bijective")
    else:
        print("   The function is not bijective")
    #If the passed in function is bijective, then it will display the inverse
    if oneBijective == True:
        print(f"c) The function is bijective, therefore the inverse function is {findInverse(oneff)}")
    else:
        print("c) The function is not bijective, therefore there is no inverse")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 1.g
Author: Combination
'''
def question1g():
    print(f"1.g) A = {onegA}, B = {onegB}, f = {onegf}")
    #If the passed in relation is a function, then it will state so
    if determineFunction(onegf) == True:
        print("a) The relation is a function")
    else:
        print("a) The relation is not a function")
    #Determines if the function is injective
    oneInjective = determineInjective(onegf)
    #Determines if the function is surjective
    oneSurjective = determineSurjective(onegf,onegB)
    #Determines if the function is bijective
    oneBijective = determineBijective(onegf,onegA,onegB)
    #If the passed in function is injective, then it will state so
    if oneInjective == True:
        print("b) The function is injective")
    else:
        print("b) The function is not injective")
    #If the passed in function is surjective, then it will state so
    if oneSurjective == True:
        print("   The function is surjective")
    else:
        print("   The function is not surjective")
    #If the passed in function is bijective, then it will state so
    if oneBijective == True:
        print("   The function is bijective")
    else:
        print("   The function is not bijective")
    #If the passed in function is bijective, then it will display the inverse
    if oneBijective == True:
        print(f"c) The function is bijective, therefore the inverse function is {findInverse(onegf)}")
    else:
        print("c) The function is not bijective, therefore there is no inverse")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 1.h
Author: Combination
'''
def question1h():
    print(f"1.h) A = {onehA}, B = {onehB}, f = {onehf}")
    #If the passed in relation is a function, then it will state so
    if determineFunction(onehf) == True:
        print("a) The relation is a function")
    else:
        print("a) The relation is not a function")
    #Determines if the function is injective
    oneInjective = determineInjective(onehf)
    #Determines if the function is surjective
    oneSurjective = determineSurjective(onehf,onehB)
    #Determines if the function is bijective
    oneBijective = determineBijective(onehf,onehA,onehB)
    #If the passed in function is injective, then it will state so
    if oneInjective == True:
        print("b) The function is injective")
    else:
        print("b) The function is not injective")
    #If the passed in function is surjective, then it will state so
    if oneSurjective == True:
        print("   The function is surjective")
    else:
        print("   The function is not surjective")
    #If the passed in function is bijective, then it will state so
    if oneBijective == True:
        print("   The function is bijective")
    else:
        print("   The function is not bijective")
    #If the passed in function is bijective, then it will display the inverse
    if oneBijective == True:
        print(f"c) The function is bijective, therefore the inverse function is {findInverse(onehf)}")
    else:
        print("c) The function is not bijective, therefore there is no inverse")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 1.i
Author: Combination
'''
def question1i():
    print(f"1.i) A = {oneiA}, B = {oneiB}, f = {oneif}")
    #If the passed in relation is a function, then it will state so
    if determineFunction(oneif) == True:
        print("a) The relation is a function")
    else:
        print("a) The relation is not a function")
    #Determines if the function is injective
    oneInjective = determineInjective(oneif)
    #Determines if the function is surjective
    oneSurjective = determineSurjective(oneif,oneiB)
    #Determines if the function is bijective
    oneBijective = determineBijective(oneif,oneiA,oneiB)
    #If the passed in function is injective, then it will state so
    if oneInjective == True:
        print("b) The function is not injective")
    else:
        print("b) The function is injective")
    #If the passed in function is surjective, then it will state so
    if oneSurjective == True:
        print("   The function is not surjective")
    else:
        print("   The function is surjective")
    #If the passed in function is bijective, then it will state so
    if oneBijective == True:
        print("   The function is bijective")
    else:
        print("   The function is not bijective")
    #If the passed in function is bijective, then it will display the inverse
    if oneBijective == True:
        print(f"c) The function is bijective, therefore the inverse function is {findInverse(oneif)}")
    else:
        print("c) The function is not bijective, therefore there is no inverse")
    #Prints a separation line
    print("_"*120)
'''
This function will find the greatest common divisor of (a,b),
and it will do so using the Euclidean Algorithm
Author: Combination 
'''
def calculateGCD(a, b):
    #This will store the steps that the function runs through
    steps = []
    #While b is not 0, the loop will continue and append the current step to the list
    while b:
        steps.append(f"{a}/{b} = {a // b} R {a % b}")
        a,b = b,a%b
    #This will return the greatest common divisor and the list of steps it took to get to it
    return a,steps

'''
This function will perform question 2.a
Author: Combination
'''
def question2a():
    print("2.a) ")
    #Creates a step counter
    step_number = 0
    #Unpacks a and b from the ordered pair
    a,b = twoa
    #Calculates the greatest common divisor
    gcd,gcd_steps = calculateGCD(a,b)
    #Displays the steps the program took to get to the greatest common divisor
    for step in gcd_steps[1:]:
        step_number += 1
        print(f"Step {step_number}. {step}")
    #Prints the gcd in the specified form
    print(f"Finally, gcd({a}, {b}) = {gcd}")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 2.b
Author: Combination
'''
def question2b():
    print("2.b) ")
    #Creates a step counter
    step_number = 0
    #Unpacks a and b from the ordered pair
    a,b = twob
    #Calculates the greatest common divisor
    gcd,gcd_steps = calculateGCD(a,b)
    #Displays the steps the program took to get to the greatest common divisor
    for step in gcd_steps[1:]:
        step_number += 1
        print(f"Step {step_number}. {step}")
    #Prints the gcd in the specified form
    print(f"Finally, gcd({a}, {b}) = {gcd}")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 2.c
Author: Combination
'''
def question2c():
    print("2.c) ")
    #Creates a step counter
    step_number = 0
    #Unpacks a and b from the ordered pair
    a,b = twoc
    #Calculates the greatest common divisor
    gcd,gcd_steps = calculateGCD(a,b)
    #Displays the steps the program took to get to the greatest common divisor
    for step in gcd_steps[1:]:
        step_number += 1
        print(f"Step {step_number}. {step}")
    #Prints the gcd in the specified form
    print(f"Finally, gcd({a}, {b}) = {gcd}")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 2.d
Author: Combination
'''
def question2d():
    print("2.d) ")
    #Creates a step counter
    step_number = 0
    #Unpacks a and b from the ordered pair
    a,b = twod
    #Calculates the greatest common divisor
    gcd,gcd_steps = calculateGCD(a,b)
    #Displays the steps the program took to get to the greatest common divisor
    for step in gcd_steps[1:]:
        step_number += 1
        print(f"Step {step_number}. {step}")
    #Prints the gcd in the specified form
    print(f"Finally, gcd({a}, {b}) = {gcd}")
    #Prints a separation line
    print("_"*120)

'''
This function will perform question 2.e
Author: Combination
'''
def question2e():
    print("2.e) ")
    #Creates a step counter
    step_number = 0
    #Unpacks a and b from the ordered pair
    a,b = twoe
    #Calculates the greatest common divisor
    gcd,gcd_steps = calculateGCD(a,b)
    #Displays the steps the program took to get to the greatest common divisor
    for step in gcd_steps:
        step_number += 1
        print(f"Step {step_number}. {step}")
    #Prints the gcd in the specified form
    print(f"Finally, gcd({a}, {b}) = {gcd}")
    #Prints a separation line
    print("_"*120)

'''
This function will express gcd(a,b) as a linear combination: 
gcd(a,b) = sa + tb, where s and t are Bézout coefficients of a and b, using the Euclidean Algorithm
Author: Combination
'''
def euclidianAlgorithmMethodOne(a, b):
    maximum = max(a,b)
    minimum = min(a,b)
    #Initialize the remainder
    remainder = 0
    #Initialize a list to store the steps
    steps = []
    #Starts a loop to run until the minimum is 0
    while minimum > 0:
        #Get the quotient and remainder of the maximum and minimum
        quotient, remainder = divmod(maximum,minimum)
        #Add the step to the list of steps
        steps.append(([maximum,minimum,quotient,remainder]))

        print(f"{maximum} = {minimum} * {quotient} + {remainder}")
        #Set the maximum to the minimum and the minimum to the remainder
        maximum,minimum = minimum,remainder
    print("\nBackward Steps:")
    #Remove the last step
    steps.pop()
    #Reverse the list of steps
    steps.reverse()
    #The ending step is the first step in the list since it is now reversed
    end_result = steps[0]
    s = 1
    #Set the final a, b and q to respective values in the final step.
    final = end_result[3]
    ending_a = end_result[0]
    ending_b = end_result[1]
    ending_q = end_result[2]
    #Loop through each step except the first one
    for a,b,t,r in steps[1:]:
        print(f"{final} = {s} * {ending_a} - {ending_q} * {ending_b}")
        '''
        If the remainder is equal to the ending b, then the index is 1, 
        if the remainder is equal to the final a, then the index to 0, 
        otherwise set the index to -1
        '''
        index = 1 if ending_b == r else 0 if ending_a == r else - 1
        #If the index is one this will run
        if index == 1:
            print(f"{final} = {s} * {ending_a} - {ending_q} * ({a} - {t} * {b})")
            s = ending_q*t+s
            ending_b = a
        #If the index is zero this will run
        elif index == 0:
            print(f"{final} = {s} * ({a} - {t} * {b}) - {ending_q} * {ending_b}")
            ending_q = s*t+ending_q
            ending_a = a
    print(f"{final} = {s} * {ending_a} - {ending_q} * {ending_b}")
    #Return s and the negative ending q since the equation is gcd = s * a - q * b
    return s,-ending_q

'''
This function will perform question 3
Author: Combination
'''
def question3():
    inputs = (414, 662), (6, 14),  (24, 36), (12, 42), (252, 198)
    questionPart = ["a", "b", "c", "d", "e"]
    #This will loop through the inputs and print their respective outputs
    for a, b in enumerate(inputs):
        print(f'3.{questionPart[a]}) ')
        print("Product Sum:")
        #Runs the Euclidian Algorithm (Method 1) and also prints the steps backwards
        euclidianAlgorithmMethodOne(b[0], b[1])
        #Prints a separation line
        print("_"*120)

'''
This function will express gcd(a,b) as a linear combination: 
gcd(a,b) = sa + tb, where s and t are Bézout coefficients of a and b, using the extended Euclidean Algorithm (Method 2)
Author: Combination
'''
def euclidianAlgorithmMethodTwo(a, b):
    #Initializes the coefficients s0, s1, t0, and t1
    s0,s1,t0,t1 = 1,0,0,1
    #Determines which number is larger and smaller
    maximum = max(a,b)
    minimum = min(a,b)
    #Creates a list to store quotients
    quotient_list =[]
    #This will find the greatest common divisor while the minimum does not equal 0
    while minimum != 0:
        #This will the remainder
        remainder = maximum%minimum
        #This will append the quotient to quotient_list
        quotient_list.append(maximum // minimum)
        #Prepares the minimum and maximum for the next iteration
        maximum = minimum
        minimum = remainder
    gcd = maximum
    #Initialize lists to track the coefficients
    s_list = [1,0]
    t_list = [0,1]
    #Calculate the coefficients for each quotient
    for value in range(len(quotient_list) - 1):
        #Creates a temporary variable
        temporary1 = s1
        s1 = s0 - s1 * quotient_list[value]
        #Appends the s1 to the s_list
        s_list.append(s1)
        s0 = temporary1
        #Creates a temporary variable
        temporary2 = t1
        t1 = t0-t1 * quotient_list[value]
        #Appends the t1 to the t_list
        t_list.append(t1)
        t0 = temporary2
    #Print the quotients and intermediate coefficients.
    for value in range(1,len(quotient_list) + 1):
        print(f'q{value} = {quotient_list[value - 1]}, ', end = '')
    print("s0 = 1, s1 = 0 ")
    #Print intermediate coefficients for s
    for value in range(2,len(s_list)):
        print(f's{value} = s{value-2} - s{value-1} * q{value-1} = {s_list[value-2]} - {s_list[value-1]} * {quotient_list[value-2]} = {s_list[value]}')
    print("t0 = 0, t1 = 1, ", end="")
    #Print intermediate coefficients for t
    for value in range(2,len(t_list)):
        print(f't{value} = t{value-2} - t{value-1} * q{value-1} = {t_list[value-2]} - {t_list[value-1]} * {quotient_list[value-2]} = {t_list[value]}')
    #Check and print the equation for the greatest common divisor
    if s1*a + t1*b == maximum:
        print(f"gcd({a}, {b}) = {s1} * {a} + {t1} * {b}")
    else:
        print(f"gcd({a}, {b}) = {t1} * {a} + {s1} * {b}")

'''
This function will perform question 4
Author: Combination
'''
def question4():
    inputs = (414, 662), (6, 14),  (24, 36), (12, 42), (252, 198)
    questionPart = ["a", "b", "c", "d", "e"]
    #This will loop through the inputs and print their respective outputs
    for a, b in enumerate(inputs):
        print(f'4.{questionPart[a]}) ')
        #Runs the Euclidian Algorithm (Method 1) and also prints the steps backwards
        euclidianAlgorithmMethodTwo(b[0], b[1])
        #Prints a separation line
        print("_"*120)

#This will run every question
def main():
    #This function will perform question 1.a
    question1a()
    #This function will perform question 1.b
    question1b()
    #This function will perform question 1.c
    question1c()
    #This function will perform question 1.d
    question1d()
    #This function will perform question 1.e
    question1e()
    #This function will perform question 1.f
    question1f()
    #This function will perform question 1.g
    question1g()
    #This function will perform question 1.h
    question1h()
    #This function will perform question 1.i
    question1i()
    #This function will perform question 2.a
    question2a()
    #This function will perform question 2.b
    question2b()
    #This function will perform question 2.c
    question2c()
    #This function will perform question 2.d
    question2d()
    #This function will perform question 2.e
    question2e()
    #This function will perform question 3
    question3()
    #This function will perform question 4
    question4()
#Runs the main function
main()