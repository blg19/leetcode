class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        sum=0
        left=0
        right=len(nums)-1
        while left<right:
            a=str(nums[left]) + str(nums[right])
            sum+=int(a)
            left+=1
            right-=1
        if left==right:
            sum+=nums[left]
        
        return sum
