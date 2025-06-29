#include<vector>
#include<unordered_map>
using std::unordered_map;
using std::vector;
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> freq_map;
        int operations = 0;

        for (int current_num : nums) {
            int complement = k - current_num;
            if (freq_map[complement] > 0) {
                // A complement is available in our map.
                // We found a pair.
                operations++;
                // Decrement the count of the complement to "use it up".
                freq_map[complement]--;
            } else {
                // No complement was available.
                // Add the current number to the map, making it available for future numbers.
                freq_map[current_num]++;
            }
        }

        return operations;
    }
};