class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n=len(candyType)//2
        type= len(set(candyType))
        return min(type,n)
        