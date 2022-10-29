class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        qoldiqlar = {}
        ind=0
        for i in numbers:
            ind+=1
            qoldiq = target-i
            kami = target-qoldiq
            if kami in qoldiqlar:return [qoldiqlar[kami],ind]
            else:qoldiqlar[qoldiq]=ind
a = Solution()
print(a.twoSum(numbers = [-1,0], target = -1))