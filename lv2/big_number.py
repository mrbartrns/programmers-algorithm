"""
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
"""
"""
# 999999999 일때 처리 필요
def solution(number, k):
    answer = number
    n = 0
    done = False
    while n < k:
        for i in range(len(answer) - 1):
            if int(answer[i]) < int(answer[i + 1]):
                answer = answer[:i] + answer[i + 1 :]
                done = False
                n += 1
                break
            else:
                done = True
        if done:
            answer = answer[:-1]
            n += 1
    return answer
"""


def solution(number, k):
    answer = []
    for _ in range(len(number) - k):
        val = "0"
        for i in range(len(number)):
            if val < number[i]:
                val = number[i]
                if val == "9":
                    break
        answer.append(val)
    res = "".join(answer)
    return res


print(solution("1111111", 6))
