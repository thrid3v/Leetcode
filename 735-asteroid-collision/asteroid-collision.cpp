class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> st;
        for (int ast : asteroids) {
            bool exploded = false;
            while (!st.empty() && st.back() > 0 && ast < 0) {
                if (st.back() < -ast) {
                    st.pop_back();
                    continue;
                } else if (st.back() == -ast) {
                    st.pop_back();
                    exploded = true;
                    break;
                } else {
                    exploded = true;
                    break;
                }
            }
            if (exploded == false) {
                st.push_back(ast);
            }
        }
        return st;
    }
};