import sys
import math
from functools import partial
from collections import namedtuple


"""
Create a stack with a `max` API.
"""


class Stack():
    """
    O(1) space
    straightforward approach is to compute the max every push
    when popping:
    * if element popped is < max, no issue
    * if element popped is max, O(n) to get new max via linear search

    time-space tradeoff
    compute max for current stack for each push - additional O(n) space
    but for O(1) time max retrieval
    """
    ElementWithMax = namedtuple("ElementWithMax", ("val", "max"))

    def __init__(self):
        self._stack = []
    
    def is_empty(self):
        return not len(self._stack)

    def get_max(self):
        # check for empty stack
        if self.is_empty():
            raise IndexError("max(): empty stack")
        
        return self._stack[-1].max

    def push(self, el):
        self._stack.append(
            self.ElementWithMax(el, el if self.is_empty() else max(el, self.get_max()))
        )
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop(): empty stack")
        return self._stack.pop().val




if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    print(stack.get_max())
    stack.push(5)
    stack.push(2)
    print(stack.get_max())
    stack.pop()
    print(stack.get_max())
    stack.pop()
    print(stack.get_max())