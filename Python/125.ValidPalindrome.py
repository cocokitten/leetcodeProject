#-*- coding: UTF-8 -*-

# Accepted
# 1、只考虑字母和数字
#     s = '.,'  return true
#     s = ''    return true
# 2、去除空格和其他特殊字符
# 3、不区分大小写


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1

       	while start < end:
       		while s[start].isalnum() == False and start<end:
       			start = start + 1
       		while s[end].isalnum() == False and start<end:
       			end = end -1
       		if s[start].lower()!=s[end].lower():
       			return False
       		start = start+1
       		end = end-1

        return True

s= '.,'
sol = Solution()
print(sol.isPalindrome(s))







