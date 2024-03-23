class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(0, len(s)):
            if s[i:i+1] == '(':
                stack.append('(')
            elif s[i:i+1] == ')':
                if len(stack) == 0:
                   return False
                if stack.pop() != '(':
                    return False
            elif s[i:i+1] == '{':
                stack.append('{')
            elif s[i:i+1] == '}':
                if len(stack) == 0:
                   return False
                if stack.pop() != '{':
                    return False
            elif s[i:i+1] == '[':
                stack.append('[')
            elif s[i:i+1] == ']':
                if len(stack) == 0:
                   return False
                if stack.pop() != '[':
                    return False

        return len(stack) == 0