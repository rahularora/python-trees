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
                
    def delete(self, key, ancestor):
        if self.data == key:
            #No child. Simply remove it from list
            
            if self.left is None and self.right is None:
                if ancestor.data > self.data:
                    ancestor.left = None
                else:
                    ancestor.right = None
            
            elif self.left is None:
                if ancestor.data > self.data:
                    ancestor.left = self.right;
                else:
                    ancestor.right = self.right;
                    
            elif self.right is None:
                if ancestor.data > self.data:
                    ancestor.left = self.left;
                else:
                    ancestor.right = self.left;
            
            #2child
            else:
                # Find largest value in left subtree
                rightMostNodeAncestor = self.left;
                rightMostNode = rightMostNodeAncestor.right;
                
                print "Work in progress if there are 2 childs"
            
        elif self.data > key and self.left is not None:
            self.left.delete(key, self);
        elif self.data < key and self.right is not None:
            self.right.delete(key, self)

    def printTree(self):
        if self.left:
            print "Going left";
            self.left.printTree();
        print self.data;
        if self.right:
            print "Going right";
            self.right.printTree()
    
    def search(self, key):
        if self.data == key:
            print key, " found";
            return 
        elif self.data > key and self.left is not None:
            self.left.search(key);
        elif self.data < key and self.right is not None:
            self.right.search(key)
            
    def search(self, key, queue):    
        if self.data == key:
            #queue.append(self.data);
            pass;
        elif self.data > key and self.left is not None:
            queue.append(self.data);
            self.left.search(key,queue);
        elif self.data < key and self.right is not None:
            queue.append(self.data);
            self.right.search(key, queue);
        
        return queue
            
    def commonAncestor(self, key1, key2):
        queue1 = self.search(key1,deque([]));
        queue2 = self.search(key2,deque([]));
        
        ancestor = None;
        try:
            while queue1:
                node1 = queue1.popleft();
                node2 = queue2.popleft();
                if node1 == node2:
                    ancestor = node1;
                else:
                    return ancestor;
        except IndexError:
            return ancestor;
            
    def breadthFirstTraversal(self, queue):      
        while len(queue) > 0:
            node = queue.popleft();
            print node.data
            if node.left:   
                queue.append(node.left);
            if node.right:
                queue.append(node.right);
    
    def findLeafNodes(self): 
        if self.left:
            self.left.findLeafNodes();
        
        if self.right:
            self.right.findLeafNodes();
        
        if self.left is None and self.right is None:
            print self.data
            
    def pathToLeafNodes(self, stack):
        stack.append(self.data);
        
        if self.left is None and self.right is None:
            print stack;
            stack.pop();
            
        if self.left:
            self.left.pathToLeafNodes(stack);
        
        if self.right:
            self.right.pathToLeafNodes(stack);
            stack.pop();
    
    def mirror(self):
        temp = self.left
        self.left = self.right
        self.right = temp
        
        if self.left:
            self.left.mirror()
        
        if self.right:
            self.right.mirror()
            
    def size(self, Node):
        if Node is None:
            return 0;
        else:
            return (self.size(Node.left) + 1 + self.size(Node.right));
    
    def minValue(self):
        while self.left is not None:
            self = self.left
        
        return self.data
    
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