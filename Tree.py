
from graphviz import Digraph

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        if children:
            self.children = children
        else:
            self.children = []
        self.dot = None

    def generateDot(self, filename=None, view=True):
        self.dot = Digraph()
        self.generateDotRecursive(self, None)
        self.dot.format = 'png'
        if not filename:
            filename = "images/temp"
        self.dot.render(filename=f"images/{filename}", view=view)
        
    def generateDotRecursive(self, treeNode, parentNode):
        self.dot.node(str(id(treeNode)), str(treeNode.val) )
        if (parentNode):
            self.dot.edge( str(id(parentNode)) , str(id(treeNode)))

        for c in treeNode.children:
            self.generateDotRecursive(c, treeNode)
