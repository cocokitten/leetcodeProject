# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.



class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
        	return len(nums)

        index_i = 0
        index_j = 0

        while index_j < len(nums):
        	if nums[index_j]!=nums[index_i]:
        		nums[index_i+1]=nums[index_j]
        		index_i += 1

        	index_j += 1
        return index_i+1

sol = Solution()
print(sol.removeDuplicates([1,1,2]))