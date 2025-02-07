class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        a=0
        stack=[]
        for x in range (1,n+1):
            if a<len(target) and target[a]==x:
                stack.append("Push")
                a+=1
            elif a<len(target) and target[a]!=x:
                stack.append("Push")
                stack.append("Pop")
        return stack






