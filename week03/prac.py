import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 넉넉하게 설정 (노드 수 최대 10,000개)

# 입력을 빠르게 처리하기 위해 input() 대신 sys.stdin.read() 사용
input = sys.stdin.read

# 전위 순회 결과를 숫자 리스트로 저장
preorder = list(map(int, input().split()))

# 전역 인덱스: 전위 순회 리스트에서 현재 처리할 위치를 추적
idx = 0

# 트리 노드 클래스 정의
class Node:
    def __init__(self, val):
        self.val = val      # 노드에 저장된 값
        self.left = None    # 왼쪽 자식 노드
        self.right = None   # 오른쪽 자식 노드

# 전위 순회를 기반으로 BST를 효율적으로 생성하는 함수
def build_tree(lower, upper):
    global idx

    # 리스트 끝까지 다 보면 종료
    if idx >= len(preorder):
        return None

    val = preorder[idx]

    # 현재 노드 값이 허용된 범위를 벗어나면 이 서브트리에는 포함되면 안 됨
    if not (lower < val < upper):
        return None

    # 현재 값을 사용할 거니까 인덱스 증가
    idx += 1

    # 새 노드 생성
    node = Node(val)

    # 왼쪽 자식 트리 구성 (현재 값보다 작은 범위)
    node.left = build_tree(lower, val)

    # 오른쪽 자식 트리 구성 (현재 값보다 큰 범위)
    node.right = build_tree(val, upper)

    return node

# 후위 순회 (왼 → 오 → 루트 순서로 출력)
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

# 트리 생성 시작 (범위는 무제한으로 시작: -∞ ~ ∞)
root = build_tree(float('-inf'), float('inf'))

# 완성된 트리를 후위 순회하여 출력
postorder(root)