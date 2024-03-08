'''
Name of program contained in the file: inputFile.py
Brief description of the program: This is a program that uses the algorithm from the lecture on Euler circuits and paths, 
                                  Dirac's theorem, and Ore's theorem to solve various problems.
Inputs: N/A
Output: Print the output of the assignment
All collaborators: Omar Mohammed, Arnav Jain
Other Sources for the Code: Stack Overflow, W3Schools, GeeksForGeeks
Author's full name: Nabeel Ahmad
Creation date: 12/07/2023
'''

#Imports the random library
import random

#Creates a class called Groups
class Groups:
    '''
    Utilizes the __init__ special method
    Author: Combination
    '''
    def __init__(self,group1,group2,group3):
        #Create 3 groups with the given values and store them in a tuple
        self.group1=group1
        self.group2=group2
        self.group3=group3
        self.groups=[self.group1,self.group2,self.group3]

    '''
    Utilizes the __str__ special method
    Author: Combination
    '''
    def __str__(self):
        #Return a string representation of the groups in the format:
        return f"{self.group1}, {self.group2}, {self.group3}"
    
    '''
    Adds a method that creates a new Groups object with different values
    Author: Combination
    '''
    def newGroups(self,index,value):
        #Create a copy of the current groups
        temp=list(self.groups)
        #Subtract the value from the group at the given index
        temp[index]-=value
        if sum(temp)>0:
            #If the sum of the new groups is 0, return None
            return Groups(temp[0],temp[1],temp[2])
        #Return the new groups object
        return None

#Creates a class called Games
class Games:
    '''
    Utilizes the __init__ special method
    Author: Combination
    '''
    def __init__(self,groups,maximumPlayer=True):
        #Create a new Games object with the given groups, max+player is True by default because the first player is always the max player
        self.groups=groups
        self.maximumPlayer=maximumPlayer
        #Create an empty list of children and set the leaf value to 0
        self.children=[]
        self.score=0

    '''
    Creates a method that adds a new child to the list of children with the same groups but with the max player switched
    Author: Combination
    '''
    def addChild(self,groups):
        self.children.append(Games(groups,not self.maximumPlayer))

    '''
    This method will return the value of the node
    Author: Combination
    '''
    def getValue(self):
        #Internal recursive function
        def calculateValue(node):
            #If the node is a leaf node, return the leaf value
            if node.score!=0:
                return node.score
            #If the node is not a leaf node, return the max or min value of the children
            if node.maximumPlayer:
                return max(calculateValue(child) for child in node.children)
            return min(calculateValue(child) for child in node.children)
        # Call the internal recursive function on self
        ans=calculateValue(self)
        return ans

    '''
    Utilizes the __str__ special method
    Author: Combination
    '''
    def __str__(self,level=0):
        #Groups: <groups>, Player: <min or max>, Value: <-1 or 0 or 1>
        #The indent is based on the level of the node
        indent="\t" * level
        nodeInfo=f"{indent}Groups: {self.groups}, "
        #If the node is a max player, set the player to Max, otherwise set it to Min
        player="Max" if self.maximumPlayer else "Min"
        nodeInfo+=f"Player: {player}, "
        nodeInfo+=f"Value: {self.getValue()}\n"
        #Recursively call the function on the children of the node adding the info to the string and level + 1
        for child in self.children:
            nodeInfo+=child.__str__(level+1)
        #Return the string
        return nodeInfo

#Creates a class called GameOfNim
class GameOfNim:
    '''
    Utilizes the __init__ special method
    Author: Combination
    '''
    def __init__(self,group1,group2,group3):
        #Create a new GameOfNim object with the given groups with the Root set to a Games with the given groups
        self.groups = Groups(group1, group2, group3)
        self.root = Games(self.groups)
        #Build the subtree
        self.buildSubtree(self.root)

    '''
    This will build the subtree of the given node
    Author: Combination
    '''
    def buildSubtree(self,node):
        #There are 3 possible moves for each group so loop through each group and each possible move
        for i in range(3):
            for j in range(1,node.groups.groups[i]+1):
                #Create a new group with the given move and add it as a child to the node (if it is a valid move)
                newGroup = node.groups.newGroups(i, j)
                if newGroup:
                    node.addChild(newGroup)
                    self.buildSubtree(node.children[-1])
        #If the node is a leaf node, set the leaf value to -1 if it is a max player, otherwise set it to 1
        if not node.children:
            node.score=-1 if node.maximumPlayer else 1

    '''
    This will print the tree starting from the root
    Author: Combination
    '''
    def printTree(self):
        print(self.root)

    '''
    This will play the game of Nim starting from the root
    Author: Combination
    '''
    def playGame(self):
        #Set the current move to the root and randomly choose who goes first
        move=self.root
        turn=bool(random.getrandbits(1))
        #While the current move has children, set the current move to the max or random child depending on who's turn it is
        print("Start:",move.groups)
        while move.children:
            if turn:
                move=max(move.children,key=lambda x:x.getValue())
            else:
                move=random.choice(move.children)
            #Print the next move and switch the turn receiver
            player="A" if turn else "B"
            print(f"Player {player}: ",move.groups)
            turn=not turn
        #If the current move is a max player, player A wins, otherwise player B wins
        winner="A" if turn else "B"
        #Print the winner and return the winner
        print("Player", winner, "won")
        print()
        return winner
    
    '''
    This will simulate the game of Nim 100 times and print the results of how many times each player won
    Author: Combination
    '''
    def simulateNim(self):
        aWinCount=0
        bWinCount=0
        for _ in range(100):
            #Play the game 100 times and keep track of the number of wins for each player
            if self.playGame()=="A":
                aWinCount+=1
            else:
                bWinCount+=1
        #Print the simulation results
        print(f"Player A won {aWinCount} times, Player B won {bWinCount} times.")
