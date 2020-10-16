from lecture_3 import Node, Edge, Graph


nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)


def permut(str):
    return str[1] + str[0] + str[2], str[0] + str[2] + str[1]


nodesList = [x.getName() for x in nodes]

for node in nodes:
    for name in nodesList:
        n1, n2 = permut(node.getName())
        if n1 in nodesList:
            g.addEdge(Edge(g.getNode(node.getName()), g.getNode(n1)))
        if n2 in nodesList:
            g.addEdge(Edge(g.getNode(node.getName()), g.getNode(n2)))

print(g)
