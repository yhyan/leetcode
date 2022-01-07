/*
 * @lc app=leetcode.cn id=35 lang=cpp
 *
 * [35] 搜索插入位置
 */

// @lc code=start
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                if (mid + 1 < nums.size()) {
                    left = mid + 1;
                } else {
                    return mid + 1;
                }
            } else {
                if ( mid - 1 >= 0) {
                    right = mid - 1;
                } else {
                    return 0;
                }
            }            
        }
        return left;
    }
};
// @lc code=end

