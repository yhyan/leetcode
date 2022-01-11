#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lastRow = [1]
        for r in range(1, rowIndex + 1):
            thisRow = [0 for _ in range(r + 1)]
            for i in range(r + 1):
                if i >= 0 and i <= r - 1:
                    thisRow[i] += lastRow[i]
                if i - 1 >= 0 and i - 1 <= r - 1:
                    thisRow[i] += lastRow[i-1]
            lastRow = thisRow
        return lastRow

# @lc code=end

