
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0
    
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()

class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self, value):
        return self.items.insert(0, value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].data

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinarTree(object):
    def __init__(self, root_value):
        self.root = Node(root_value)

    def print_traversals(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_traversal(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_traversal(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_traversal(self.root, '')
        elif traversal_type == 'levelorder':
            return self.levelorder(self.root)
        elif traversal_type == 'reverselevelorder':
            return self.reverselevelorder_traversal(self.root)
        else:
            return f'This traversal "{traversal_type}" is Not a valid one!!'
    
    def preorder_traversal(self, start, traversal):
        if start:
            traversal+= str(start.data)+'-'
            traversal = self.preorder_traversal(start.left,traversal)
            traversal = self.preorder_traversal(start.right,traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal+= str(start.data)+'-'
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += str(start.data)+'-'
        return traversal

    def levelorder(self, start):
        if start is None :
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        while len(queue)>0:
            traversal+= str(queue.peek())+'-'
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverselevelorder_traversal(self, start):
        if start is None:
            return 
        queue = Queue()
        queue.enqueue(start)
        stack = Stack()
        traversal = ""
        while len(queue)>0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack)>0:
            n = stack.pop()
            traversal += str(n.data)+'-'
        return traversal

    def height(self, start):
        if start is None:
            return -1
        left_height = self.height(start.left)
        right_height = self.height(start.right)
        return 1+max(left_height,right_height)

    def size(self, node):
        if node is None:
            return 0
        return 1 +self.size(node.left)+self.size(node.right)
        

            

    



tree = BinarTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.size(tree.root))