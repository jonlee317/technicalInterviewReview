# Question 3
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
# Your function should take in and return an adjacency list structured like this:
#
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)

def question3(G):
    nodeList = []
    # naively iterating through all items
    for item in G:
        for val in G[item]:
            print val[1]

# test cases
myGraph1 = {'A': [('B',4), ('C',2)],
            'B': [('A',4), ('D',3)],
            'C': [('A',2), ('D',5)],
            'D': [('B',3),('C',5)]
}

myGraph2 = {'A': [('B',4), ('C',2)],
            'B': [('A',4), ('C',1), ('D',3)],
            'C': [('A',2), ('B',1), ('D',5)],
            'D': [('B',3),('C',5)]
}

question3(myGraph1)
#question3(myGraph2)
