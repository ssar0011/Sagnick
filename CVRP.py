'''
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
'''

class Graph():

    def __init__(self):
        self.graph = []
        self.length = 0
        self.depot = 0
        self.demand = 0
        self.capacity = 0

    def buildGraph(self, filename):
        '''
        The following function forms the graph by reading through the text file provided. The length of the graph is the same as the number
        of nodes. Each node is in its repective index. At each node, is a list of lists which has [connecting node, distance], thus
        showing which nodes are connected to which and the weight of their edges.
        Time Complexity:
            Best: O(V)
            Worst: O(V)
        Space Complexity:
            O(V)
        Error Handle:
            None
        Return:
            No return, graph is saved in memory as well as the size of the graph
        Parameter:
            filename: name of the file that consists of the nodes
        Precondition:
            file must exist and be properly formatted
        '''

        with open(filename) as f:
            lines = f.readlines()
            #print(lines)

            for l in range(len(lines)):
                if lines[l] == "NODE_COORD_SECTION\n":
                    l1 = l
                elif lines[l] == "DEMAND_SECTION\n":
                    l2 = l
                elif lines[l] == "DEPOT_SECTION\n":
                    l3 = l

            DEPOT = lines[l3+1]
            self.depot = int(DEPOT[:-1])

            NODE_COORD = lines[l1+1:l2]
            DEMAND_SECTION = lines[l2+1:l3]

            CAPACITY = int(lines[5][11:])

            self.capacity = CAPACITY

            for i in range(len(NODE_COORD)):
                if NODE_COORD[i][-1] == '\n':
                    NODE_COORD[i] = NODE_COORD[i][:-1]
                NODE_COORD[i] = NODE_COORD[i].split(' ')

            for i in range(len(DEMAND_SECTION)):
                if DEMAND_SECTION[i][-1] == '\n':
                    DEMAND_SECTION[i] = DEMAND_SECTION[i][:-1]
                DEMAND_SECTION[i] = DEMAND_SECTION[i].split(' ')

            #print(NODE_COORD)
            #print(DEMAND_SECTION)
            #print(self.depot)

            graph = [0] * (int(NODE_COORD[-1][0]) + 1)
            count = 0
            while count < len(NODE_COORD):
                graph[int(NODE_COORD[count][0])] = [int(NODE_COORD[count][1]), int(NODE_COORD[count][2])]
                count += 1

            demand = [0]
            count = 0
            while count < len(DEMAND_SECTION):
                demand.append(int(DEMAND_SECTION[count][1]))
                count += 1

        self.demand = demand
        self.graph = graph
        self.length = len(self.graph)

        distMatrix = [[0 for k in range(len(self.graph))]for l in range(len(self.graph))]

        for i in range(1,len(self.graph)):
            for j in range(1,len(self.graph)):
                dist = abs(self.graph[i][0]-self.graph[j][0]) + abs(self.graph[i][1]-self.graph[j][1])
                #print(distMatrix[1][32])
                distMatrix[i][j] = dist
                distMatrix[j][i] = dist

        print(self.findMinNode(self.depot,distMatrix))

    def findMinNode(self,start,matrix):
        #print(matrix[start])
        array = matrix[start]
        CAPACITY = self.capacity
        routes = []

        visited = self.length - 1
        index = start
        count = 1
        while visited >= 0:
            while count <= self.length:
                temp = sorted(array)
                #print(temp)
                minDist = min([n for n in array if n>0])
                node = array.index(minDist)
                DEMAND = self.demand[node]
                if DEMAND <= CAPACITY:
                    print(node)
                    CAPACITY -= DEMAND
                    print(CAPACITY)
                    print('\n')
                    routes.append(node)
                    array = matrix[node]
                    index = node

                    matrix[index] = [float("inf")] * self.length
                    for i in range(self.length):
                        matrix[i][index] = float("inf")

                    visited -= 1
                    break
                else:
                    if CAPACITY < min([n for n in self.demand if n>0]):
                        index = self.depot
                        CAPACITY = self.capacity
                        break
                    else:
                        array = array[count:]
                        count += 1
        return routes





if __name__ == "__main__":
    graph = Graph()

    graph.buildGraph("A-n32-k5.txt")
