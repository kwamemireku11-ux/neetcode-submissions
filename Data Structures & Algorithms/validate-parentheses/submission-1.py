class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in brackets:
                if not stack:
                    return False
                top = stack.pop()
                if brackets[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
