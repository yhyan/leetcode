#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        ret = 0
        neg = lambda i: i + 1 < len(s) and self.d[s[i]] < self.d[s[i+1]]
        for i in range(len(s) - 1, -1, -1):
            ret += self.d[s[i]] * (-1 if neg(i) else 1)
        return ret

# @lc code=end

