class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
       
        char_freq = {}
        for char in words[0]:
            char_freq[char] = char_freq.get(char, 0) + 1

        for word in words[1:]:
            word_freq = {}
            for char in word:
                word_freq[char] = word_freq.get(char, 0) + 1


            for char , freq in char_freq.items():
                if char in word_freq:
                    char_freq[char] = min(freq, word_freq[char])
                else:
                    char_freq[char] = 0  


        result = []
        for char, freq in char_freq.items():
            result.extend([char] * freq)
        return result

   