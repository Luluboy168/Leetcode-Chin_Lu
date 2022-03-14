class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def solve(output, op, cl, ans):
            if op == 0 and cl == 0:
                ans.append(output)
                return
            elif op == 0 and cl != 0:
                solve(output + ')', op, cl -1, ans)
            elif op != 0 and op < cl:
                solve(output + '(', op - 1, cl, ans)
                solve(output + ')', op, cl - 1, ans)
            elif op != 0 and op == cl:
                solve(output + '(', op - 1, cl, ans)
        ans = []
        solve("", n, n, ans)
        return ans
