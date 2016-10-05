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
    nodeList = [[0,'A']]

    print G
    # naively iterating through all items
    traveled = {item: 0 for item in G}
    minTree = {item: [] for item in G}
    while len(nodeList) > 0:
        val = nodeList.pop(0)
        traveled[val[1]] = 1
        for item in G[val[1]]:
            if traveled[item[0]] == 0 or traveled[val[1]]==0:
                nodeList.append([item[1],item[0],val[1]])
                #traveled[item[0]] = 1
        nodeList = sorted(nodeList)
        print "hi"
        print nodeList
        if len(nodeList) >0 and (traveled[nodeList[0][2]] == 0 or traveled[nodeList[0][1]]==0):
            #minTree[val[1]].append(nodeList[0])
            minTree[nodeList[0][2]].append([nodeList[0][1],nodeList[0][0]])
            minTree[nodeList[0][1]].append([nodeList[0][2],nodeList[0][0]])

    # TODO: able to go through each node but unable to tell which value belongs
    # to which node.  So need ability to save from where to where.  It already has
    # strategy of choosing the min.
    print traveled
    print minTree

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

#question3(myGraph1)
question3(myGraph2)
