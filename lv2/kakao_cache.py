"""
입력된 도시이름 배열을 순서대로 처리할 때, 총 실행시간을 출력

캐시 교체 알고리즘은 LRU(least recently used)사용
cache hit일 경우 실행시간 1
cache miss일 경우 실행시간 5
"""
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()  # cache는 cache사이즈를 넘어서면 안됨
    if cacheSize > 0:
        for i in range(len(cities)):
            lower = cities[i].lower()
            if lower not in cache:
                answer += 5
                if len(cache) >= cacheSize:
                    cache.popleft()
                cache.append(lower)
            else:
                # 기존것이라도 가장 마지막에 오도록 갱신
                answer += 1
                temp_arr = []
                while cache:
                    temp = cache.popleft()
                    if temp != lower:
                        temp_arr.append(temp)
                for i in range(len(temp_arr)):
                    cache.append(temp_arr[i])
                cache.append(lower)
    else:
        answer = len(cities) * 5
    return answer


cache_size = 3
cities1 = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
]
cities2 = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "Pangyo",
    "Jeju",
    "Seoul",
    "Seoul",
    "Jeju",
    "Pangyo",
]
cities3 = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "SanFrancisco",
    "Seoul",
    "Rome",
    "Paris",
    "Jeju",
    "NewYork",
    "Rome",
]
print(solution(cache_size, cities2))