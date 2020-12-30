def solution(clothes):
    answer = 0
    clothes_dict = {}
    only_one = True
    # dictionary 만드는 함수
    for i in range(len(clothes)):
        clothes_dict[clothes[i][1]] = clothes_dict.get(clothes[i][1], []) + [
            clothes[i][0]
        ]

    print(clothes_dict)
    keys = list(clothes_dict.keys())
    for key in clothes_dict:
        if len(clothes_dict[key]) != 1:
            only_one = False
            break
    if only_one:
        answer = 2 ** len(keys) - 1
    else:
        for i in range(1 << len(keys)):
            temp = 1
            for j in range(len(keys)):
                if i & (1 << j):
                    temp *= len(clothes_dict[keys[j]])
            if i != 0:
                answer += temp

    return answer


# arr = [
#     ["yellow_hat", "headgear"],
#     ["blue_sunglasses", "eyewear"],
#     ["green_turban", "headgear"],
# ]

# arr2 = [["crow_mask", "face"], ["blue_sunglasses", "hi"], ["smoky_makeup", "by"]]
arr2 = [[str(i)] * 2 for i in range(1, 31)]
print(arr2)

print(solution(arr2))
