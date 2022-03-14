# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 1, n
        while i+1 < j:
            m = (i + j) // 2
            if isBadVersion(m):
                j = m
            else:
                i = m
        
        return i + (isBadVersion(i)!=True)
