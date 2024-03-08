'''
Name of program contained in the file: EECS210_Assignment8.py
Brief description of the program: This is a program that uses the algorithm from the lecture on Euler circuits and paths, 
                                  Dirac's theorem, and Ore's theorem to solve various problems.
Inputs: inputFile.py
Output: Print the output of the assignment
All collaborators: Omar Mohammed, Arnav Jain
Other Sources for the Code: Stack Overflow, W3Schools, GeeksForGeeks
Author's full name: Nabeel Ahmad
Creation date: 12/07/2023
'''

#Imports the inputFile in the directory 
from inputFile import *

#Creates a class named edge
class Edge:
    '''
    Utilizes the __init__ special method
    Author: Combination
    '''
    def __init__(self,x,y):
        #Creates x and y, where x and y are vertices
        self.x = x
        self.y = y

    '''
    Utilizes the __eq__ special method
    Author: Combination
    '''
    def __eq__(self,value):
        #If value is an edge, check if the vertices are the same
        if isinstance(value,Edge):
            return {self.x,self.y}=={value.x,value.y}
        #If value is not an edge, compare the vertices to the value
        return {self.x,self.y}==value
    
    '''
    Creates a method to determine if the edge contains the input value
    Author: Combination
    '''
    def contain(self,value):
        #Check if the edge contains the input value
        return value==self.x or value==self.y
    
    '''
    Utilizes the __hash__ special method
    Author: Combination
    '''
    def __hash__(self):
        #Return a hashed value of x and y
        return hash(self.x)+hash(self.y)
    
    '''
    Utilizes the __str__ special method
    Author: Combination
    '''
    def __str__(self):
        #Return x and y as a string
        return f"({self.x}, {self.y})"
    
    '''
    Utilizes the __repr__ special method
    Author: Combination
    '''
    def __repr__(self):
        #Return the vertices as a string 
        return self.__str__()
    
    '''
    This method returns the opposite vertex
    Author: Combination
    '''
    def oppositeVertex(self,vertex):
        #If x is equal to the vertex, return the opposite vertex
        if self.x==vertex:
            return self.y
        return self.x

#Creates a class named Graph
class Graph:
    '''
    Utilizes the __init__ special method
    Author: Combination
    '''
    def __init__(self,vertices,edges):
        #This is a set of vertices
        self.vertices=vertices
        #Edges is a set of edge classes
        self.edges=set()
        for edge in edges:
            self.edges.add(Edge(edge[0],edge[1]))
        #The verticesCount is the number of vertices in the graph
        self.verticesCount=len(self.vertices)

    '''
    Adds a way to count the edges with the vertex
    Author: Combination
    '''
    def countEdges(self,vertex):
        #Create a method to count the number of edges that contain the vertex
        count=0
        for edge in self.edges:
            #If the edge contains the vertex, increase the count
            if edge.contain(vertex):
                count+=1
        return count
    
    '''
    Adds a way to return a set of vertices with odd countEdges
    Author: Combination
    '''
    def oddVertices(self):
        #Initialize a set to store the odd vertices
        odd=set()
        for vertices in self.vertices:
            #If the countEdges of the vertex is odd, add that value to the set
            if self.countEdges(vertices) % 2 == 1:
                odd.add(vertices)
        return odd
    
    '''
    Adds a way to check if the graph satisfies Dirac's condition
    Author: Combination
    '''
    def hamiltonDirac(self):
        for vertices in self.vertices:
            #If the countEdges of the vertex is less than half the number of vertices, it is not a Hamilton circuit
            if self.countEdges(vertices)<self.verticesCount/2:
                #If the loop does not complete, the graph does not satisfy Dirac's condition
                return False
        #If the loop completes, the graph satisfies Dirac's condition
        return True
    
    '''
    Adds a way to check if the graph satisfies Ore's condition
    Author: Combination
    '''
    def hamiltonOre(self):
        verts_list=list(self.vertices)
        for i in range(self.verticesCount):
            for j in range(i+1,self.verticesCount):
                #Go through every pair of vertices and get the vertices
                vertex1=verts_list[i]
                vertex2=verts_list[j]
                #If the vertices are the same edge, skip
                if Edge(vertex1,vertex2) in self.edges:
                    continue
                #Find the sum of the degrees of the vertices
                check = self.countEdges(vertex1) + self.countEdges(vertex2)
                #If the sum is less than the number of vertices, it is not a Hamilton circuit
                if check<self.verticesCount:
                    return False
        #If the loop completes, the graph satisfies Ore's condition
        return True
    
    '''
    Adds a way to return a set of edges adjacent to the vertex
    Author: Combination
    '''
    def adjacentEdges(self,vertex):
        #Initialize a set to store the edges
        edges=set()
        for edge in self.edges:
            #If the edge contains the vertex, add it to the set
            if edge.contain(vertex):
                edges.add(edge)
        #Return the set of edges
        return edges
    
    '''
    Adds a way to return a list of vertices that form a Euler circuit
    Author: Combination
    '''
    def eulerCircuit(self):
        #If there are any odd vertices, the graph does not have a Euler circuit and raises an error
        if len(self.oddVertices())>0:
            raise RuntimeError("Graph does not have an Euler circuit")
        #Save the current state of the graph's edges
        temp_edges = self.edges.copy()
        #Initialize a list to track vertices; start with an arbitrary vertex
        curr_vert=list(self.vertices)[0]
        vertex_tracker=[curr_vert]
        #Initialize the circuit list
        eulerCircuit=[]
        #While there are still vertices to visit
        while vertex_tracker!=[]:
            #Select the current vertex
            curr_vert = vertex_tracker[-1]
            #Get the adjacent edges
            available_edges=self.adjacentEdges(curr_vert)
            if not available_edges:
                #If no edges are left, add the vertex to the circuit and remove it from the tracker
                eulerCircuit.append(curr_vert)
                vertex_tracker.pop()
            else:
                #Remove an edge and add the opposite vertex to the tracker
                edge = available_edges.pop()
                self.edges.remove(edge)
                next_vertex = edge.oppositeVertex(curr_vert)
                vertex_tracker.append(next_vertex)
        #Restore the original state of edges and return the circuit
        self.edges=temp_edges
        return eulerCircuit
    
