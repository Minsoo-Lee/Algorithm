def perm(self, nums):
    result = []
    prev = []
    
    def dfs(elements):
        if len(elements) == 0:
            result.append(prev[:])
        for e in elements:
            next = elements[:]
            next.remove(e)
            
            prev.append(e)
            dfs(next)
            prev.pop()
            
    dfs(nums)
    return result

def factorial(n):
    if n == 1:
        return 1;
    return n * factorial(n - 1);

def perm_manual(nums):
    tmp = []
    result  = []
            
    dfs(result, tmp, 0)
    print(result)

def dfs(result, tmp, count):
    if count == factorial(len(nums)):
        return
    if len(nums) == len(tmp):
        result.append(tmp)
        tmp = []
        count += 1
    for i in nums:
        if i in tmp:
            continue;
        tmp.append(i)
        dfs(result, tmp, count)

nums = [1, 2, 3]
perm_manual(nums)
