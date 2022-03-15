class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num += str(i)        #i轉為字串
        num = int(num) + 1       #num轉為int
        return list(str(num))    #轉為字串再轉list
