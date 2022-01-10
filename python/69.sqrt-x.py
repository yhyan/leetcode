#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = int((left + right) / 2)
            t0 = mid * mid
            t1 = t0 + 2 * mid + 1
            if t0 <= x and x < t1:
                return int(mid)
            if x < t0:
                right = mid - 1
            if x >= t1:
                left = mid + 1
        raise Exception("can't get here")
            


# @lc code=end

