def sum_comb(self, cand, target):
    result = []
    
    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        for i in range(index, len(cand)):
            dfs(csum - cand[i], i, path + [cand[i]])
    
    dfs(target, 0, [])
    return result
