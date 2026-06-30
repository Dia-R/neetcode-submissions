class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_dict = {"]": "[", "}": "{", ")": "("}
        for bracket in s:
            if bracket in stack_dict:
                if stack and stack[-1] == stack_dict[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        if stack:
            return False
        return True


        