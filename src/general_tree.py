#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_children(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"

def iterative_deepening_search(root, goal):
    def depth_limited_search(node, goal, limit):
        if node is None:
            return False
        if node.value == goal:
            return True
        if limit == 0:
            return False
        return (
            depth_limited_search(node.left, goal, limit - 1) or
            depth_limited_search(node.right, goal, limit - 1)
        )

    depth = 0
    while True:
        found = depth_limited_search(root, goal, depth)
        if found:
            return True
        depth += 1

# Построение дерева
root = BinaryTreeNode(1)
left_child = BinaryTreeNode(2)
right_child = BinaryTreeNode(3)
root.add_children(left_child, right_child)
right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))

# Целевое значение
goal = 4

# Поиск с итеративным углублением
result = iterative_deepening_search(root, goal)

print(result)
