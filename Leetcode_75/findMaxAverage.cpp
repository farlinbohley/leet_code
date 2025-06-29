#include <vector>
#include <algorithm>
#include <iostream>
using std::vector;

class Solution {
    public:
    float findMaxAverage(vector<int>& nums, int k) {
        float sum = 0;
        float currentAverage = 0;
        float maxAverage = 0;
        for(int i = 0; i < k; i++){
            sum += nums[i];
            currentAverage = sum/k;
        }
        for(int i = 0; i < nums.size() - k; i++){
            maxAverage = std::max(currentAverage, maxAverage);
            sum = sum - nums[i] + nums[i + k];
            currentAverage = sum/k;
        }
        maxAverage = std::max(currentAverage, maxAverage);
        return maxAverage;
    }
};

int main() {
    std::vector<int> nums = {1,12,-5,-6,50,3};
    int k = 4;
    Solution sol;
    float result = sol.findMaxAverage(nums, k);
    std::cout << "Maximum average of subarray of length " << k << " is: " << result << std::endl;
    return 0;
}