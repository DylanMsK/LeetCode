class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        total_length = word_length * len(words)
        window = "".join(sorted(words))

        result = []
        for i in range(len(s)-total_length+1):
            combined_words = [s[j:j+word_length] for j in range(i, i+total_length, word_length)]
            sorted_word = "".join(sorted(combined_words))
            if sorted_word == window:
                result.append(i)
        return result