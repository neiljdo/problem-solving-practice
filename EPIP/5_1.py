import sys
import math
from functools import partial


"""
Write a program that takes an array A and an index i into A, and rearranges the elements
such that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot, followed by elements greater than the pivot.

"""

def dutch_flag_partition(pivot_index, A):
    # O(n) time but with extra O(n) space for storing splits
    less, equal, greater = [], [], []
    pivot = A[pivot_index]
    for n in A:
        if n < pivot: less.append(n)
        elif n == pivot: equal.append(n)
        else: greater.append(n)
    result = []
    for n in less: result.append(n)
    for n in equal: result.append(n)
    for n in greater: result.append(n)
    return result 


def dutch_flag_partition_v2(pivot_index, A):
    # O(n) time but with O(1) space
    # reuse the original array
    pivot = A[pivot_index]
    smaller = 0
    # first pass: move all vals less than pivot to front
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
            print(A)
    # second pass: move all vals greater than pivot to end
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            # all values after this will be less than the pivot, we can stop
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
            print(A)


def dutch_flag_partition_v3(pivot_index, A):
    # Still O(n) time but with O(1) space
    # only does one pass ??
    # reuse the original array
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    print(A[:smaller], A[smaller:equal], A[equal:larger], A[larger:])
    while equal < larger:
        if A[equal] < pivot:
            print(f"A[{equal}] = {A[equal]} < {pivot}")
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            print(f"A[{equal}] = {A[equal]} = {pivot}")
            equal += 1
        else:
            print(f"A[{equal}] = {A[equal]} > {pivot}")
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
        print(smaller, equal, larger, A[:smaller], A[smaller:equal], A[equal:larger], A[larger:])

if __name__ == "__main__":
    A = [0, 1, 2, 0, 2, 1, 1]
    print(dutch_flag_partition(3, A))
    print(dutch_flag_partition(2, A))

    print("*****")
    print(dutch_flag_partition_v2(3, [0, 1, 2, 0, 2, 1, 1]))
    print("---")
    print(dutch_flag_partition_v2(2, [0, 1, 2, 0, 2, 1, 1]))
    print("*****")

    print("*****")
    print(dutch_flag_partition_v3(3, [0, 1, 2, 0, 2, 1, 1]))
    print("---")
    print(dutch_flag_partition_v3(1, [0, 1, 2, 0, 2, 1, 1]))
    print("*****")
