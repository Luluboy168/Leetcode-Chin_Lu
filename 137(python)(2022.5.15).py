class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #set 會去掉重複元素而且排序
        return int((3 * sum(set(nums)) - sum(nums)) * 0.5)
    
    
# ##solution 2
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
        
#         for num in nums:
#             if nums.count(num) == 1:
#                 return num
              
# ##solution 3
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
        
#         d = Counter(nums)
#         return sorted(d, key=d.get)[0]
