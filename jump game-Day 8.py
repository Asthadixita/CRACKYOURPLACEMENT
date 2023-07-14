class Solution(object):
    def canJump(self, nums):
        right=0
        last=len(nums)-1
        for i in range(len(nums)):
            if i>right:
                return False
            if nums[i]+1>right:
                right=nums[i]+i
            if right>=last:
                return True

