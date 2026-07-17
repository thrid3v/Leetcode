class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        low, high = 0, m
        half = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2
            j = half - i
            
            L1 = nums1[i-1] if i > 0 else float('-inf')
            R1 = nums1[i] if i < m else float('inf')
            L2 = nums2[j-1] if j > 0 else float('-inf')
            R2 = nums2[j] if j < n else float('inf') 
            
            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2 != 0:
                    return float(max(L1, L2))
                return (max(L1, L2) + min(R1, R2)) / 2.0
            elif L1 > R2:
                high = i - 1
            else:
                low = i + 1