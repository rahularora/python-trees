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
            
    def search(self, key):
        if self.data == key:
            print key, " found";
            return 
        elif self.data > key and self.left is not None:
            self.left.search(key);
        elif self.data < key and self.right is not None:
            self.right.search(key)

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
    root.search(11);
    
    
if __name__ == '__main__':
    build123();