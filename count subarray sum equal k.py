class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        mpp = defaultdict(int)
        mpp[0]=1
        presum=0
        remove=0
        count=0
        for i in range(n):
            presum+=nums[i]
            remove=presum-k
            count+=mpp[remove]
            mpp[presum]+=1
        return count