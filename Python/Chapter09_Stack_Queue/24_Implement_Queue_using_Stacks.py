# 232. Implement Queue using Stacks

class MyQueue:
    
    def __init__(self):
        self.st = []
        self.index = 0

    def push(self, x: int) -> None:
        self.st.append(x)
        
    def pop(self) -> int:
        self.index += 1
        return (self.st[self.index - 1])

    def peek(self) -> int:
        return self.st[self.index]

    def empty(self) -> bool:
        return (self.index == len(self.st))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()