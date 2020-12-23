def solution(n):
    arr = [0] * ((n * (n + 1) // 2) + 1)
    arr[0] = None
    solve(n, arr)
    arr = arr[1:]
    return arr


def solve(n, arr, num=1, k=1, i=0):
    if (k * (k - 1)) // 2 + 1 + i < len(arr) and (arr[(k * (k - 1)) // 2 + 1 + i]) == 0:
        while k < n - i:
            if arr[(k * (k - 1)) // 2 + 1 + i] == 0:
                arr[(k * (k - 1)) // 2 + 1 + i] = num
                num += 1
                k += 1

        if k == n - i:
            if (k * (k + 1)) // 2 - i > (k * (k - 1)) // 2 + 1 + i:
                for j in range((k * (k - 1)) // 2 + 1 + i, (k * (k + 1)) // 2 - i):
                    if arr[j] == 0:
                        arr[j] = num
                        num += 1

            else:
                arr[(k * (k - 1)) // 2 + 1 + i] = num

        while k > i + 1:
            if arr[(k * (k + 1)) // 2 - i] == 0:
                arr[(k * (k + 1)) // 2 - i] = num
                num += 1
                k -= 1
            else:
                break
        k += 1
        solve(n, arr, num, k + 1, i + 1)


print(solution(1))