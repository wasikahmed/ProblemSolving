# Excel Sheet Column Number


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for i in range(len(columnTitle)):
            col_num += pow(26, len(columnTitle) - 1 - i) * (
                ord(columnTitle[i]) - ord("A") + 1
            )
        return col_num


def main():
    s = Solution()
    print(s.titleToNumber("A"))
    print(s.titleToNumber("AB"))
    print(s.titleToNumber("ZY"))


if __name__ == "__main__":
    main()
