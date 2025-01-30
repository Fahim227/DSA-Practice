class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value=value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value=value)
        if self.height == 0:
            self.top = new_node
            self.height = 1
            return True
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        pop_node = self.top
        self.top = self.top.next
        self.height -= 1
        return pop_node.value



my_stack = Stack(4)
my_stack.push(5)
my_stack.push(6)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.print_stack()