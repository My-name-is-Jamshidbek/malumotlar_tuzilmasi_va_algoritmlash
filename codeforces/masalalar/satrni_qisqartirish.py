for _ in range(int(input())):m = input();print(str(m[0] + str(len(m) - 2) + m[-1])) if len(m)>10 else print(m)