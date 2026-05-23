class Solution:
    def myAtoi(self, s: str) -> int:
        INT_max = 2**31 - 1
        INT_min = -2**31

        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        if s[0] == "-":
            sign = -1
            index += 1
        elif s[0] == "+":
            index += 1

        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result *= sign

        if result > INT_max:
            return INT_max
        elif result < INT_min:
            return INT_min
        
        return result

        

        