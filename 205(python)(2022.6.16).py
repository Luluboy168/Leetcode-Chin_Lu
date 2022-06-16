class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        wordmap = {}
        for i in range(len(s)):
            if s[i] not in wordmap.keys():
                if t[i] in wordmap.values():
                    return False
                wordmap[s[i]] = t[i]
            else:
                if t[i] != wordmap[s[i]]:
                    return False
                
        return True
