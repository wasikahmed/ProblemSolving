# Isomorphic Strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for c1, c2 in zip(s, t):
            if (c1 in map_s_to_t and map_s_to_t[c1] != c2) or (
                c2 in map_t_to_s and map_t_to_s[c2] != c1
            ):
                return False
            map_s_to_t[c1] = c2
            map_t_to_s[c2] = c1

        return True


def main():
    s = Solution()
    print(s.isIsomorphic("egg", "add"))
    print(s.isIsomorphic("foo", "bar"))
    print(s.isIsomorphic("paper", "title"))
    print(s.isIsomorphic("badc", "baba"))


if __name__ == "__main__":
    main()
