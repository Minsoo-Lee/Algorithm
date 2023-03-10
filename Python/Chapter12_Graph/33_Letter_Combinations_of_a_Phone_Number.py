# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def dfs(index, tmp):
            if len(tmp) == len(digits):
                result.append(tmp)
                return
            for i in range(index, len(digits)):
                for ch in dic[digits[i]]:
                    dfs(i + 1, tmp + ch)
        
        if digits == "":
            return []
        dic = { "2" : "abc", "3":"def", "4":"ghi", "5":"jkl", 
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        dfs(0, "")
        return result