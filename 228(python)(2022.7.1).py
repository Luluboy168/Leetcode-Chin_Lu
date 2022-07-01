class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1:
            return nums
        left, right = nums[0], nums[0]
        summary = []
        for i in range(1, len(nums)):
            if (nums[i]-nums[i-1] == 1):
                right = nums[i]
            else:
                if left == right:
                    summary.append("{}".format(left))
                else:
                    summary.append("{}->{}".format(left, right))
                left, right = nums[i], nums[i]
        if left == right:
            summary.append("{}".format(left))
        else:
            summary.append("{}->{}".format(left, right))
            
        return summary
