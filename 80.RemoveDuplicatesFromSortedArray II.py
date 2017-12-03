
#-*-coding:utf-8-*-

#Follow up for "Remove Duplicates":
#What if duplicates are allowed at most twice?
#
#For example,
#Given sorted array nums = [1,1,1,2,2,3],
#
#Your function should return length = 5, 
#with the first five elements of nums being 1, 1, 2, 2 and 3. 
#It doesn't matter what you leave beyond the new length.
#

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3: return len(nums)
        i = 2      #遍历整个数组
        index = 2  #指向满足要求的数组的下一个元素

        while i<len(nums):
            if nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index = index+1
            i = i+1
        return index
      

sol = Solution()
print(sol.removeDuplicates([1,1,1]))
    