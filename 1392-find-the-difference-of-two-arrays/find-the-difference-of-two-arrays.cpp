class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());

        vector<int> nums1_unique;
        vector<int> nums2_unique;

        for (int x : set1) {
            if (set2.count(x) == 0) {
                nums1_unique.push_back(x);
            }
        }

        for (int y : set2) {
            if (set1.count(y) == 0) {
                nums2_unique.push_back(y);
            }
        }

        return {nums1_unique, nums2_unique};
    }
};