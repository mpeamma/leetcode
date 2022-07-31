from typing import List


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


def print_tree(node, tabs=""):
    print(f"{tabs}({node.start}, {node.end}) = {node.total}")
    if node.left:
        print_tree(node.left, tabs + "\t")
        print_tree(node.right, tabs + "\t")

def build_tree(nums, start, end) -> Node:
    node = Node(start, end)

    if start == end:
        node.total = nums[start]
    else:
        node.left = build_tree(nums, start, (start + end) // 2)
        node.right = build_tree(nums, ((start + end) // 2) + 1, end)
        node.total = node.left.total + node.right.total
    return node

def sum_tree(root, start, end):
    
    if root.start == start and root.end == end:
        return root.total
    
    mid = (root.start + root.end) // 2

    if end <= mid:
        return sum_tree(root.left, start, end)
    elif start >= mid + 1:
        return sum_tree(root.right, start, end)
    else:
        return sum_tree(root.left, start, mid) + sum_tree(root.right, mid+1, end)

class NumArray:

    def __init__(self, nums: List[int]):
        self.root = build_tree(nums, 0, len(nums) - 1)
        
    def print(self):
        print_tree(self.root)

    def update(self, index: int, val: int) -> None:
        current = self.root
        update_list = [current]
        while current.left is not None and current.right is not None:
            if index <= current.left.end and index >= current.left.start:
                update_list.append(current.left)
                current = current.left
            else:
                update_list.append(current.right)
                current = current.right
        diff = current.total - val
        for node in update_list:
            node.total -= diff
        

    def sumRange(self, start, end):
        return sum_tree(self.root, start, end)


numArray = NumArray([1, 3, 5]);
numArray.print()
print(numArray.sumRange(0, 2))
numArray.update(1, 2)
numArray.print()
print(numArray.sumRange(0, 2))
