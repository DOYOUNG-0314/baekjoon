import sys
sys.setrecursionlimit(10000)

# 노드 클래스
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 트리 저장 딕셔너리
tree = {}

# 트리 만들기
n = int(input())
for _ in range(n):
    root, left, right = input().split()

    # 루트 노드가 없으면 새로 생성
    if root not in tree:
        tree[root] = Node(root)

    # 왼쪽 자식
    if left != '.':
        tree[left] = Node(left)
        tree[root].left = tree[left]
    # 오른쪽 자식
    if right != '.':
        tree[right] = Node(right)
        tree[root].right = tree[right]

# 순회 함수
def preorder(node):
    if node:
        print(node.val, end='')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end='')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end='')

# 루트는 항상 'A'
root = tree['A']
preorder(root)
print()
inorder(root)
print()
postorder(root)
