# 819. Most Common Word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        dic = {}
        s = []
        tmp = []
        for ch in paragraph:
            if ch.isalpha():
                tmp.append(ch.lower())
            else:
                word = "".join(tmp)
                if word not in banned and word != "":
                    s.append("".join(tmp))
                tmp = []
        s.append("".join(tmp))
                
        print(s)
        
        for word in s:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 0
        
        max_key = ""
        for key in dic:
            if max_key == "":
                max_key = key
            if dic[key] > dic[max_key]:
                max_key = key
                
        return max_key
            