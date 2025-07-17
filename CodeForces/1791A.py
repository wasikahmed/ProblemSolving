# Codeforces Checking

import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    letter = sys.stdin.readline().strip()
    
    if letter in "codeforces":
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")