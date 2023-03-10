# 344. Reverse String

class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]