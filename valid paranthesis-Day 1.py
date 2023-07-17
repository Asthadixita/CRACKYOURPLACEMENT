class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s)%2!=0):
            return false
        dict={'(':')','{':'}','[':']'}  #'keys:data'
        stack=[]
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack==[]:  #stack is empty
                    return false
                a=stack.pop()
                if i!= dict[a]:
                    return False
        return stack==[]                

    