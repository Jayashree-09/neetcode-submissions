class Solution:
    def isValid(self, s):
        stack = []
        pairs = {')':'(', ']': '[', '}': '{'}
        
        for char in s:
            if char in '([{':
                stack.append(char)

            elif char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
        return len(stack) == 0


solution = Solution()
print(solution.isValid("{[()]}"))