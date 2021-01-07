def solution(record):
    answer = []
    user_nickname = {}
    new_record = []
    # record를 쪼개기
    for i in range(len(record)):
        new_record.append(record[i].split(" "))
    for i in range(len(new_record)):
        if new_record[i][0] == "Enter":
            user_nickname[new_record[i][1]] = new_record[i][2]
        elif new_record[i][0] == "Change":
            user_nickname[new_record[i][1]] = new_record[i][2]

    for i in range(len(new_record)):
        temp = ""
        temp += user_nickname[new_record[i][1]]
        if new_record[i][0] == "Enter":
            temp += "님이 들어왔습니다."
            answer.append(temp)
        elif new_record[i][0] == "Leave":
            temp += "님이 나갔습니다."
            answer.append(temp)

    return answer


test = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]
print(solution(test))