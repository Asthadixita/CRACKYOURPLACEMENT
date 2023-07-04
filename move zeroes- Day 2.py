class Solution(object):
    def moveZeroes(self, nums):
        index=0
        for i in range(len(nums)):
            if nums[i]==0:
                index=i
                break
        i=index
        j=i+1
        
        while(j<len(nums)):
            if(nums[i]==0 and nums[j]!=0):
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            else:
                j+=1
        return nums