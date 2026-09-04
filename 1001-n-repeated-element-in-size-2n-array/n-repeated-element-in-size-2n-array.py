class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1] or nums[i] == nums[i-2]):
                return nums[i]
        return nums[len(nums)-1]

        
        