from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            x = self.q1.popleft()
            self.q2.append(x)
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        while len(self.q1) > 1:
            x = self.q1.popleft()
            self.q2.append(x)
        result = self.q1.popleft()
        self.q2.append(result)
        self.q1, self.q2 = self.q2, self.q1
        return result

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.pop()
print(param_3)
param_4 = obj.top()
print(param_4)
param_5 = obj.empty()
print(param_5)
