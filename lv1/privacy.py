def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)):
        if len(phone_number) - i < 5:
            answer += phone_number[i]
        else:
            answer += '*'
    return answer

print(solution('01033334444'))