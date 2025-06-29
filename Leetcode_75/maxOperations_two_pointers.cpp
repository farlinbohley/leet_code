#include <vector>
#include <algorithm> // Required for std::sort

class Solution {
public:
    int maxOperations(std::vector<int>& nums, int k) {
        // First, sort the array. This is essential for the two-pointer approach.
        std::sort(nums.begin(), nums.end());

        int left = 0;
        int right = nums.size() - 1;
        int operations = 0;

        // Loop until the two pointers meet or cross each other.
        while (left < right) {
            int current_sum = nums[left] + nums[right];

            if (current_sum == k) {
                // Found a valid pair.
                operations++;
                left++;  // Move to the next potential element from the left.
                right--; // Move to the next potential element from the right.
            } else if (current_sum < k) {
                // The sum is too small, so we need a larger number.
                // The only way to get a larger sum is to move the left pointer.
                left++;
            } else { // current_sum > k
                // The sum is too large, so we need a smaller number.
                // The only way to get a smaller sum is to move the right pointer.
                right--;
            }
        }

        return operations;
    }
}; 