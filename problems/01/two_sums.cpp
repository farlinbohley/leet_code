#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_to_index;  // Hash map to store number and its index
        
        for (int index = 0; index < nums.size(); index++) {
            int num = nums[index];
            int complement = target - num;
            
            // Check if complement exists in hash map
            if (num_to_index.find(complement) != num_to_index.end()) {
                // Found the pair! Return indices
                return {num_to_index[complement], index};
            }
            
            // Store current number and its index
            num_to_index[num] = index;
        }
        
        // No solution found
        return {};
    }
};

// Example usage and testing
int main() {
    Solution solution;
    
    // Test case 1
    vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    vector<int> result1 = solution.twoSum(nums1, target1);
    cout << "Test 1 - nums: [2, 7, 11, 15], target: 9" << endl;
    cout << "Result: [" << result1[0] << ", " << result1[1] << "]" << endl;
    
    // Test case 2
    vector<int> nums2 = {3, 2, 4};
    int target2 = 6;
    vector<int> result2 = solution.twoSum(nums2, target2);
    cout << "Test 2 - nums: [3, 2, 4], target: 6" << endl;
    cout << "Result: [" << result2[0] << ", " << result2[1] << "]" << endl;
    
    // Test case 3
    vector<int> nums3 = {3, 3};
    int target3 = 6;
    vector<int> result3 = solution.twoSum(nums3, target3);
    cout << "Test 3 - nums: [3, 3], target: 6" << endl;
    cout << "Result: [" << result3[0] << ", " << result3[1] << "]" << endl;
    
    return 0;
}
