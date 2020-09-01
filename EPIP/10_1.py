import sys
import math
import heapq
from functools import partial
from collections import namedtuple


"""
Test if a binary tree is height-balanced
i.e. abs(height(left subtree) - heigh (right subtree)) = 1 for each node of the tree
"""

# For trees, function call stack is part of the space complexity

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_height_balanced(root):
    # O(n) time since we have to compute this for all n nodes of the tree
    # O(h) space since we have h calls in the call stack
    if root:
        # recursive step with a few optimizations
        left_balanced, left_height = is_height_balanced(root.left)
        if not left_balanced:
            return False, 0             # no need to compute height
        
        right_balanced, right_height = is_height_balanced(root.right)
        if not right_balanced:
            return False, 0

        # merge left and right results
        node_balanced = abs(left_height - right_height) <= 1
        node_height = max(left_height, right_height) + 1
        return node_balanced, node_height

    else:
        # base case
        return True, -1


if __name__ == "__main__":
    tree = BinaryTreeNode()
    
