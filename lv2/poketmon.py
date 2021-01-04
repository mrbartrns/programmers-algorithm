def solution(nums):
    n = -1
    counts = 0
    nums.sort()
    for i in range(len(nums)):
        if n != nums[i]:
            n = nums[i]
            counts += 1
        if counts == len(nums) // 2:
            break
    return counts


print(solution([3, 3, 3, 2, 2, 4]))