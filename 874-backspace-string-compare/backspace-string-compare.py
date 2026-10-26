class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def strcmp(a):
            stack = []
            for i in range(len(a)):
                if a[i] != "#":
                    stack.append(a[i])
                elif stack:
                    stack.pop() 
            return stack

        return strcmp(s) == strcmp(t)