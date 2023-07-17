class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n1=len(haystack)
        n2=len(needle)
        if(n2>n1):
            return -1
        else:
            i=0
            j=0
            start=0
            while(i<n1 and j<n2):
                if(haystack[i]==needle[j]):
                    if(i-start+1==n2):
                        return start
                    i+=1
                    j+=1
                else:
                    j=0
                    start+=1
                    i=start
            return -1  