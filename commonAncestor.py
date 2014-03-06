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
    
    def search(self, key, queue):    
        if self.data == key:
            queue.append(self.data);
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
        while queue1:
            try:
                node1 = queue1.popleft();
                node2 = queue2.popleft();
                if node1 == node2:
                    ancestor = node1;
                else:
                    break;

            except IndexError:
                break;

        print ancestor
        

    def breadthFirstTraversal(self, queue):      
        while len(queue) > 0:
            node = queue.popleft();
            print node.data
            if node.left:   
                queue.append(node.left);
            if node.right:
                queue.append(node.right);

def build123():
    root = Node(11);
    root.insert(7);
    root.insert(15);
    root.insert(5);
    root.insert(9);
    root.insert(3);
    root.insert(6);
    root.insert(10);
    root.insert(14);
    #root.breadthFirstTraversal(deque([root]));
    root.commonAncestor(7,15);
    
    
if __name__ == '__main__':
    build123();