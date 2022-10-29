class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ind = 0
        l = len(nums)
        while ind<l:
            if nums[ind]==val:
                ind1 = ind
                while ind1<l-1:nums[ind1],ind1 = nums[ind1+1],ind1+1
                nums.pop(ind1)
                l-=1
            else:ind+=1