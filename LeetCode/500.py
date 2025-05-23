# Keyboard Row

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # row1, row2, row3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        # res = []
        #
        # for i in range(len(words)):
        #     word = words[i].lower()
        #     row = None
        #     flag = True
        #     if word[0] in row1:
        #         row = row1
        #     elif word[0] in row2:
        #         row = row2
        #     else:
        #         row = row3
        #
        #     for j in range(1, len(word)):
        #         if word[j] not in row:
        #             flag = False
        #             break
        #
        #     if flag:
        #         res.append(words[i])
        #
        # return res

        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

        def is_one_row(word: str) -> bool:
            for row in rows:
                if word[0].lower() in row:
                    return all(c.lower() in row for c in word)
            return False

        return [word for word in words if is_one_row(word)]


def main():
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
    print(s.findWords(["omk"]))
    print(s.findWords(["adsdf", "sfd"]))


if __name__ == "__main__":
    main()
