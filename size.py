class Node(object):
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;
        
    def insert(self,data):
        newNode = Node(data);
        if data < self.data :
            if self.left is None:
                self.left = newNode;
            else:
                self.left.insert(data);
        else:
            if self.right is None:
                self.right = newNode;
            else:
                self.right.insert(data);
    
    def printTree(self):
        if self.left:
            print "Going left";
            self.left.printTree();
        print self.data;
        if self.right:
            print "Going right";
            self.right.printTree()
    
    def size(self, Node):
        if Node is None:
            return 0;
        else:
            return (self.size(Node.left) + 1 + self.size(Node.right));

def build123():
    root = Node(2);
    root.insert(1);
    root.insert(4);
    root.printTree()
    print root.size(root)
    
if __name__ == '__main__':
    build123();