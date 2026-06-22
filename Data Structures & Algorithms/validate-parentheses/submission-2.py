class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s :
            if i == '(' :
                stack.append(i)
            elif i == '{' :
                stack.append(i)
            elif i == '[' :
                print("hi")
                stack.append(i)
            elif not stack :
                return False
            elif i == ')' :
                if stack.pop() != '(':
                    return False
            elif i == '}' :
                if stack.pop() != '{':
                    return False
            elif i == ']' :
                if stack.pop() != '[':
                    return False
        return not stack

        