from sortedcontainers import SortedDict

# Создайте TreeMap и добавьте 5 ключей (имена) и значений (баллы). Выведите отсортированные данные.

tm: SortedDict[str, int] = SortedDict()

tm['kate'] = 22
tm['semen'] = 25
tm['vasya'] = 30
tm['petr'] = 44
tm['dima'] = 11
tm['vitasik'] = 9

for idx, (k, v) in enumerate(tm.items(), start=1):
    print(f"{idx}. {k}: {v}")

# Найдите минимальный и максимальный ключ в TreeMap.

print(tm.keys()[0])
print(tm.keys()[-1])










