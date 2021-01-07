"""
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환
재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환
절차적인 방법으로 단계적으로 풀어나가기



# print("info_bool:", info_bool)

# 조건으로 음악 반환
# 1. 조건을 만족하는 노래가 하나일 때, 그것을 반환
# 2. 여러개가 조건을 만족할 때, 길이가 더 긴것을 반환
# 3. 길이가 같을 경우, 먼저 재생된 노래를 반환 (길이가 더 클경우에만 하면 됨)
"""


def solution(m, musicinfos):
    new_musicinfos = []
    for i in range(len(musicinfos)):
        temp = musicinfos[i].split(",")
        new_musicinfos.extend(temp)
    answer = solve(m, new_musicinfos)
    return answer


def solve(m, musicinfos):
    answer = "(None)"  # answer는 매칭된 노래 제목
    info_arr = []

    # 새로운 악보 배열 만들기
    for i in range(0, len(musicinfos), 4):
        hour = (
            (int(musicinfos[i + 1][:2]) - int(musicinfos[i + 0][:2])) * 60
            if int(musicinfos[i + 1][:2]) >= int(musicinfos[i][:2])
            else (24 + int(musicinfos[i + 1][:2]) - int(musicinfos[i + 0][:2])) * 60
        )
        minutes = int(musicinfos[i + 1][3:]) - int(musicinfos[i + 0][3:])

        # "#"은 앞 글자와 붙여 한글자로 처리가 필요
        new_string = ""
        j = 0
        k = 0
        while j < (hour + minutes):
            new_string += musicinfos[i + 3][k % len(musicinfos[i + 3])]
            if musicinfos[i + 3][k % len(musicinfos[i + 3])] != "#":
                j += 1
            k += 1
        # 뒤에 "#"이 있을지도 모르니 필요
        if musicinfos[i + 3][k % len(musicinfos[i + 3])] == "#":
            new_string += musicinfos[i + 3][k % len(musicinfos[i + 3])]
        info_arr.append(new_string)

    print("info_arr:", info_arr)

    # 악보 배열 비교. "#" 처리를 어떻게 하는지가 중요
    info_bool = [-1] * len(info_arr)
    for i in range(len(info_arr)):
        idx = info_arr[i].find(m)
        while idx != -1:
            if (
                info_arr[i][idx + len(m) - 1] == "C"
                or info_arr[i][idx + len(m) - 1] == "D"
                or info_arr[i][idx + len(m) - 1] == "F"
                or info_arr[i][idx + len(m) - 1] == "G"
                or info_arr[i][idx + len(m) - 1] == "A"
            ):
                if (
                    idx + len(m) < len(info_arr[i]) and info_arr[i][idx + len(m)] == "#"
                ):  # index error
                    idx = info_arr[i].find(m, idx + len(m))
                else:
                    idx = info_arr[i].find(m, idx)
                    info_bool[i] = idx
                    break
            else:
                info_bool[i] = idx
                break

    idx_ = -1
    length = -1
    for i in range(len(info_bool)):
        if info_bool[i] != -1:
            temp_length = get_length(info_arr[i])
            if temp_length > length:
                idx_ = i
                length = temp_length
    if idx_ != -1:
        answer = musicinfos[idx_ * 4 + 2]

    return answer


def get_length(string):
    counts = 0
    for i in range(len(string)):
        if string[i] != "#":
            counts += 1
    return counts


"""
m = "ABCDEFG"
musicinfos = [
    "12:00",
    "12:14",
    "HELLO",
    "CDEFGAB",
    "13:00",
    "13:05",
    "WORLD",
    "ABCDEF",
]  # [0]: 시작시간, [1]: 끝난시간, [2]: 노래 제목, [3]: 악보

m = "CC#BCC#BCC#BCC#B"
musicinfos = [
    "03:00",
    "03:30",
    "FOO",
    "CC#B",
    "04:00",
    "04:08",
    "BAR",
    "CC#BCC#BCC#B",
]
"""

m = "ABC"
# musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "23:55,00:00,WORLD,ABCDEF"]
musicinfos = ["12:00,12:09,HELLO,ABC#ABC#ABC"]
print(solution(m, musicinfos))
