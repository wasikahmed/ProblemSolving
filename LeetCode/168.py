# Excel Sheet Column Title


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            title = chr(ord("A") + remainder) + title
            columnNumber //= 26
        return title


def main():
    s = Solution()
    print(s.convertToTitle(1))
    print(s.convertToTitle(28))
    print(s.convertToTitle(79))
    print(s.convertToTitle(2147483647))


if __name__ == "__main__":
    main()
