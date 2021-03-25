#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isnumeric() or i[0] == "-" and i[1:].isnumeric():
                stack.append(int(i))
            else:
                a2 = stack.pop()
                a1 = stack.pop()
                if i == "+":
                    stack.append(a1 + a2)
                elif i == "-":
                    stack.append(a1 - a2)
                elif i == "*":
                    stack.append(a1 * a2)
                elif i == "/":
                    stack.append(int(a1 / a2))
        return stack[-1]

# @lc code=end

print(6//132)