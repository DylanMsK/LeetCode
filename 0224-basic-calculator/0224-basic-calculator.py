class Solution:
  def calculate(self, s: str) -> int:
    result, temp = 0, 0
    op = 1
    stack = [op]

    for c in s:
      if c.isdigit():
        temp *= 10
        temp += int(c)
      elif c == '(':
        stack.append(op)
      elif c == ')':
        stack.pop()
      elif c == '+' or c == '-':
        result += op * temp
        op = (1 if c == '+' else -1) * stack[-1]
        temp = 0

    return result + op * temp