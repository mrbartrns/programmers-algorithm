"""
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    seconds = 0
    bridge = deque([])
    trucks = deque(truck_weights)
    crossed = []
    # 트럭이 다리 위로 올라갈 때
    while crossed != truck_weights:
        while len(bridge) < bridge_length:
            if trucks and sum(bridge) + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
            else:
                bridge.append(0)
            seconds += 1
            # 트럭이 다리 끝까지 왔을 때
        if trucks:
            truck = bridge.popleft()
            if truck != 0:
                crossed.append(truck)
        else:
            while bridge:
                truck = bridge.popleft()
                if truck != 0:
                    crossed.append(truck)
                seconds += 1
                if crossed == truck_weights:
                    break

    return seconds


bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(bridge_length, weight, truck_weights))