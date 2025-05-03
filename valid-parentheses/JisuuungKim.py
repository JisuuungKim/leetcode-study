class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if top == '(' and i == ')' or top == '{' and i == '}' or top == '[' and i == ']':
                    stack.pop()
                    continue
                return False

        if stack:
            return False
        return True

# self_feedback : dictionary 를 이용하여 같은 type의 화살표끼리 묶으면 더 깔끔하게 코드를 작성할 수 있다.
