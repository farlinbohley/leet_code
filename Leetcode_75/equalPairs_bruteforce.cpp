#include <vector>
#include <iostream>
using std::vector;
class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        vector<vector<int>> changed(grid.size());
        int count = 0;
        //inverting the grid
        for (int i = 0; i < grid.size(); i++) {
            for (const vector<int> vec: grid) {
                changed[i].push_back(vec[i]);
            }
        }
        //trash code
        for(const vector<int> vec1 : grid){
            for (const vector<int> vec2: changed) {
                if (vec1 == vec2) {
                    count++;
                }
            }
        }
        
        return count;
    }
};

int main() {
    Solution solution;
    
    // Test case 1
    vector<vector<int>> grid1 = {{3,2,1},{1,7,6},{2,7,7}};
    int result1 = solution.equalPairs(grid1);
    std::cout << "Test 1: " << result1 << " (expected: 1)" << std::endl;
    
    // Test case 2
    vector<vector<int>> grid2 = {{3,1,2,2},{1,4,4,5},{2,4,2,2},{2,4,2,2}};
    int result2 = solution.equalPairs(grid2);
    std::cout << "Test 2: " << result2 << " (expected: 3)" << std::endl;
    
    return 0;
}