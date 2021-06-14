class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # V: No. of Vertices(Node in this case)
    # E: No. of Edges(Edge is the line which connect two node)
    # A<-->B, <--> is an edge
    # T.C: O(V + E)
    # O(V) as we traserve every node once
    # O(E) as we also traverse each child,
    # and there are total of E children i.e number of Edges
    # S.C: O(V)
    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            current = queue.pop(0)
            array.append(current.name)
            queue += current.children
        return array
