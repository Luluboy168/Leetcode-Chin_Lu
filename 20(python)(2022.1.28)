class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = {'(', '[', '{'}
        stake = []
        for p in s:
            if p in left:
                stake.append(p)
            elif p == ')':
                if stake and stake[-1] == '(':
                    stake.pop()
                else:
                    return False
            elif p == ']':
                if stake and stake[-1] == '[':
                    stake.pop()
                else:
                    return False
            elif p == '}':
                if stake and stake[-1] == '{':
                    stake.pop()
                else:
                    return False
        return not len(stake)
