class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { ')' : '(', '}' : '{', ']': '['}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if brackets[char] != top:
                    return False
        return not stack

