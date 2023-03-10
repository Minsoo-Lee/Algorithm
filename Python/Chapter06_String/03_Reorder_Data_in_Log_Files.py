# 937. Reorder Data in Log Files

class Solution:
    def reorderLogFiles(self, logs):
        digits = []
        alphas = []
        
        for s in logs:
            if s.split(" ")[1].isdigit():
                digits.append(s)
            elif s.split(" ")[1].isalpha():
                alphas.append(s)

        print(alphas)
        for i in range(len(alphas)):
            index = i
            for j in range(i, len(alphas)):
                alphas1 = alphas[index].split(" ")[1:]
                alphas2 = alphas[j].split(" ")[1:]
                if alphas1 > alphas2:
                    index = j;
            alphas[i], alphas[index] = alphas[index], alphas[i]
        
        
        for i in range(len(alphas)):
            index = i
            for j in range(i + 1, len(alphas)):
                alphas1 = alphas[index].split(" ")[1:]
                alphas2 = alphas[j].split(" ")[1:]
                if alphas1 == alphas2:
                    if alphas[index].split(" ")[0] > alphas[j].split(" ")[0]:
                        index = j
            alphas[i], alphas[index] = alphas[index], alphas[i]
                        
        return alphas + digits
        