#include <vector>
#include <algorithm>
using std::vector;
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> altitude = {0};
        for (int i = 0; i < gain.size(); i++) {
            altitude.push_back((gain[i] + altitude[i]));
        }
        return *std::max_element(altitude.begin(), altitude.end());
    }
};



















