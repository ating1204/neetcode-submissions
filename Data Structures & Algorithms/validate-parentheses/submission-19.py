class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}": "{", ")": "(", "]": "["}
        stack = []
        for ch in s:
            if ch in list(brackets.values()): #{,(, [
                stack.append(ch)
            if ch in brackets:
                if stack and brackets[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True
