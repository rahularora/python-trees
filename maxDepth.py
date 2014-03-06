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
                
    def maxDepth(self, Node):
        if Node is None:
            return 0;
        else:
            leftDepth = self.maxDepth(Node.left);
            rightDepth = self.maxDepth(Node.right);
            if leftDepth > rightDepth:
                return leftDepth + 1;
            else:
                return rightDepth + 1;
    
def build123():
    root = Node(6);
    root.insert(2);
    root.insert(7);
    root.insert(8);
    root.insert(9);
    root.insert(10);
    root.insert(1);
    root.insert(4);
    root.insert(3);
    print root.maxDepth(root);
    
if __name__ == '__main__':
    build123();
            