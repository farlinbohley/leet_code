#include <vector>
using std::vector;
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total = 0;
        for (int i = 0; i < nums.size();i++) {
            total += nums[i];
        }
        for (int i = 0; i < nums.size();i ++) {
            int sum = 0;
            for (int j= 0; j < i; j++) {
                sum += nums[j];
            }
            if (sum == (total -sum - nums[i])) {
                return i;
            }
            else {
                continue;
            }
        }
        return -1;
    }
};