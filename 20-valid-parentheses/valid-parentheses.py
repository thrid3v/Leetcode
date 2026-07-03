class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if i not in hashmap:
                stack.append(i)
            else:
                if not stack:
                    return False
                
                popp = stack.pop()
                if popp != hashmap[i]:
                    return False
        if not stack:
            return True
        else:
            return False

        