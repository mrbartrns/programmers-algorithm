"""
LZW 압축은 다음 과정을 거친다.

1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다.

"""


def solution(msg):
    answer = []
    word_dict = {}
    ord_a = ord("A")
    delta = 25
    # word_dict 초기화
    for i in range(delta + 1):
        word_dict[chr(ord_a + i)] = i + 1
    j = 0
    longest = 1
    k = longest
    # 이전 글자수의 갯수에 영향을 받는것이 아닌 무조건 딕셔너리에 등록된 가장 긴 숫자를 찾아야 한다.
    # 이전 숫자에 대해서 늘리는 것이 아닌, 무조건 가장 긴 수에서 부터 탐색한다면?
    while j < len(msg):
        if msg[j : j + k] not in word_dict:
            k -= 1
        else:
            answer.append(word_dict[msg[j : j + k]])
            # 답 배열에 추가한 후 그보다 하나 더 긴 단어가 딕셔너리에 없다면, 딕셔너리에 추가
            if j + k + 1 < len(msg) and msg[j : j + k + 1] not in word_dict:
                word_dict[msg[j : j + k + 1]] = len(word_dict) + 1
                # 딕셔너리 키의 길이가 바로 전보다 클경우, longest 갱신 (추가한 경우에만)
            j += k
            key_list = list(word_dict.keys())
            if len(key_list[-1]) > longest:
                longest = len(key_list[-1])
            k = longest

    print(word_dict)
    return answer


msg = "THATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATI"
print(solution(msg))

expected = [
    20,
    8,
    1,
    20,
    27,
    29,
    9,
    19,
    33,
    31,
    30,
    28,
    20,
    33,
    14,
    15,
    39,
    19,
    41,
    43,
    36,
    9,
    39,
    46,
    38,
    47,
]

# print(solution("THATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATI"))
print(expected)


"""
while j < len(msg):
    print("raw:", msg[j : j + length])
    if msg[j : j + length] not in word_dict:
        length -= 1
    if msg[j : j + length] in word_dict:
        answer.append(word_dict[msg[j : j + length]])
        print(f"after: {msg[j : j + length]} {word_dict[msg[j : j + length]]}")
        if j + length + 1 < len(msg) and msg[j : j + length + 1] not in word_dict:
            word_dict[msg[j : j + length + 1]] = last + 1
            print(f"saved: {msg[j : j + length + 1]}, {last + 1}")
        last += 1
        j += length
        length += 1
"""