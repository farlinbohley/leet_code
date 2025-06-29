#include <vector>
using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zero_count = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == 0){
                nums.erase(nums.begin() + i);
                zero_count ++;
                i--;
            }
        }
        for (int i = 0; i < zero_count; i++){
            nums.push_back(0);
        }
    }
};