# Accepted

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution:
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		h_len = len(haystack)
		n_len = len(needle)
		h_index = n_index = 0
		# h_index , n_index = 0 , 0

		while h_index < h_len and n_index < n_len:
			
			if haystack[h_index] != needle[n_index]:
			  
			  h_index = h_index - n_index +1
			  n_index = 0
			else:
			  h_index = h_index + 1
			  n_index = n_index + 1

			# if haystack[h_index] == needle[n_index]:
			# 	h_index = h_index+1
			# 	n_index = n_index+1
			# else:
			# 	h_index = h_index - n_index +1
			# 	n_index = 0

			 
		if n_index == n_len:
			return h_index - n_index 
		else: 
			return -1


sol = Solution()

print(sol.strStr("mississippi","issip"))
