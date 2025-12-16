class Solution {
public:
    string removeStars(string s) {
        string sol = "";
        for (char c : s) {
            if (c == '*') {
                sol.pop_back();
            } else {
                sol += c;
            }
        }
        return sol;
    }
};