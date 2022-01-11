#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        m = [[1]]
        for r in range(1, numRows):
            m.append([0 for i in range(r + 1)])
            for i in range(r + 1):
                if i >= 0 and i <= r - 1:
                    m[r][i] += m[r-1][i]
                if i - 1 >= 0 and i - 1 <= r - 1:
                    m[r][i] += m[r-1][i-1]
        return m

# @lc code=end

