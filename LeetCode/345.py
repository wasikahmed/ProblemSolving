# Reverse Vowels of a String


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return "".join(s)


def main():
    s = Solution()
    print(s.reverseVowels("IceCreAm"))
    print(s.reverseVowels("leetcode"))


if __name__ == "__main__":
    main()
