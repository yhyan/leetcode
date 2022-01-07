/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        while (nums.size() > 0 && nums[nums.size() - 1] == val) {
            nums.pop_back();
        }        
        int i = 0;
        while (i < nums.size()) {
            if (nums[i] == val) {
                nums[i] = nums[nums.size() - 1];
                nums.pop_back();
            } else {
                i += 1;
            }
        }
        return nums.size();
    }
};
// @lc code=end

