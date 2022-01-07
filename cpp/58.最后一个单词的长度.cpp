/*
 * @lc app=leetcode.cn id=58 lang=cpp
 *
 * [58] 最后一个单词的长度
 */

// @lc code=start
class Solution {
public:
    int lengthOfLastWord(string s) {
        int rt = s.size() - 1;
        while (s[rt] == ' ') {
            rt--;
        }
        int lt = rt;
        while (lt >= 0 && s[lt] != ' ') {
            lt--;
        }
        return rt - lt;
    }
};
// @lc code=end

