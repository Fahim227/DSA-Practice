class Sorting:

    def bubble_sort(self,nums):
        size = len(nums)
        for i in range(size-1,0,-1):
            for j in range(i):
                if nums[j] > nums [j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        print(nums)
    

    
    def selection_sort(self,nums):
        size = len(nums)
        for i in range(size):
            min_index = i
            for j in range(i+1,size):
                if nums[j] < nums[min_index]:
                    min_index = j
            if i != min_index:
                nums[i], nums[min_index] = nums[min_index],nums[i]
        print(nums)

    def insertion_sort(self,nums):
        size = len(nums)
        for i in range(1,size):
            swaping_index = i
            for j in range(i-1,0,-1):
                if nums[j] > nums[i]:
                    swaping_index = j
            if swaping_index != i:
                nums[i], nums[swaping_index] = nums[swaping_index],nums[i]
        print(nums)


                    

bubbleSort = Sorting()
bubbleSort.bubble_sort([4,2,6,5,1,3])
bubbleSort.selection_sort([4,2,6,5,1,3])
bubbleSort.insertion_sort([4,2,6,5,1,3])

