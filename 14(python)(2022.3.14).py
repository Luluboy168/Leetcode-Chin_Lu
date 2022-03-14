class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        same = 1
        mini = len(strs[0])
        if len(strs) == 1:
            return strs[0]
        
        for i in range(len(strs)):
            if strs[i] == "":
                return ""
            if len(strs[i]) < mini:
                mini = len(strs[i])
        
                
        for i, c in enumerate(strs[0]):
            if i >= mini: 
                return common
            for j in range(len(strs)):
                if strs[j][i] != c:
                    same = 0
                
            if same:
                common = common + c
            else:
                return common
        return common
