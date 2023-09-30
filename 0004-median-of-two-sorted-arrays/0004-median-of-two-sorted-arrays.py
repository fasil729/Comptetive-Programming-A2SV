class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num_merge=sorted(nums1+nums2)
        n=len(num_merge)
        if n%2==0:
            return (num_merge[int(n/2)-1]+num_merge[int(n/2)+1-1])/2
        else:
            return num_merge[int(((n+1)/2)-1)]
        