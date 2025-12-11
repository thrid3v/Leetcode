class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int operations = 0;
        int left = 0;
        int right = nums.size()-1;
        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == k) {
                left++;
                right--;
                operations++;
            } else if (sum < k) {
                left++;
            } else {
                right--;
            }
        }
        return operations;
    }
};