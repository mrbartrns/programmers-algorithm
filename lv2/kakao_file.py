"""
파일을 정해진 규칙대로 정렬하기
"""


def solution(files):
    files_arr = []
    for i in range(len(files)):
        is_number = False
        files_arr.append(["", "", ""])
        for j in range(len(files[i])):
            if (ord(files[i][j]) < 48 or ord(files[i][j]) > 57) and (not is_number):
                if ord(files[i][j]) >= ord("A") and ord(files[i][j]) <= ord("Z"):
                    files_arr[i][0] += files[i][j].lower()
                else:
                    files_arr[i][0] += files[i][j]
            elif ord(files[i][j]) >= 48 and ord(files[i][j]) <= 57:
                is_number = True
                files_arr[i][1] += files[i][j]
            elif (ord(files[i][j]) < 48 or ord(files[i][j]) > 57) and (is_number):
                break
        temp = files_arr[i][1]
        files_arr[i][1] = int(temp)
        if j < len(files[i]) - 1:
            files_arr[i][2] = files[i][j:]
        else:
            files_arr[i][2] = ""
        files_arr[i].append(files[i])
    files_arr.sort(key=lambda x: (x[0], x[1]))
    answer = [x[3] for x in files_arr]
    return answer


files_name = [
    "F-5 Freedom Fighter",
    "B-50 Superfortress",
    "A-10 Thunderbolt II",
    "F-14 Tomcat",
]

print(solution(files_name))