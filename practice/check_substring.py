# Check Substring
# Given two strings s and t, check if t is a substring of s.
# A substring is contiguous non-empty sequence of characters within a string

# Test Cases:
# s = "hello", t = "ll" → ✅ True (substring found at index 2)
# s = "abcdef", t = "gh" → ❌ False
# s = "abcabcabc", t = "cab" → ✅ True (appears starting at index 2)
# s = "abcd", t = "abcd" → ✅ True (whole string is substring)
# s = "abcd", t = "" → ✅ True (empty string is always a substring)


def check_substring(s: str, t: str) -> bool:
    if s == t or t == "":
        return True

    for i in range(len(s) - len(t) + 1):
        if s[i : i + len(t)] == t:
            return True
    return False


def main():
    print(check_substring("hello", "ll"))
    print(check_substring("abcdef", "gh"))
    print(check_substring("abcabcabc", "cab"))


if __name__ == "__main__":
    main()
