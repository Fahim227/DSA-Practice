class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            else:
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right
                    
    def contains(self,value):
        if self.root is None : return False
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

my_tree = BinarySearchTree()


my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(5)
my_tree.insert(10)
my_tree.insert(10)
my_tree.insert(11)


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(11))