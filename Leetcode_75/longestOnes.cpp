#include<vector>
#include<algorithm>
#include<iostream>
using std::iostream;
using std::vector;
class Solution{
private:
    /* data */
public:
    int longestOnes (std::vector<int>& nums, int k){
        int maxLen = 0;
        int left = 0;
        int right = 0;
        int zeros = 0;
        while (right < nums.size()){
            if (nums[right] == 0){
                zeros ++;
            }
            while(zeros > k){
                if(nums[left] == 0){
                    zeros--;
                }
                left ++;
            }
            maxLen = std::max(maxLen, right - left + 1);
            right++;
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