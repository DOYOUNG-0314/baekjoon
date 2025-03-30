import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.read
preorder = list(map(int, input().split()))
idx = 0

def build_tree(lower, upper):
    global idx
    if idx >= len(preorder):
        return None
    
    val = preorder[idx]
    if not (lower < val < upper):
        return None

    idx += 1
    node = Node(val)
    node.left = build_tree(lower, val)
    node.right = build_tree(val, upper)
    return node

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

root = build_tree(float('-inf'), float('inf'))
postorder(root)
