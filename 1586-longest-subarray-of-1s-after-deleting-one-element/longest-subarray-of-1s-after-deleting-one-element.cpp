class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0;
        int right = 0;
        int zeros = 0;
        int maxlen = 0;
        int k = 1;
        while (right < nums.size()) {
            if (nums[right] == 0) {
                zeros++;
            }
            while (zeros > k) {
                if (nums[left] == 0) {
                    zeros--;
                }
                left++;
            }
            maxlen = max(maxlen, right - left);
            right++;
        }
        return maxlen;
    }
};