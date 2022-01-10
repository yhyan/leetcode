#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:

    ZERO = ord('0')

    def addDigit(self, ia, ib, carry_):
        
        ia = ord(ia) - self.ZERO
        ib = ord(ib) - self.ZERO
        carry_ = ord(carry_) - self.ZERO
        r = ia + ib + carry_
        if r == 3:
            return '1', '1'
        elif r == 2:
            return '0', '1'
        elif r == 1:
            return '1', '0'
        elif r == 0:
            return '0', '0'
        else:
            raise Exception("input ERROR") 

    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b)) + 1
        ra = a[::-1] + (n - len(a)) * '0'
        rb = b[::-1] + (n - len(b)) * '0'
        c = ['0' for i in range(n)]
        carry_ = '0'
        for i in range(n):
            c[i], carry_ = self.addDigit(ra[i], rb[i], carry_)
        if c[-1] == '0' and n > 1:
            c[-1] = ''
        return ''.join(c[::-1])

# @lc code=end

