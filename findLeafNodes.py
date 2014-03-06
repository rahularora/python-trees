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
                
    def findLeafNodes(self): 
        if self.left:
            self.left.findLeafNodes();
        
        if self.right:
            self.right.findLeafNodes();
        
        if self.left is None and self.right is None:
            print self.data
    
def build123():
    root = Node(8);
    root.insert(3);
    root.insert(1);
    root.insert(5);
    root.insert(4);
    root.insert(6);
    root.insert(12);
    root.insert(10);
    root.insert(11);
    root.findLeafNodes();
    
if __name__ == '__main__':
    build123();
            