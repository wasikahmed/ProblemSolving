# Is Subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i, j = 0, 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         t = t.replace(t[j], " ", 1)
        #         j += 1
        # t = t.replace(" ", "")
        # return s == t

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


def main():
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))


if __name__ == "__main__":
    main()
