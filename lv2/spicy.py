"""
programmers 2단계 '더 맵게' 문제
모든 음식의 스코빌 지수를 K 이상으로 만들고 싶을 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해서는
스코빌 지수가 가장 낮은 두 개의 음식을 다음과 같이 특별한 방법으로 섞어야 한다.
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + 두 번째로 맵지 않은 음식의 스코빌 지수 * 2
모든 음식의 스코빌 지수가 K 이상이 될 때까지 섞는다.
"""
import heapq


class MinHeap:
    def __init__(self, arr=None):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        if len(self.heap) > 2:
            i = len(self.heap) - 1
            while i > 1:
                if self.heap[i // 2] > self.heap[i]:
                    self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                    i //= 2
                else:
                    break

    def get_value(self):
        if len(self.heap) > 2:
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        value = self.heap.pop()
        self.heapify(1)
        return value

    # 이부분이 이상
    def heapify(self, idx):
        smallest = idx
        if idx * 2 < len(self.heap) and self.heap[idx] > self.heap[idx * 2]:
            smallest = idx * 2
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
        if idx * 2 + 1 < len(self.heap) and self.heap[idx] > self.heap[idx * 2 + 1]:
            smallest = idx * 2 + 1
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
        if smallest != idx:
            self.heapify(smallest)

    def peek(self):
        return self.heap[1]

    def length(self):
        return len(self.heap) - 1

    def __str__(self):
        return str(self.heap[1:])


def solution(scoville, K):
    answer = 0  # 횟수
    heap = MinHeap()
    for i in scoville:
        heap.insert(i)
    while heap.length() > 1:
        if heap.peek() >= K:
            return answer
        else:
            make_it_spicy(heap)
            answer += 1
    if heap.peek() >= K:
        return answer
    else:
        return -1


def make_it_spicy(heap: list):
    min1 = heap.get_value()
    min2 = heap.get_value()
    new_value = min1 + (2 * min2)
    heap.insert(new_value)


if __name__ == "__main__":
    a = [4, 3, 1, 2, 5, 4, 2, 5, 8, 5, 7, 9, 200039]
    arr1 = MinHeap()
    arr2 = []
    for i in a:
        arr1.insert(i)
        heapq.heappush(arr2, i)
    arr1.get_value()
    heapq.heappushpop(arr2, i)
    arr1.get_value()
    heapq.heappushpop(arr2, i)
    arr1.get_value()
    heapq.heappushpop(arr2, i)
    arr1.get_value()
    heapq.heappushpop(arr2, i)
    arr1.get_value()
    heapq.heappushpop(arr2, i)
    arr1.get_value()
    heapq.heappushpop(arr2, i)

    equal = False
    for i in (0, len(arr2)):
        equal = equal or (arr1.heap[i + 1] == arr2[i])

    print("equal? ", equal)
