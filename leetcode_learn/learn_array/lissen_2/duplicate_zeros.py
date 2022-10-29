class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i,l=0,len(arr)
        while(i<l):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i,0)
                i+=1
            i+=1
arr = [1,0,2,3,0,4,5,0]
a = Solution()
print(a.duplicateZeros(arr = arr))
print(arr)