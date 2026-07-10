class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        zipped = nums1 + nums2
        zipped.sort()

        n = len(zipped)

        if n % 2 == 0:
            sol = zipped[(n//2)-1] + zipped[(n//2)]
            sol /= 2
            return sol 
        else:
            sol = zipped[(n//2)]
            return sol



