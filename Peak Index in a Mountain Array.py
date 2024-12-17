class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        right=len(arr)-1
        left=0
        
        while left<right:
            n=(right+left)//2
            if arr[n]<arr[n+1]:
                left=n+1
            elif arr[n]>arr[n+1]:
                right=n
        return left
        