/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 实现 strStr()
 */

// @lc code=start
#include <string>

class Solution {
public:
    int strStr(string haystack, string needle) {
        const char *p = strstr(haystack.c_str(), needle.c_str());
        return (p == NULL) ? -1 : (p - haystack.c_str());
    }
};
// @lc code=end

