# Longest Palindrome


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        res = 0
        has_odd_frq = False
        for freq in freq_map.values():
            if freq % 2 == 0:
                res += freq
            else:
                res += freq - 1
                has_odd_frq = True

        if has_odd_frq:
            return res + 1
        return res


def main():
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("s"))


if __name__ == "__main__":
    main()
