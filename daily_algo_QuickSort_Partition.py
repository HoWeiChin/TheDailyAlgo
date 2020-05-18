class Solution(object):
    def partition(self, nums, left, right):
        pivot = nums[left]
        i = left + 1
        j = i
        
        while j <= right:
            curr = nums[j]
            
            if curr <= pivot:
                inter = curr
                nums[j] = nums[i]
                nums[i] = inter
                i += 1
            j += 1
        
        inter = nums[i-1]
        nums[i-1] = pivot
        nums[left] = inter
    

        return i - 1
        
                
    def quicksort(self, nums, l, h):
        
        if l < h:
            pivot_position = self.partition(nums, l, h)
            self.quicksort(nums, l, pivot_position -1)
            self.quicksort(nums, pivot_position+1, h)
        
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quicksort(nums, 0, len(nums)-1)
        return nums
