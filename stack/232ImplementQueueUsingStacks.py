class MyQueue:
    # def __init__(self):
    #     self.input_stack = []
    #     self.output_stack = []

    # def push(self, x):
    #     self.input_stack.append(x)

    # def pop(self):
    #     self.move_elements()
    #     if self.output_stack:
    #         return self.output_stack.pop()
    #     else:
    #         return None  # Queue is empty

    # def peek(self):
    #     self.move_elements()
    #     if self.output_stack:
    #         return self.output_stack[-1]
    #     else:
    #         return None  # Queue is empty

    # def empty(self):
    #     return not self.input_stack and not self.output_stack

    # def move_elements(self):
    #     if not self.output_stack:
    #         while self.input_stack:
    #             self.output_stack.append(self.input_stack.pop())

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
