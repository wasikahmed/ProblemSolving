


# class Solution:
#     def lexSmallest(self, s: str) -> str:
#         result = s
#         for i in range(1, len(s)+1):
#             res_rev_first = s[:i-1][::-1] + s[i-1:]
#             res_rev_last = s[:i] + s[i:][::-1]
#             result = min(result, res_rev_first, res_rev_last)
#         return result

class Solution:
    def lexSmallest(self, s: str) -> str:
        result = s
        for i in range(len(s) + 1):
            res_rev_first = s[:i][::-1] + s[i:]
            res_rev_last = s[:i] + s[i:][::-1]
            
            result = min(result, res_rev_first, res_rev_last)
        return result

def main():
    s = Solution()
    print(s.lexSmallest("dcab"))
    print(s.lexSmallest("abba"))
    print(s.lexSmallest("zxy"))
    print(s.lexSmallest("lk"))



if __name__ == "__main__":
    main()