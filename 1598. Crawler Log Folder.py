class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count=0

        for x in logs:
            if x=="../":
                count-=1
                if count<0:
                    count=0
            elif x=="./":
                continue
            else: 
                count+=1
        
        return count
        

