import sys
import math
from functools import partial


class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def print_list(nodes):
    for node in nodes.values():
        print(f"{node.left.val if node.left else '*'} <- {node.val} -> {node.right.val if node.right else '*'}")


def main():
    while 1:
        s, b = list(map(int, sys.stdin.readline().strip().split()))
        if not s and not b: break
        nodes = {}
        left = None
        for i in range(s+1):
            node = ListNode(val=i, left=left)
            nodes[i] = node
            if left is not None: left.right = node
            left = node
        
        for _ in range(b):
            l, r = list(map(int, sys.stdin.readline().strip().split()))
            l_node, r_node = nodes[l], nodes[r]

            out_l = "*" if not l_node.left or not l_node.left.val else l_node.left
            out_r = "*" if not r_node.right or not r_node.right.val else r_node.right
            print(out_l, out_r)
            if l_node.left:
                l_node.left.right = r_node.right
            else:
                r_node.right.left = None

            if r_node.right:
                r_node.right.left = l_node.left
            else:
                l_node.left.right = None

        print("-")

if __name__ == "__main__":
    main()
