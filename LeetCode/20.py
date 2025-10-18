# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if len(stack) == 0 and c in map.keys():
                return False
            if c in map.values():
                stack.append(c)
                continue
            if not map[c] == stack[-1]:
                return False
            stack.pop()
        return len(stack) == 0

def main():
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([])"))
    print(s.isValid("([)]"))


if __name__ == "__main__":
    main()