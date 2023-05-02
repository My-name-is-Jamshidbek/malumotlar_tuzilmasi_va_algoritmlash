def is_beautiful(num):
    digits = set(str(num))
    return len(digits) == 1
def count_beautiful_numbers(l, r):
    if str(l)[0] != str(r)[-1]:
        return 0
    count = (r - l) // 10 + 1
    return count

l, r = map(int, input().split())
print(count_beautiful_numbers(l, r))

# numb = 152
# print(str(numb)[::-1])

# l, r = map(int, input().split())
# print(cou/nt_beautiful_numbers(l, r))
