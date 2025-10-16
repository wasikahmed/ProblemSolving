# Uncommon Words from Two Sentences

from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + " " + s2

        words = s.strip().split(" ")
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
                continue
            word_dict[word] += 1

        uncommon_word = []
        for word in word_dict.keys():
            if word_dict[word] == 1:
                uncommon_word.append(word)      

        return uncommon_word 

def main():
    s = Solution()
    print(s.uncommonFromSentences("this apple is sweet", "this apple is sour"))
    print(s.uncommonFromSentences("apple apple", "banana"))

if __name__ == "__main__":
    main()