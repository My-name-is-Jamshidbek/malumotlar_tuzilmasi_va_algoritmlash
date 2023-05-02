"""
bsuit
"""
import time
from memory_profiler import memory_usage



def my_function():
    import math

    def count_t(n, m):
        count = 0
        for i in range(n):
            for j in range(m):
                if j + 2 < m and i + 1 < n and (j + 1) % m != 0:
                    # Check for the first T configuration
                    if all(sheet[i][j + k] == 'X' for k in range(3)) and sheet[i + 1][j + 1] == 'X':
                        count += 1
                if i + 2 < n and j + 1 < m:
                    # Check for the second T configuration
                    if all(sheet[i + k][j] == 'X' for k in range(3)) and sheet[i + 1][j + 1] == 'X':
                        count += 1
        return count

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        sheet = [input().strip() for _ in range(n)]
        total_t = count_t(n, m)
        required_t = math.ceil(n * m / 4)
        if total_t >= required_t:
            print("Yes")
        else:
            print("No")


start_time = time.time()
memory_used = memory_usage((my_function, ))
end_time = time.time()

print(f"time: {end_time - start_time}")
print(f"memory: {max(memory_used) - min(memory_used)} MiB")
