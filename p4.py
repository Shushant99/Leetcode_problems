class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=nums1+nums2
        num3.sort()
        median=0
        if len(num3)%2==0:
            temp1=num3[(len(num3)//2)-1]
            temp2=num3[(len(num3)//2)]
            median=(temp1+temp2)/2

        else:
            median=num3[len(num3)//2]
        return median