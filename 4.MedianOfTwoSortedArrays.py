# Accepted

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        index1 = 0
        index2 = 0
        mergedArr=[]
        while index1<len(nums1) and index2<len(nums2):

            if nums1[index1]<nums2[index2]:
                mergedArr.append(nums1[index1])
                index1 = index1+1

            elif nums1[index1]>nums2[index2]:
                mergedArr.append(nums2[index2])
                index2 = index2+1
            else:
                mergedArr.append(nums1[index1])
                mergedArr.append(nums2[index2])
                index1 = index1+1
                index2 = index2+1

        if index1!=len(nums1):
            while index1<len(nums1):
                mergedArr.append(nums1[index1])
                index1 = index1+1
        
        if index2!=len(nums2):
            while index2<len(nums2):
                mergedArr.append(nums2[index2])
                index2 = index2+1

        mergedLen = len(mergedArr)
        l = mergedLen//2

        if mergedLen%2 == 0:
            return (mergedArr[l]+mergedArr[l-1])/2
        else:
            return mergedArr[l]

sol = Solution()
arr1 = [1,2,3]
arr2 = [3,4,5]
print(sol.findMedianSortedArrays(arr1,arr2))


     		



     		
        

	