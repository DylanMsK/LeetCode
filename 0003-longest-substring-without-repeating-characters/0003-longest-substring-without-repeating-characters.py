class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        start = 0
        end = 0

        while start < end or end <= len(s):
            sub = s[start:end]
            validated = set(s[start:end])
            if len(sub) == len(validated):
                _max = max(len(sub), _max)
                end += 1
                if end > len(s):
                    break
            else:
                start += 1

        return _max