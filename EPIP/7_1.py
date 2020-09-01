import sys
import math
from functools import partial


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


"""
Write a program that takes two lists, assumed to be sorted, and returns their merge.
The only field your program can change in a node is its next field.
"""

def merge_sorted_lists(L1, L2):
    head = result = ListNode()

    # O(len(L1) + len(L2)) time, O(1) space
    while L1 and L2:
        if L1.val < L2.val:
            result.next, L1 = L1, L1.next
        else:
            result.next, L2 = L2, L2.next
        result = result.next
        
    result.next = L1 or L2
    return head.next


def create_list(ls):
    head = result = ListNode()
    for val in ls:
        result.next = ListNode(val=val)
        result = result.next
    return head.next


def print_list(L):
    result = ""
    while L:
        result += str(L.val) + (" -> " if L.next else "")
        L = L.next
    print(result)


if __name__ == "__main__":
    L1 = create_list([2, 5, 7])
    L2 = create_list([3 ,11])
    print_list(merge_sorted_lists(L1, L2))