"""
스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
스킬 순서와 스킬트리는 문자열로 표기합니다.
예를 들어, C → B → D 라면 CBD로 표기합니다
선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
skill_trees는 길이 1 이상 20 이하인 배열입니다.
skill_trees의 원소는 스킬을 나타내는 문자열입니다.
skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.
"""

# stack으로 구현하는것이 좋겠다.
def solution(skill, skill_trees):
    flag = False
    answer = 0
    for c in skill_trees:
        stack = []
        for i in range(len(c)):
            if c[i] in skill:
                stack.append(c[i])
        if not stack:
            flag = True
        else:
            for i in range(len(stack)):
                if stack[i] != skill[i]:
                    flag = False
                    break
                else:
                    flag = True
        if flag:
            answer += 1

    return answer


print(solution("CBD", ["AEF", " ZJW"]))
