# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = []
        for ch in s:
            if ch.isalpha():
                tmp.append(ch.lower())
            if ch.isdigit():
                tmp.append(ch)
        for i in range(len(tmp) // 2):
            if tmp[i] != tmp[len(tmp) - i - 1]:
                return False
        return True;