'''
The main function to run all the methods
Author: Combination
'''
def main():
    #Create the graphs and test if they are Euler circuits, if there is an error, print the odd vertices
    print("Problem 1)")
    vertices={'a','b','c','d','e'}
    edges=[('a','e'),('a','b'),('b','e'),('e','d'),('e','c'),('c','d'),('d','e')]
    p1g1=Graph(vertices,edges)
    try:
        print(f"Example 1 graph G1 is a Euler circuit: {p1g1.eulerCircuit()}")
    except RuntimeError:
        print(f"Example 1 graph G1 is not a Euler circuit. The odd vertices are: {p1g1.oddVertices()}")
    #Problem 1 G2
    vertices={'a','b','c','d','e'}
    edges=[('a','e'),('a','b'),('b','e'),('e','d'),('e','c'),('c','d'),('d','e'),('a','d'),('c','b')]
    p1g2=Graph(vertices,edges)
    try:
        print(f"Example 1 graph G2 is a Euler circuit: {p1g2.eulerCircuit()}")
    except RuntimeError:
        print(f"Example 1 graph G2 is not a Euler circuit. The odd vertices are: {p1g2.oddVertices()}")
    #Problem 1 G3
    vertices={'a','b','c','d','e'}
    edges=[('a','b'),('a','d'),('a','c'),('b','d'),('c','d'),('d','e'),('b','e')]
    p1g3=Graph(vertices,edges)
    try: 
        print(f"Example 1 graph G3 is a Euler circuit: {p1g3.eulerCircuit()}")
    except RuntimeError:
        print(f"Example 1 graph G3 is not a Euler circuit. The odd vertices are: {p1g3.oddVertices()}")
    #Bridge Exercise
    vertices={'a','b','c','d'}
    edges=[('a','b'),('b','a'),('a','c'),('c','a'),('c','d'),('d','a'),('d','b')]
    bridge=Graph(vertices,edges)
    try:
        print(f"Bridge graph is a Euler circuit: {bridge.eulerCircuit()}")
    except RuntimeError:
        print(f"Bridge graph is not a Euler circuit. The odd vertices are: {bridge.oddVertices()}")
    #1b
    vertices={'a','b','c','d','e','f','g','h','i'}
    edges=[('a','d'),('a','b'),('b','e'),('b','c'),('b','d'),('c','f'),('d','g'),('d','e'),('e','h'),('e','f'),('f','i'),('g','h'),('h','i'),('h','f')]
    p1b=Graph(vertices, edges)
    try:
        print(f"Problem 1b graph is a Euler circuit: {p1b.eulerCircuit()}")
    except RuntimeError:
        print(f"Problem 1b graph is not a Euler circuit. The odd vertices are: {p1b.oddVertices()}")
    #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*150)
    print("Problem 2)")
    #Graphs for problem 2 and 3
    #Example 5 G1
    vertices={'a','b','c','d','e'}
    edges=[('a','e'),('a','b'),('a','c'),('b','e'),('b','c'),('c','e'),('c','d'),('e','d')]
    p2g1=Graph(vertices,edges)
    #Example 5 G2
    vertices={'a','b','c','d'}
    edges=[('a','b'),('b','d'),('b','c'),('c','d')]
    p2g2=Graph(vertices,edges)
    #Example 5 G3
    vertices={'a','b','c','d','e','f','g'}
    edges=[('a','b'),('b','c'),('b','g'),('e','g'),('d','c'),('c','e'),('e','f')]
    p2g3=Graph(vertices, edges)
    #Test case 2 (used for 3b also)
    vertices={'a','b','c','d','e','f'}
    edges=[('a','b'),('a','c'),('b','c'),('c','f'),('d','e'),('d','f'),('e','f')]
    p2b=Graph(vertices, edges)
    #Problem 2: Calls the hamilton dirac function for each graph. If it returns true, it satisfies Dirac's condition and is a Hamilton circuit, otherwise it may be a Hamilton circuit
    if p2g1.hamiltonDirac():
        print("Example 5 graph G1 satisfies Dirac's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G1 does not satisfy Dirac's condition and may be a Hamilton circuit")
    if p2g2.hamiltonDirac():
        print("Example 5 graph G2 satisfies Dirac's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G2 does not satisfy Dirac's condition and may be a Hamilton circuit")
    if p2g3.hamiltonDirac():
        print("Example 5 graph G3 satisfies Dirac's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G3 does not satisfy Dirac's condition and may be a Hamilton circuit")
    if p2b.hamiltonDirac():
        print("Test case 2 graph satisfies Dirac's condition and is a Hamilton circuit")
    else:
        print("Test case 2 graph does not satisfy Dirac's condition and may be a Hamilton circuit")    
    #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*150)
    print("Problem 3)")
    #Problem 3: Calls the hamilton ore function for each graph. If it returns true, it satisfies Dirac's condition and is a Hamilton circuit, otherwise it may be a Hamilton circuit
    if p2g1.hamiltonOre():
        print("Example 5 graph G1 satisfies Ore's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G1 does not satisfy Ore's condition and may be a Hamilton circuit")
    if p2g2.hamiltonOre():
        print("Example 5 graph G2 satisfies Ore's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G2 does not satisfy Ore's condition and may be a Hamilton circuit")
    if p2g3.hamiltonOre():
        print("Example 5 graph G3 satisfies Ore's condition and is a Hamilton circuit")
    else:
        print("Example 5 graph G3 does not satisfy Ore's condition and may be a Hamilton circuit")
    if p2b.hamiltonOre():
        print("Test case 2 graph satisfies Ore's condition and is a Hamilton circuit")
    else:
        print("Test case 2 graph does not satisfy Ore's condition and may be a Hamilton circuit")
    #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*150)
    print("Problem 4)") 
    #Problem 4: Calls the play_game function for each game and prints the winner
    #Question 4a, print the game tree for values 2,2,1
    print("Question 4a)")
    nimSolver=GameOfNim(2,2,1)
    nimSolver.printTree()
    #Question 4b, print the game tree for values 1,2,3
    print("Question 4b)")
    nimSolver=GameOfNim(1,2,3)
    nimSolver.printTree()
    #Question 4c, Simulate the game 100 times and print the results
    print("Question 4c)")
    nimSolver=GameOfNim(2,2,1)
    nimSolver.simulateNim()
    #Prints a separation line to allow for better distinguishing of questions. One underscore multiplied by 100 repeats the underscore 100 times in the print line
    print("_"*150)

main()
