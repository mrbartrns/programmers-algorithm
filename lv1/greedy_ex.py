def solve(value, coin):
    a = []
    for i in coin:
        a.append([value - i, i])
    res = a[0]
    for i in a:
        if res[0] > i[0] and i[0] > 0:
            res = i
    return res

coin = [1, 50, 100]
value = [362, 0]
dic = {}
for i in coin:
    dic[i] = 0

while True:
    value = solve(value[0], coin)
    if value[0] < 0:
        break
    else:
        dic[value[1]] += 1

print(dic)