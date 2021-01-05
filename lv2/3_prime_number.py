def solution(nums):
    arr = []
    temp = 0
    count = 0
    is_prime = True

    # 합 배열 구하기
    for i in range(len(nums) - 2):
        temp += nums[i]
        for j in range(i + 1, len(nums) - 1):
            temp += nums[j]
            for k in range(j + 1, len(nums)):
                temp += nums[k]
                arr.append(temp)
                temp -= nums[k]
            temp -= nums[j]
        temp -= nums[i]

    # 소수 구하기
    # print(arr)
    for i in range(len(arr)):
        is_prime = True
        for j in range(2, int(arr[i] ** 1 / 2) + 1):
            if arr[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    return count


# nums = [1, 2, 3, 4]
nums = [1, 2, 7, 6, 4]
print(solution(nums))