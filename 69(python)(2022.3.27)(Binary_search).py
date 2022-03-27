# 暴力解
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         for i in range(2 ** 17):
#             if (i * i) == x:
#                 return i
#             elif (i *i) < x and ((i+1) * (i+1)) > x:
#                 return i
            
#         return 0

# Binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        ans = -1
        while(low <= high):
            mid = (low + high) // 2
            midSq = mid * mid 
            
            if midSq == x:
                return mid
            elif midSq > x:
                high = mid - 1
            else:
                low = mid + 1
                ans = mid
                
        return ans
