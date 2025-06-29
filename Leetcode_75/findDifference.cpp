#include<vector>
#include<unordered_set>
using std::unordered_set;
using std::vector;
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());
        vector<int> distinct_in_nums2;
        vector<int> distinct_in_nums1;
        for (int num : set2) {
            if (set1.count(num) == 0) { // Check if num from set2 is NOT in set1
                distinct_in_nums2.push_back(num);
            }
        }
        for (int num : set1){
            if (set2.count(num) == 0){
                distinct_in_nums1.push_back(num);
            }
        }
        return {distinct_in_nums1, distinct_in_nums2};
    }
};