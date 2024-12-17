class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i={}
        s={}
        count={}
        a=[]
        for x in range (len(nums)):
            if nums[x] not in i:
                i[nums[x]]=x
                count[nums[x]]=1
                s[nums[x]]=x
            else:
                s[nums[x]]=x
                count[nums[x]]+=1
        k=max(count.values())
        for x in count:
            if count[x]==k:
                a.append(s[x]-i[x]+1)
        return min(a)



        