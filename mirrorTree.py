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
            
    def mirror(self):
        temp = self.left
        self.left = self.right
        self.right = temp
        
        if self.left:
            self.left.mirror()
        
        if self.right:
            self.right.mirror()
        
        
def build123():
    root = Node(8);
    root.insert(3);
    root.insert(12);
    root.insert(9);
    root.mirror();
    print "mirror"
    root.printTree();
    
if __name__ == '__main__':
    build123();
            