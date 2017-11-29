# Accepted
# Given an array and a value, remove all instances of that value in place and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example:
# Given input array nums = [3,2,2,3], val = 3
# Your function should return length = 2, with the first two elements of nums being 2.


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        start = 0
        end = len(nums)-1

        while start<=end:
        	if(nums[start] == val):
        		nums[start]=nums[end]
        		end = end-1
        		continue
        	start = start+1

        return end+1


sol = Solution()
print(sol.removeElement([3,3,2,2,3],3))
