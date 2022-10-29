def rob( nums: list[int]) -> int:
    rob1,rob2 = 0,0
    for n in nums:
        temp = max(rob1+n, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
nums = []
n = 0
for _ in range(int(input().split()[0])):
    nums += list(map(int,input().split()))
    n += rob(nums=nums)
