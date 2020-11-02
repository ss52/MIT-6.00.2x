class Node(object):
    def __init__(self, name) -> None:
        self.name = name

    def getName(self):
        return self.name

    def __str__(self) -> str:
        return self.name


class Edge(object):
    def __init__(self, src, dest) -> None:
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self) -> str:
        return self.src.getName() + "->" + self.dest.getName()


class Digraph(object):
    """ Ребра представляют словарь соответсвий вершины и ее потомков """
    def __init__(self) -> None:
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()

        if not (src in self.edges and dest in self.edges):
            raise ValueError("Node not in graph")

        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self) -> str:
        result = ""
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + " -> " + dest.getName() + "\n"
        return result[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'LA'):
        g.addNode(Node(name))

    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('LA'), g.getNode('Boston')))

    return g


def printPath(path):
    """ Принимает путь, как список. Вывод на печать """
    result = ""
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += "->"
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """ Принимает: объект граф, старт и финиш как node.
        Возвращает кратчайший путь по графу
        Алгоритм поиска в глубину"""
    path = path + [start]
    if toPrint:
        print("Current DFS path:", printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath is not None:
                    shortest = newPath
        elif toPrint:
            print("Already visited", node)
    return shortest


def shortestPath(graph, start, end, toPrint=False):
    return DFS(graph, start, end, [], None, toPrint)


def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)

    print(f"Shortest path: {printPath(sp)}")


# testSP("Boston", "Phoenix")


def BFS(graph, start, end, toPrint=False):
    """ Поиск в ширину """
    initPath = [start]
    pathQuery = [initPath]

    if toPrint:
        print("Current BFS path:", printPath(pathQuery))

    while len(pathQuery) != 0:
        tmpPath = pathQuery.pop(0)
        print("Current BFS path:", printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQuery.append(newPath)

    return None


g = buildCityGraph(Digraph)
sp = BFS(g, g.getNode("Boston"), g.getNode("Phoenix"), toPrint=True)
print(f"Shortest path: {printPath(sp)}")
