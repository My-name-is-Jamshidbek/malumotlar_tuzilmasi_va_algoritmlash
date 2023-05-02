"""
[
(2019, 2025),
(2020, 2023),
.
.
.
.
]

list ichida 1millon data (bitth_date, death_date)

qaysi yilda kup inson trik bulgan
"""
# _list = [
#     [124,356],
#     [248,2896],
#     [127,258],
#     [250,251],
#     [251,252],
#     [251,252]
# ]
import random
import time
from memory_profiler import memory_usage
from collections import Counter

def random_number(n, m):
    return random.randint(n, m)
data = []

f = 0
for massiv_uzunligi in range(5,6):
    f+=1
    print("Test: ",f)
    for _ in range(10**massiv_uzunligi):
        n = 1000
        m = 3000
        r1 = random_number(n, m)
        r2 = random_number(r1 - 1, m)
        data.append([r1, r2])


        def mf(data=data) -> None:
            _new_list = list(map(lambda l: [l[0], 1], data)) + list(map(lambda l: [l[1], 0], data))

            _new_list = sorted(_new_list, key=lambda x: list(x))

            _year, _people, m_people = 0, 0, -1

            for i in _new_list:
                if i[1]:
                    _people += 1
                    if _people > m_people:m_people, _year = _people, i[0]
                else:
                    _people -= 1

            print("Natija:")
            print(f"Maksimal oddam: {m_people}")
            print(f"Maksimal odam yashashni boshlagan yil: {_year}")




    # start_time = time.time()
    # memory_used = memory_usage((mf, ))
    # end_time = time.time()
    #
    # print(f"Author: Jamshidbek\nMassiv uzunligi: 10**{massiv_uzunligi}")
    # print(f"time: {end_time - start_time} sec")
    # print(f"memory: {max(memory_used) - min(memory_used)} MiB")

    def zf(data: list) -> None:
        """
        :param data:
        :return:
        """
        yil = []
        for item in data:
            yil.extend(range(item[0], item[1] + 1))

        max_yil = Counter(yil).most_common(1)[0][0]
        print(max_yil)

    start_time = time.time()
    memory_used = memory_usage((zf,(data,)))
    end_time = time.time()

    print(f"Ziyodulla:\nMassiv uzunligi:{massiv_uzunligi}")
    print(f"time: {end_time - start_time} sec")
    print(f"memory: {max(memory_used) - min(memory_used)} MiB")
# """
# [
# (2019, 2025),
# (2020, 2023),
# .
# .
# .
# .
# ]
#
# list ichida 1millon data (bitth_date, death_date)
#
# qaysi yilda kup inson trik bulgan
# """
# import random
# import time
# from memory_profiler import memory_usage
# from collections import Counter
#
# massiv_uzunligi = 2
# def mf(_list):
#     """
#     :param _list:
#     :return:
#     """
#     print(_list)
#
# def zf(data: list) -> None:
#     """
#     :param data:
#     :return:
#     """
#     yil = []
#     for item in data:
#         yil.extend(range(item[0], item[1] + 1))
#
#     max_yil = Counter(yil).most_common(1)[0][0]
#     print(max_yil)
#
# def random_number(n, m):
#     return random.randint(n, m)
# _list = []
# #
# # for _ in range(10**massiv_uzunligi):
# #     n = 1000
# #     m = 3000
# #     r1 = random_number(n, m)
# #     r2 = random_number(r1 - 1, m)
# #     _list.append((r1, r2))
# #
#
# start_time = time.time()
# memory_used = memory_usage((zf,(_list,)))
# end_time = time.time()
#
# print(f"Ziyodulla:\nMassiv uzunligi:{massiv_uzunligi}")
# print(f"time: {end_time - start_time} sec")
# print(f"memory: {max(memory_used) - min(memory_used)} MiB")
#
# # time.sleep(20)
# _list = [(1281, 1491), (1460, 1462), (1491, 2885), (2153, 2323), (2311, 2810), (1368, 1702), (2230, 2902), (2413, 2775), (2657, 2886), (2907, 2971), (2209, 2559), (2249, 2748), (1734, 1805), (1585, 1639), (1416, 1996), (2290, 2432), (1963, 2571), (1521, 2283), (1958, 2626), (2762, 2845), (2774, 2801), (2645, 2663), (2871, 2921), (1533, 2759), (1202, 2316), (2437, 2939), (2675, 2721), (1762, 2443), (1034, 2564), (1407, 2243), (2924, 2973), (1523, 1608), (1838, 2436), (1139, 2455), (1087, 2727), (1272, 1717), (2552, 2955), (1391, 2453), (2450, 2797), (2876, 2893), (2695, 2882), (2373, 2416), (1429, 2166), (2487, 2736), (1006, 1047), (1266, 2060), (1568, 2533), (1784, 2089), (2998, 2997), (2382, 2779), (1145, 1974), (2727, 2791), (2474, 2698), (2123, 2546), (2566, 2961), (2914, 2962), (1232, 2542), (1890, 2166), (2020, 2653), (1389, 1670), (2756, 2791), (1545, 2712), (2658, 2987), (2518, 2966), (2533, 2857), (2327, 2529), (2938, 2947), (1592, 2838), (1097, 1266), (1007, 1578), (2719, 2799), (2487, 2765), (1821, 2754), (2273, 2731), (2128, 2200), (1328, 2838), (1862, 2179), (2038, 2260), (1614, 2663), (2187, 2509), (1068, 1090), (1285, 1680), (1153, 2320), (2650, 2845), (2718, 2779), (1831, 2543), (2906, 2954), (2297, 2789), (2341, 2458), (1282, 1887), (2754, 2981), (2452, 2477), (2137, 2632), (2884, 2998), (2588, 2750), (1804, 2250), (1511, 1929), (1922, 2447), (2677, 2777), (2020, 2342)]
#
#
# for _ in range(10**massiv_uzunligi):
#     n = 1000
#     m = 3000
#     r1 = random_number(n, m)
#     r2 = random_number(r1 - 1, m)
#     _list.append((r1, r2))
#
# print(_list)
# start_time = time.time()
# memory_used = memory_usage((mf,(list(_list))))
# end_time = time.time()
# #
# print(f"My:\nMassiv uzunligi:{massiv_uzunligi}")
# print(f"time: {end_time - start_time} sec")
# print(f"memory: {max(memory_used) - min(memory_used)} MiB")
