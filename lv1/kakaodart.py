# test = '1S2D*3T'
def solution(dartResult):
    answer = 0
    temp = []
    res = []
    num = ''
    VALUES_DICT = {'S': 1, 'D': 2, 'T': 3, '*': 2, '#': -1}
    for i in range(len(dartResult)):
        if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            if num:
                res.append(int(num) ** VALUES_DICT[dartResult[i]])
            temp.append({'*': 0, '#': 0})
            num = ''
        elif dartResult[i] == '*' or dartResult[i] == '#':
            temp[-1][dartResult[i]] += 1
        else:
            num += dartResult[i]
            
    # [1, 8, 3], [{'*': 1, '#': 0}, {'*': 1, '#': 0}, {'*': 0, '#': 0}]
    for i in range(1, len(temp)):
        if temp[i]['*'] == 1:
            temp[i - 1]['*'] += 1
    
    for i in range(len(res)):
        if temp[i]['#'] == 0 and temp[i]['*'] != 0:
            answer += res[i] * VALUES_DICT['*'] * temp[i]['*']
        elif temp[i]['*'] == 0 and temp[i]['#'] != 0:
            answer += res[i] * VALUES_DICT['#'] * temp[i]['#']
        elif temp[i]['*'] != 0 and temp[i]['#'] != 0:
            answer += res[i] * VALUES_DICT['#'] * temp[i]['#'] * VALUES_DICT['*'] * temp[i]['*']
        else:
            answer += res[i]
        
    # print(res, temp)
    return answer


print(solution('1D#2S*3S'))

# 만약 value