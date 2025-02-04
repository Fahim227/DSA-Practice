class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child_index(self,index):
        return 2 * index + 1
    
    def _right_child_index(self,index):
        return 2 * index + 2
    
    def _parent_index(self,index):
        return (index - 1) // 2
    
    def _swap(self,index1,index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent_index(current)]:
            self._swap(current, self._parent_index(current))
            current = self._parent_index(current)

    def remove_value(self,value):
        target_index = self.heap.index(value)

        left_index = self._left_child_index(target_index)
        right_index = self._right_child_index(target_index)
        max_index = len(self.heap)-1
        is_in_range = (left_index <= max_index and right_index <= max_index ) 
        if is_in_range:
            if  self.heap[left_index] > self.heap[right_index]:
                self._swap(target_index,left_index)
            else:
                self._swap(target_index,right_index)            
        self.heap.remove(value)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    def _sink_down(self,index):
        max = index
        while True:
            left = self._left_child_index(index)
            right = self._right_child_index(index)

            if left<len(self.heap) and self.heap[left] > self.heap[max]:
                max = left
            
            if right<len(self.heap) and self.heap[right] > self.heap[max]:
                max = right
            
            if max != index:
                self._swap(max,index)
                index = max
            else :
                return


class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child_index(self,index):
        return 2 * index + 1
    
    def _right_child_index(self,index):
        return 2 * index + 2
    
    def _parent_index(self,index):
        return (index - 1) // 2
    
    def _swap(self,index1,index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent_index(current)]:
            self._swap(current, self._parent_index(current))
            current = self._parent_index(current)
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_value
    
    def _sink_down(self,index):
        min_index = index
        while True:
            left = self._left_child_index(index)
            right = self._right_child_index(index)

            if left<len(self.heap) and self.heap[left] < self.heap[min_index]:
                min_index = left
            
            if right<len(self.heap) and self.heap[right] < self.heap[min_index]:
                min_index = right
            
            if min_index != index:
                self._swap(min_index,index)
                index = min_index
            else :
                return


myHeap = MaxHeap()
myHeap.insert(99)
myHeap.insert(72)
myHeap.insert(61)
myHeap.insert(58)



myHeap.insert(100)


myHeap.insert(75)
print(myHeap.heap)


# myHeap.remove_value(72)
myHeap.remove()

print(myHeap.heap)