from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = len(digits) - 1
        
        while r >= 0:
            if digits[r] == 9:
                digits[r] = 0
                r -= 1 
            else:
                digits[r] += 1
                return digits
                
        return [1] + digits
            
        