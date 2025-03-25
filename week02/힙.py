class MinHeap:
    def __init__(self):
        self.heap = [0]  # 0번 인덱스는 비워둠 (계산 편의용)

    def push(self, x):
        self.heap.append(x)
        idx = len(self.heap) - 1
        while idx > 1 and self.heap[idx] < self.heap[idx // 2]:
            self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
            idx //= 2

    def pop(self):
        if len(self.heap) <= 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._heapify(1)
        return root

    def _heapify(self, idx):
        smallest = idx
        left = idx * 2
        right = idx * 2 + 1
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]
            self._heapify(smallest)
