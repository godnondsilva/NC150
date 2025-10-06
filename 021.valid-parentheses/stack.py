class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in brackets:
                if stk and brackets[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c) 
        return True if not stk else False