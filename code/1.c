/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
   int idx1, idx2;
   int *res = (int *)malloc(sizeof(int) * 2);
   for(idx1 = 0; idx1 < numSize; idx1 ++){
       for(idx2 = idx1 + 1; idx2 < numSize; idx2 ++){
            if(nums[idx1] + nums[idx2] == target){
                res[0] = idx1;
                res[1] = idx2;
                return res;
            }
       }
   }
   return NULL;
}
