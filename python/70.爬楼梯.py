#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a = [3, 1, 2]
        if n <= 3:
            return a[n % 3]
        for i in range(4, n+1):
            a[i % 3] = a [(i - 1) % 3] + a[(i-2) % 3]
        return a[n % 3]

# @lc code=end

