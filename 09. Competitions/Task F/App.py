# ГДЕ-ТО ОШИБКА
# Presentation Error

from collections import Counter


def get_ingreds(dish, recepts):
    ingreds = dict()
    for item in recepts[dish]:
        # если это  ингридиент а не блюдо
        if item[0] not in recepts:
            if item[0] in ingreds:
                ingreds[item[0]] += item[1]
            else:
                ingreds[item[0]] = item[1]
        # если это блюдо
        else:
            sub_ingreds = get_ingreds(item[0], recepts)
            for sub_ingred in sub_ingreds.items():
                ingreds[sub_ingred[0]] = item[1]*sub_ingred[1]
    return ingreds


x = int(input())
result = []

for test in range(x):
    res = []

    N, K, F = list(map(int, input().split()))
    menu = dict()
    for i in range(N):
        name, count = input().split()
        count = int(count)
        menu[name] = count

    recepts = dict()
    for i in range(K):
        name, count = input().split()
        count = int(count)
        ingred = []
        for j in range(count):
            name_1, count_1 = input().split()
            count_1 = int(count_1)
            ingred.append((name_1, count_1))
        recepts[name] = ingred

    holod = dict()
    for i in range(F):
        name, count = input().split()
        count = int(count)
        holod[name] = count
    # print(menu)
    # print(recepts)
    # print(holod)

    need_ingred = dict()
    for dish, count in menu.items():
        # print(dish, get_ingreds(dish, recepts))
        ingred_for_dish = get_ingreds(dish, recepts)
        for key in ingred_for_dish:
            ingred_for_dish[key] *= count

        need_ingred = dict(Counter(need_ingred) + Counter(ingred_for_dish))
    # print(need_ingred)
    to_buy = dict(Counter(need_ingred) - Counter(holod))
    # print(to_buy)
    for item in to_buy.items():
        res.append((item[0], item[1]))
    res.sort(key=lambda x: x[0])
    # print(res)

    result.append(res)

for res in result:
    for e in res:
        print(*e)
