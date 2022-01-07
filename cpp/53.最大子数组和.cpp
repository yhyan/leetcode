/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子数组和
 */

// @lc code=start

#include <algorithm>

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currentMax = nums[0], resMax = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (currentMax <= 0) {
                currentMax = nums[i];
            } else {
                currentMax += nums[i];
            }
            resMax = std::max(resMax, currentMax);
        }
        return resMax;
    }
};
// @lc code=end

