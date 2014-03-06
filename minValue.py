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
                
    def minValue(self):
        while self.left is not None:
            self = self.left
        
        return self.data
    
    def printTree(self):
        if self.left:
            print "Going left";
            self.left.printTree();
        print self.data;
        if self.right:
            print "Going right";
            self.right.printTree()

def build123():
    root = Node(12);
    root.insert(10);
    root.insert(31);
    root.insert(4);
    root.insert(6);
    root.insert(14);
    root.insert(2);
    print root.minValue();
    root.printTree()
    
if __name__ == '__main__':
    build123();