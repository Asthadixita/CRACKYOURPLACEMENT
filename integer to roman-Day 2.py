class Solution(object):
    def intToRoman(self,num):
        romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        seqSize = len(romans)
        idx = seqSize - 1
        ans = ""
        while num > 0:
            while value[idx] <= num:
                ans += romans[idx]
                num -= value[idx]
            idx -= 1
        return ans