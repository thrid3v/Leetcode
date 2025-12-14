class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> counts;

        for (int x : arr) {
            counts[x]++;
        }

        unordered_set<int> unique_counts;

        for (auto it : counts) {
            int freq = it.second;
            unique_counts.insert(freq);
        }
        return unique_counts.size() == counts.size();
    }
};