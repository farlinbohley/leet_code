#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int longestSubarray(vector<int>& arr) {
        int right = 0, left = 0, maxLength = 0, zeros = 0;

        while (right < arr.size()) {
            if (arr[right] == 0) {
                zeros++;
        }
            while (zeros > 1) {
                if (arr[left] == 0) {
                    zeros--;
                }
                left++;
            }
            right ++;
            maxLength = max(maxLength, right - left - 1); // Subtract 1 because we must delete one element
        }
        return maxLength == 0 ? 0 : maxLength; // Handle edge case where all elements are 1
    }
};

// Test function
void runTests() {
    Solution solution;

    // Test case 1: [1,1,0,1] - Expected: 3
    vector<int> test1 = {1, 1, 0, 1};
    int result1 = solution.longestSubarray(test1);
    cout << "Test 1: [1,1,0,1] -> " << result1 << " (Expected: 3)" << endl;

    // Test case 2: [0,1,1,1,0,1,1,0,1] - Expected: 5
    vector<int> test2 = {0, 1, 1, 1, 0, 1, 1, 0, 1};
    int result2 = solution.longestSubarray(test2);
    cout << "Test 2: [0,1,1,1,0,1,1,0,1] -> " << result2 << " (Expected: 5)" << endl;

    // Test case 3: [1,1,1] - Expected: 2 (must delete one element)
    vector<int> test3 = {1, 1, 1};
    int result3 = solution.longestSubarray(test3);
    cout << "Test 3: [1,1,1] -> " << result3 << " (Expected: 2)" << endl;

    // Test case 4: [0,0,0] - Expected: 0
    vector<int> test4 = {0, 0, 0};
    int result4 = solution.longestSubarray(test4);
    cout << "Test 4: [0,0,0] -> " << result4 << " (Expected: 0)" << endl;

    // Test case 5: [1,0,1,1,1,0,0] - Expected: 3
    vector<int> test5 = {1, 0, 1, 1, 1, 0, 0};
    int result5 = solution.longestSubarray(test5);
    cout << "Test 5: [1,0,1,1,1,0,0] -> " << result5 << " (Expected: 3)" << endl;
}

int main() {
    cout << "Running Longest Subarray Tests..." << endl;
    cout << "=================================" << endl;
    runTests();
    cout << "=================================" << endl;
    cout << "Tests completed!" << endl;
    return 0;
}
