# Ransom Note


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ## 1st solution ##

        # freq_map_magazine = {}
        # for char in magazine:
        #     freq_map_magazine[char] = freq_map_magazine.get(char, 0) + 1
        #
        # for char in ransomNote:
        #     if char not in freq_map_magazine:
        #         return False
        #     if not freq_map_magazine[char] > 0:
        #         return False
        #     freq_map_magazine[char] -= 1
        # return True

        ## 2nd solution ##

        for element in ransomNote:
            if element in magazine:
                magazine = magazine.replace(element, " ", 1)
            else:
                return False
        return True


def main():
    s = Solution()
    print(s.canConstruct("a", "b"))
    print(s.canConstruct("aa", "ab"))
    print(s.canConstruct("aa", "aab"))


if __name__ == "__main__":
    main()
