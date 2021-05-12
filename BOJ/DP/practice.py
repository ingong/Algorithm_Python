import sys

string_a = ' ' + sys.stdin.readline().rstrip()
string_b = ' ' + sys.stdin.readline().rstrip()
dp = [[0] * len(string_b) for _ in range(len(string_a))]
print(dp)