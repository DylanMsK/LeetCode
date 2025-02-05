class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        s1_diff = []
        s2_diff = []
        for a, b in zip(s1, s2):
            if a != b:
                s1_diff.append(a)
                s2_diff.append(b)
                if len(s1_diff) > 2:
                    return False

        s1_diff.sort()
        s2_diff.sort()
        for a, b in zip(s1_diff, s2_diff):
            if a != b:
                return False
        return True