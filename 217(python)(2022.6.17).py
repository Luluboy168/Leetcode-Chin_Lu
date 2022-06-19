class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #dictionary solution
        
        hashTable = {}
        
        for num in nums:
            strkey = str(num)
            if strkey not in hashTable:
                hashTable[strkey] = num
            else:
                return True
            
        return False
