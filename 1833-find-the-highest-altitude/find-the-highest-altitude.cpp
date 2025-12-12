class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int max_height = 0;
        int current_height = 0;

        for (int x : gain) {
            current_height += x;
            max_height = max(max_height, current_height);
        }
        return max_height;
    }
};