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
    
    def isBSTHelper(self,treeList):
        if self.left:
            self.left.isBSTHelper(treeList);
        treeList.append(self.data);
        if self.right:
            self.right.isBSTHelper(treeList);
            
        return treeList
            
    def isBST(self):
        treeList = self.isBSTHelper([]);
        isBST = True;
        for i in range(len(treeList) - 1):
            if treeList[i] > treeList[i+1] :
                isBST = False;
                break;
        
        return isBST;

def build123():
    root = Node(2);
    root.insert(1);
    root.insert(3);
    print root.isBST();
    
    
if __name__ == '__main__':
    build123();