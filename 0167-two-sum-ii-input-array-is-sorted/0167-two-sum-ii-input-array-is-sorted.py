class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = None
        for i in range(len(numbers)-1):
            if numbers[i] > target or numbers[i] == prev:
                continue

            for j in range(i+1, len(numbers)):
                _sum = numbers[i] + numbers[j]
                if _sum == target:
                    return [i+1, j+1]
                elif _sum > target:
                    break
                    
            prev = numbers[i]

        return None