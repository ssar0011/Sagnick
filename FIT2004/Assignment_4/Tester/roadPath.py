class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def buildMinHeap(self,array):
        for i in reversed(range(0, self.size // 2)):
            self.minHeapify(i)

    def minHeapify(self, idx):
        '''
        Start from the last parent node and compare the lest and right child nodes, and swap the parent node with the smallest child node
        provided that the value of the parent node is larger than that of the child nodes'.
        :param array: heap of size k
        :param i: parent node index
        :param heapsize: size of heap (size = k)
        :return: N/A

        pre-condition:
            heap must be present
        post-condition:
            smallest element sifts to the root node
        time-complexity:
            worst case: O(log(k))
            avg case: O(1)
        space complexty:
            O(logn)
        '''
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

            # The nodes to be swapped in min
        # heap if idx is not smallest
        if smallest != idx:
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            # Swap nodes
            temp = self.array[idx]
            self.array[idx] = self.array[smallest]
            self.array[smallest] = temp
            self.minHeapify(smallest)

            self.minHeapify(smallest)

    def extractMin(self):
        '''
        The following function extracts the node with minimum value by removing the root node and replacing it with the leaf node. Now
        minHeap sturcture is broken so in order to restore, minHeapify is called.

        Time Complexity:
            Best: O(1)
            Worst: O(log(v))
        Space Complexity:
            O(log(v))
        Error Handle:
            None
        Return:
            return the node with minimum value
        Parameter:
            None
        Precondition:
            self.array must not be empty (ie. heap must exist)
        '''

        # Return NULL if heap is empty
        if self.isEmpty() == True:
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def upHeap(self, v, dist):
        '''
        When you upheap a node, you compare its value to its parent node; if its value is less than its parent node, then you switch the
        two nodes and continue the process. Otherwise the condition is met that the parent node is less than the child node,
        and so you can stop the process.

        Time Complexity:
            Best: O(1)
            Worst: O(logv), v = number of vertices
        Space Complexity:
            O(logv)
        Error Handle:
            None
        Return:
            No return, heap structure in memory is changed
        Parameter:
            v: node that is added to heap
            dist: weight of vertex
        Precondition:
            self.array must not be empty
        '''

        # Get the index of v in  heap array

        i = self.pos[v]

        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is
        # not heapified. This is a O(Logn) loop
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:

            self.pos[self.array[i][0]] = (i - 1) // 2
            self.pos[self.array[(i - 1) // 2][0]] = i

            tmp = self.array[i]
            self.array[i] = self.array[(i-1)//2]
            self.array[(i-1)//2] = tmp

            i = (i - 1) // 2


    def isInMinHeap(self, v):

        if v > len(self.pos)-1:
            return False
        if self.pos[v] < self.size:
            return True
        return False

class Graph():
    
    def __init__(self):
        self.graph = []
        self.graphSaver = []
        self.length = 0
        self.detourGraph = []
        self.safeGraph = []
        self.parent = []

    def buildGraph(self,filename):
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
            for i in range(len(lines)):
                if lines[i][-1] == '\n':
                    lines[i] = lines[i][:-1]
                lines[i] = lines[i].split(' ')

            graph = [0] * (int(lines[-1][0]) + 1)
            count = 0
            while count < len(lines):
                if graph[int(lines[count][0])] != 0:
                    graph[int(lines[count][0])].append([int(lines[count][1]), float(lines[count][2])])
                    count+=1

                else:
                    graph[int(lines[count][0])] = [int(lines[count][0])]
                    graph[int(lines[count][0])].append([int(lines[count][1]), float(lines[count][2])])
                    count+=1

        self.graph = graph
        self.length = len(self.graph)


    def dijkstra(self, src, graph):
        '''
        The following function implements dijkstra's algorithm for finding the optimal path of traversal by traversing through a minHeap
        representation of the graph and calculates the distance of every node in the graph from the source node.

        Time Complexity:
            Best: O(Elog(V))
            Worst: O(Elog(V))
        Space Complexity:
            O(E+V)
        Error Handle:
            None
        Return:
            tuple with list containing the distances each node is from the source, and the parent nodes of each node
        Parameter:
            src: source node
            graph: binary graph obtained from text file
        Precondition:
            source and graph must be given
        '''

        dist = []
        parent = []

        minHeap = Heap()

        nodes = []
        for item in graph:
            if item != None and item != 0:
                nodes.append(item[0])


        cam = [0]*len(graph)
        for v in range(len(graph)):
            if graph[v] == None:
                cam[v] = 1
                dist.append(float("inf"))
                minHeap.pos.append(v)
                minHeap.array.append([v, dist[v]])
                parent.append(v)
            else:
                dist.append(float("inf"))
                minHeap.pos.append(v)
                minHeap.array.append([v, dist[v]])
                parent.append(v)


        minHeap.size = self.length
        minHeap.pos[src] = src
        dist[src] = 0
        minHeap.upHeap(src, dist[src])
        parent[src] = None

        while minHeap.isEmpty() == False:

            newHeapNode = minHeap.extractMin()

            u = newHeapNode[0]
            if graph[u] != None and graph[u] != 0:


                for cxn in range(1,len(graph[u])):

                    if graph[u][cxn] != None:

                        v = graph[u][cxn][0]
                        inHeap = minHeap.isInMinHeap(v)

                        if minHeap.isInMinHeap(v) and dist[u] != float('inf') and graph[u][cxn][1] + dist[u] < dist[v] and cam[v] != 1:
                            dist[v] = graph[u][cxn][1] + dist[u]
                            parent[v] = u

                            minHeap.upHeap(v, dist[v])

        return dist,parent

    def quickestPath(self,source,target):
        '''
        quickestPath function finds the quickest path by first finding the distances of every node from the source node thorugh the dijkstra
        function. THe dijkstra function returns a list of distances (how far each node is with respect to the source node) and a list
        of parents (parent nodes of each node in the graph). Using these two lists, the quickest path is assimilated.

        Time Complexity:
            Best: O(Elog(V))
            Worst: O(Elog(V))
        Space Complexity:
            O(E+V)
        Error Handle:
            None
        Return:
            tuple where tuple[0] is a list of nodes giving the optimal path and tuple[1] is the distance of this optimal path
        Parameter:
            source: source node, starting point
            target: target node, destination
        Precondition:
            function which implements dijkstra's algorithm
            source and target must be specified otherwise the program cannot assimilate an optimal path
        '''

        source  = int(source)
        target = int(target)
        result = self.dijkstra(source,self.graph)
        dist = result[0]
        parents = result[1]
        self.parent = parents


        if target > len(dist):
            return [[],-1]

        distance = dist[target]

        if distance == float("inf"):
            return [[],-1]

        p = target
        path = [p]
        while parents[p] != None:
            path.append(parents[p])
            p = parents[p]

        path = path[::-1]
        return (path,distance)

    def augmentGraph(self,filename_camera,filename_toll):
        '''
        augmentGraph takes the graph saved in the memory and modifies it so that the program can avoid certain nodes. For the nodes and
        edges specified where there is either a camera of a toll, at that spot in self.graph, the value is replaced with a None.

        Time Complexity:
            Best: O(V + E)
            Worst: O(V + E)
        Space Complexity:
            O(V)
        Error Handle:
            None
        Return:
            No return, graph is saved in memory as well as the size of the graph
        Parameter:
            filename_camera: name of the file that consists of the nodes at which there is a camera
            filename_toll: name of the file that consists of the edges at which there is a toll
        Precondition:
            file must exist and be properly formatted
        '''

        with open(filename_camera) as f:
            camera = f.readlines()

            if len(camera) > 1:
                for i in range(len(camera)):
                    if camera[i][-1] == '\n':
                        camera[i] = camera[i][:-1]
                    camera[i] = int(camera[i])
            else:
                camera[0] = int(camera[0])

        with open(filename_toll) as g:
            toll = g.readlines()

            if len(toll) > 1:
                for i in range(len(toll)):
                    if toll[i][-1] == '\n':
                        toll[i] = toll[i][:-1]
                    toll[i] = toll[i].split(' ')
                    toll[i][0] = int(toll[i][0])
                    toll[i][1] = int(toll[i][1])


        for item in camera:
            self.graphSaver.append(self.graph[item])
            self.graph[item] = None

        for itm in toll:

            if self.graph[itm[0]] == None or self.graph[itm[1]] == None:
                continue

            for edge1 in range(1, len(self.graph[itm[0]])):

                if self.graph[itm[0]][edge1][0] == itm[1]:
                    self.graphSaver.append([itm[0],edge1,self.graph[itm[0]][edge1]])
                    self.graph[itm[0]][edge1] = None



    def quickestSafePath(self, source, target):
        '''
        quickestSafePath function finds the quickest path by first finding the distances of every node from the source node thorugh the
        dijkstra function. The dijkstra function returns a list of distances (how far each node is with respect to the source node) and a
        list of parents (parent nodes of each node in the graph). Using these two lists, the quickest path is assimilated.

        Time Complexity:
            Best: O(Elog(V))
            Worst: O(Elog(V))
        Space Complexity:
            O(E+V)
        Error Handle:
            None
        Return:
            tuple where tuple[0] is a list of nodes giving the optimal path and tuple[1] is the distance of this optimal path
        Parameter:
            source: source node, starting point
            target: target node, destination
        Precondition:
            function which implements dijkstra's algorithm
            source and target must be specified otherwise the program cannot assimilate an optimal path
        '''

        source = int(source)
        target = int(target)

        for saved in self.graphSaver:
            if type(saved[1]) == list:
                if saved[0] == source:
                    self.graph[saved[0]] = saved
                    break

        result = self.dijkstra(source,self.graph)
        dist = result[0]
        parents = result[1]


        if target > len(dist):
            return ([],-1)

        distance = dist[target]

        if distance == float("inf"):
            return [[],-1]

        p = target
        path = [p]
        while parents[p] != None:
            path.append(parents[p])
            p = parents[p]

        path = path[::-1]
        return (path,distance)

    def addService(self,filename_service):
        '''
        addService traverses through filename_service and saves the nodes to a list in memory called self.detour

        Time Complexity:
            Best: O(1)
            Worst: O(V)
        Space Complexity:
            O(V)
        Error Handle:
            None
        Return:
            No return, detour list is saved in memory as well as the size of the graph
        Parameter:
            filename_service: name of the file that lists the nodes at which there is a service station
        Precondition:
            file must exist and be properly formatted
        '''

        with open(filename_service) as f:

            detour = f.readlines()
            if len(detour) > 1:
                for i in range(len(detour)):
                    if detour[i][-1] == '\n':
                        detour[i] = detour[i][:-1]
                    detour[i] = int(detour[i])
            else:
                detour[0] = int(detour[0])

        self.detour = detour

    def quickestDetourPath(self,source,target):
        '''
        The following function finds the optimal path for which at least one of the nodes in self.detour must be included in the path.
        This is done by first finding the distances of every node with repect to the source node, and saving the distances of the detour
        nodes into a list, detourDist. Next form a smaller version of the graph that includes the source node, target node and all the
        service point nodes. Apply dijkstra to this simplified graph, find the optimal path including the service point node and then
        expand the path to include all the nodes.

        Time Complexity:
            Best: O(Elog(V))
            Worst: O(Elog(V))
        Space Complexity:
            O(E+V)
        Error Handle:
            None
        Return:
            tuple where tuple[0] is a list of nodes giving the optimal path and tuple[1] is the distance of this optimal path
        Parameter:
            source: source node, starting point
            target: target node, destination
        Precondition:
            function which implements dijkstra's algorithm
            source and target must be specified otherwise the program cannot assimilate an optimal path
        '''

        source = int(source)
        target = int(target)

        for saved in self.graphSaver:
            if type(saved[1]) != list:
                self.graph[saved[0]][saved[1]] = saved[2]
            else:
                self.graph[saved[0]] = saved


        result = self.dijkstra(source,self.graph)
        dist = result[0]
        parents = result[1]
        self.parent = parents


        if target > len(dist):
            return ([], -1)

        detourDist = []
        for item in self.detour:
            detourDist.append([item,dist[item]])

        targetDist = []
        allParents = [None] * len(self.graph)
        for node in detourDist:
            optPath = self.dijkstra(node[0],self.graph)
            allParents[node[0]] = optPath[1] # path from detour to target
            targetDist.append([node[0],optPath[0][target]])


        detourGraph = [None]*len(self.graph)
        detourGraph[source] = [source]

        for detourNode in detourDist:
            detourGraph[source].append(detourNode)

        detourGraph[target] = [target]
        for destNode in targetDist:
            detourGraph[destNode[0]] = [destNode[0]]
            detourGraph[destNode[0]].append([target,destNode[1]])
            detourGraph[target].append([destNode[0],destNode[1]])

        self.detourGraph = detourGraph

        result = self.dijkstra(source,self.detourGraph)
        dist = result[0]
        parents = result[1]

        if target > len(dist):
            return ([],-1)

        distance = dist[target]

        if distance == float("inf"):
            return [[],-1]


        p = target
        simpPath = [p]
        while parents[p] != None:
            simpPath.append(parents[p])
            p = parents[p]

        simpPath = simpPath[::-1]

        #simpPath has max length of 3 therefore this loop is O(3^3) = O(9) which is constant
        for nd in simpPath:
            if nd in self.detour:
                idx = simpPath.index(nd)

        if len(simpPath) == 1:
            idx = 0

        q = simpPath[idx]
        Path = [q]

        while self.parent[q] != None:
            Path.append(self.parent[q])
            q = self.parent[q]

        Path = Path[::-1]


        detourParents = allParents[Path[-1]]
        r = simpPath[-1]
        path_b = [r]
        if detourParents != None:
            while detourParents[r] != None:
                path_b.append(detourParents[r])
                r = detourParents[r]

        path_b = path_b[::-1]


        Path.extend(path_b[1:])
        return (Path,distance)

if __name__ == "__main__":
    graph = Graph()

    filename_roads = input("Enter the file name for the graph: ")
    filename_camera = input("Enter the file name for camera nodes: ")
    filename_toll = input("Enter the file name for the toll roads: ")
    filename_service = input("Enter the file name for the service nodes: ")


    print('-'*80)

    src_node = input("Source node: ")
    sink_node = input("Sink node: ")

    print('-' * 80)

    graph.buildGraph(filename_roads)
    print("Quickest Path:")
    QuickPath = graph.quickestPath(src_node,sink_node)
    if QuickPath != [[],-1]:
        output = ''
        count = 0
        while count < len(QuickPath[0])-1:
            output += str(QuickPath[0][count]) + ' --> '
            count += 1
        output += str(QuickPath[0][-1])
        print(output)

        time = str(QuickPath[1]) + " minute(s)"
        print("Time: {}".format(time))
    else:
        print("Path does not exist")

    print('-' * 80)


    graph.augmentGraph(filename_camera,filename_toll)
    print("Safest Path:")
    SafePath = graph.quickestSafePath(src_node, sink_node)
    if SafePath != [[],-1]:
        output = ''
        count = 0
        while count < len(SafePath[0]) - 1:
            output += str(SafePath[0][count]) + ' --> '
            count += 1
        output += str(SafePath[0][-1])
        print(output)

        time = str(SafePath[1]) + " minute(s)"
        print("Time: {}".format(time))

    else:
        print("Path does not exist")


    print('-' * 80)


    graph.addService(filename_service)
    print("Quickest Detour Path:")
    Detour = graph.quickestDetourPath(src_node, sink_node)
    if Detour != [[],-1]:
        output = ''
        count = 0
        while count < len(Detour[0]) - 1:
            output += str(Detour[0][count]) + ' --> '
            count += 1
        output += str(Detour[0][-1])
        print(output)

        time = str(Detour[1]) + " minute(s)"
        print("Time: {}".format(time))
    else:
        print("Path does not exist")

    print('-' * 80)
