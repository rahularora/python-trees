from collections import deque
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
                
    def breadthFirstTraversal(self, queue):      
        while len(queue) > 0:
            node = queue.popleft();
            print node.data
            if node.left:   
                queue.append(node.left);
            if node.right:
                queue.append(node.right);
            
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
            

def build123():
    root = Node(7);
    root.insert(3);
    root.insert(1);
    root.insert(5);
    root.insert(4);
    root.insert(6);
    root.insert(14);
    root.insert(11);
    root.insert(9);
    root.insert(12);
    root.insert(13);
    root.insert(8);
    root.insert(10);
    root.breadthFirstTraversal(deque([root]));
    root.delete(11, root);
    print "\n";
    #root.breadthFirstTraversal(deque([root]));
    
    
if __name__ == '__main__':
    build123();