class Solution {
public:
    int maxVowels(string s, int k) {
        int counter = 0;
        for (int i = 0; i < k; i++) {
            char h = s[i];
            if (isVovel(h) == true) {
                counter++;
            }
        }
        int maxCounter = counter;

        for (int m = k; m < s.size(); m++) {
            if (isVovel(s[m - k]) == false && isVovel(s[m]) == true) {
                counter++;
            } else if (isVovel(s[m - k]) == true && isVovel(s[m]) == false) {
                counter--;
            }
            maxCounter = max(maxCounter, counter);
        }
        return maxCounter;
    }

private:
    bool isVovel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
};