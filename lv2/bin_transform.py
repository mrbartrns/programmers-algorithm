"""
0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

x의 모든 0을 제거합니다.
x의 길이를 c라고 하면, x를 c를 2진법으로 표현한 문자열로 바꿉니다.
예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.

0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. 
s가 1이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.
answer = [이진변환 횟수, 변환과정에서 제거된 모든 0의 갯수]
"""


def solution(s):
    answer = [0, 0]
    solve(s, answer)
    return answer


def solve(string, answer):
    if string == "1":
        return
    else:
        new_string = ""
        for i in range(len(string)):
            if string[i] == "1":
                new_string += "1"
            else:
                answer[1] += 1
        len_string = bin(len(new_string))[2:]
        answer[0] += 1
        solve(len_string, answer)


answer = [0, 0]
solve("1111111", answer)
print(answer)