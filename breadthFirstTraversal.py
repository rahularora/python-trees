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
    root.breadthFirstTraversal(deque([root]));
    
    
if __name__ == '__main__':
    build123();
            