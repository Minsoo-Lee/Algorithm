# 5. Longest Palindromic Substring

class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
    
    def longestPalindrome(self, s: str) -> int:
        longest = []
        if len(s) < 2 or s == s[::-1]:
            return s
        for i in range(len(s)):
            if len(longest) < len(self.expand(s, i, i + 1)):
                longest = self.expand(s, i, i + 1)
            if len(longest) < len(self.expand(s, i, i + 2)):
                longest = self.expand(s, i, i + 2)
        return longest
        
        