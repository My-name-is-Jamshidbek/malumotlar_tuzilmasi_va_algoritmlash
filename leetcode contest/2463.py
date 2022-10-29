class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        while robot:
            min_z=0
            min_b=0
            m = abs(factory[0][0]-robot[0])
            i=1
            for i1 in robot:
                if factory[i]:pass