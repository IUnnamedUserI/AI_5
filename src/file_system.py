#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def __repr__(self):
        return f"<{self.value}>"

def iterative_deepening_search(root, goal):
    def depth_limited_search(node, goal, limit, path):
        if node is None:
            return False
        path.append(node.value)
        if node.value == goal:
            return True
        if limit == 0:
            path.pop()
            return False
        for child in node.children:
            if depth_limited_search(child, goal, limit - 1, path):
                return True
        path.pop()
        return False

    depth = 0
    while True:
        path = []
        found = depth_limited_search(root, goal, depth, path)
        if found:
            return " -> ".join(path)
        depth += 1

# Построение дерева
root = TreeNode("dir")
root.add_child(TreeNode("dir2"))
root.add_child(TreeNode("dir3"))
root.children[0].add_child(TreeNode("file4"))
root.children[1].add_child(TreeNode("file5"))
root.children[1].add_child(TreeNode("file6"))

# Цель поиска
goal = "file5"

# Поиск с итеративным углублением
result = iterative_deepening_search(root, goal)

print(result)
