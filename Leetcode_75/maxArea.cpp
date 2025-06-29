#include <vector>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int start = 0;
        int end = height.size() - 1;
        while(start < end){
            int currentArea = min(height[start], height[end])*(end - start);
            maxArea = max(currentArea, maxArea);
            if (height[start] <= height[end]){
                start ++;
            }
            else{
                end--;
            }
        }
        return maxArea;
    }
};
        