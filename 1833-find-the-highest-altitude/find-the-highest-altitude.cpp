class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int n = gain.size();
        vector<int> altitudes(n + 1);
        altitudes[0] = 0;
        for (int i = 1; i < n + 1; i++) {
            altitudes[i] = altitudes[i - 1] + gain[i - 1];
        }
        int maxi = 0;
        int j = 0;
        int m = altitudes.size();
        while (j < m) {
            maxi = max(maxi, altitudes[j]);
            j++;
        }
        return maxi;
    }
};