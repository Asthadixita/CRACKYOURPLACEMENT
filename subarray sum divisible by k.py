class Solution(object):
    def subarraysDivByK(self, nums, k):
        ans = 0
        prefix = 0
        count = [0] * k
        count[0] = 1

        for num in nums:

            prefix = (prefix + num % k + k) % k
            ans += count[prefix]
            count[prefix] += 1

        return ans