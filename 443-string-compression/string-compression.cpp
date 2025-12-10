class Solution {
public:
    int compress(vector<char>& chars) {
        int read = 0;
        int write = 0;
        int n = chars.size();

        while (read < n) {
            char current_char = chars[read];
            int count = 0;

            while (read < n && chars[read] == current_char) {
                read++;
                count++;
            }

            chars[write] = current_char;
            write++;

            if (count > 1) {
                string strCount = to_string(count);
                for (int j = 0; j < strCount.length(); j++) {
                    char c = strCount[j];
                    chars[write] = c;
                    write++;
                }
            }
        }
        return write;
    }
};