class Solution:
    def average(self, salary: List[int]) -> float:
        maximal = salary[0]
        minimal = salary[0]
        n,s=0,0
        for i in salary:
            if i>maximal:maximal=i
            if i<minimal:minimal=i
            n,s=n+1,s+i
        return (s-maximal-minimal)/(n-2)