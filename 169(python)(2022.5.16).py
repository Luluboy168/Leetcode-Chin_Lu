class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = Counter(nums)
        return sorted(d, key=d.get)[-1]
