class Solution:
    def myAtoi(self, s: str) -> int:
        s, ans = s.strip(), ''  #ignore leading whitespace
        if s == '': return 0
        elif s[0] == '-': 
            ans += '-'
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        for dig in s:
            if dig.isnumeric(): ans += dig
            else: break
        ans = '0' if ans in ['-', '+', ''] else ans #避免ans裡沒有東西
        return max(int(ans), - 2**31) if int(ans)<0 else min(int(ans), 2**31 - 1)
