/*
 * @lc app=leetcode.cn id=66 lang=cpp
 *
 * [66] 加一
 */

// @lc code=start
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> res(digits.rbegin(), digits.rend());
        res[0] += 1;
        int carry = res[0] / 10;
        res[0] %= 10;
        int i = 1;
        while (i < res.size() && carry > 0) {
            res[i] += carry;
            if (res[i] >= 10) {
                carry = res[i] / 10;
                res[i] %= 10;
            } else {
                carry = 0;
            }
            i += 1;
        }
        if (i >= res.size() && carry > 0) {
            res.push_back(carry);
        }
        return vector<int>(res.rbegin(), res.rend());
    }
};
// @lc code=end

