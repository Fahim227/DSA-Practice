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


class TreeTraversal:

    def BFS(self,current_node:Node):
        queue = [current_node]
        results = []

        while queue:
            visiting = queue.pop(0)
            results.append(visiting.value)

            if visiting.left != None:
                queue.append(visiting.left)
            
            if visiting.right != None:
                queue.append(visiting.right)
        return results
    
    def DFS(self,tree:Node):
        results  = []
        def pre_order(tree:Node):
            results.append(tree.value)
            if tree.left is not None:
                pre_order(tree.left)
            if tree.right is not None:
                pre_order(tree.right)
                
        def post_order(tree:Node):
            if tree.left is not None:
                post_order(tree.left)
            if tree.right is not None:
                post_order(tree.right)
            results.append(tree.value)

        def in_order(tree:Node):
            if tree.left is not None:
                in_order(tree.left)
            results.append(tree.value)
            if tree.right is not None:
                in_order(tree.right)
            

        pre_order(tree)
        print("--- pre_order = {}".format(results))
        results = []
        post_order(tree)
        print("--- post_order = {}".format(results))
        results = []
        in_order(tree)
        print("--- in_order = {}".format(results))

            


my_tree = BinarySearchTree()

my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

tree_traversal = TreeTraversal()
# print(tree_traversal.BFS(my_tree.root))
print(tree_traversal.DFS(my_tree.root))