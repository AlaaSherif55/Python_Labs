class Solution(object):
    def climbStairs(self, n):
        a = 0
        b = 1
        for i in range(n):
            temp = a
            a = b
            b = temp + b
        return b
    

solution = Solution()
output = solution.climbStairs(2)
print(f"the numbers of ways is: {output}")