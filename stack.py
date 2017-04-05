from stack_base import StackBase


class Stack(StackBase):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.insert(0, value)

    def pop(self):
        return self.stack.pop(0)

    def look(self):
        return self.stack[0] if self.stack else None

