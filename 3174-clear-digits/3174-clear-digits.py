class Solution:
    def clearDigits(self, s: str) -> str:
        idx = 0
        result = list(s)
        while idx < len(result):
            if result[idx].isdigit():
                result.pop(idx)
                if idx != 0:
                    idx -= 1
                    result.pop(idx)
            else:
                idx += 1
        return "".join(result)
            