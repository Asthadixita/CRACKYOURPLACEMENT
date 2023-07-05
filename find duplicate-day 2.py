class Solution(object):
    def findDuplicate(self, nums):
        for num in nums:
            ind = abs(num)
            
            if nums[ind] < 0:
                return ind
            
            nums[ind] *= -1 
        