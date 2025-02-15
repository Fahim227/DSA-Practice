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
    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root,value)
                    
    def __r_insert(self,current_node,value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left,value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)
        return current_node
    
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

    def __r_contains(self,current_node:Node,value):
        if current_node == None: 
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left,value)
        if value > current_node.value:
            return self.__r_contains(current_node.right,value)
        return False

    def r_contains(self,value):
        return self.__r_contains(self.root,value)

    def min_value(self,current_node:Node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def __r_delete(self,current_node:Node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left,value)
        if value > current_node.value:
            current_node.right = self.__r_delete(current_node.right,value)
        else: 
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                return current_node.left
            else:
                sub_tree_min_value = self.min_value(current_node.right)
                current_node.value = sub_tree_min_value
                current_node.right = self.__r_delete(current_node.right,sub_tree_min_value)
        return current_node

    def r_delete(self,value):
        self.__r_delete(self.root,value)

my_tree = BinarySearchTree()

node = Node(2)

my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
my_tree.r_insert(5)
my_tree.r_insert(10)
my_tree.r_insert(10)
my_tree.r_insert(11)


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.r_contains(12))