class Solution(object):
    def calPoints(self, operations):
        stack = []
        for i in operations:
            if i == 'D':
                stack.append(stack[-1] * 2)
            elif i == 'C':
                stack.pop()
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)