#include<vector>
#include<limits>
#include<iostream>
#include<algorithm>
using std::iostream;
class Solution {
public:
    int longestOnes(std::vector<int>& nums, int k) {
        int maxLen = -std::numeric_limits<int>::infinity();
        for(int i = 0; i < nums.size();i++){
            int fliped = 0;
            int curLen = 0;
            int j = i;
            // Expand the window while we can still flip zeros (within k limit)
            while(fliped <= k && j < nums.size()) {
                if(nums[j] == 0){
                    fliped++;
                    j++;
                    curLen++;
                }
                else if(nums[j] == 1){
                    j++;
                    curLen++;
                }
            }
            if(fliped > k){
                curLen--;
            }
            maxLen = std::max(curLen, maxLen);
        }
        return maxLen;
    }
};

int main() {
    Solution sol;
    
    // Test case 1
    std::vector<int> nums1 = {1,1,1,0,0,0,1,1,1,1,0};
    int k1 = 2;
    int result1 = sol.longestOnes(nums1, k1);
    std::cout << "Test 1: Array with k=" << k1 << " -> Longest ones: " << result1 << std::endl;
    
    // Test case 2
    std::vector<int> nums2 = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
    int k2 = 3;
    int result2 = sol.longestOnes(nums2, k2);
    std::cout << "Test 2: Array with k=" << k2 << " -> Longest ones: " << result2 << std::endl;
    
    // Test case 3
    std::vector<int> nums3 = {0,0,0,0};
    int k3 = 2;
    int result3 = sol.longestOnes(nums3, k3);
    std::cout << "Test 3: Array with k=" << k3 << " -> Longest ones: " << result3 << std::endl;
    
    return 0;
}