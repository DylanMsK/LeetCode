class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ")}]":
                if not stack:
                    return False
                    
                prev = stack.pop()
                if c == ")" and prev != "(":
                    return False
                elif c == "}" and prev != "{":
                    return False
                elif c == "]" and prev != "[":
                    return False
            else:
                stack.append(c)

        return not bool(stack)

