class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for num in nums:
            if nums.count(num) == 1:
                return num
              
# ##solution 2
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
        
#         d = Counter(nums)
#         return sorted(d, key=d.get)[0]
