class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        nums = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = [c for c in nums[digits[0]]]
        for n in digits[1:]:
            temp = []
            for comb in result:
                for c in nums[n]:
                    temp.append(comb+c)
            result = temp
        return result
        

