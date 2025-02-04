class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_str = self.sort_string(s)
            if anagrams.get(sorted_str):
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]

        return list(anagrams.values())

    def sort_string(self, string: str) -> str:
        temp = [s for s in string]
        return "".join(sorted(temp))
