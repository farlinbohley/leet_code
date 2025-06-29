#include<vector>
#include<unordered_map>
#include<unordered_set>
using std::unordered_set;
using std::unordered_map;
using std::vector;
class Solution{
    public:
        bool uniqueOccurrences(vector<int>& arr){
            unordered_map<int, int> occurrences;
            for (int number : arr) {
                occurrences[number]++;
            }
            
            unordered_set<int> unique_counts;
            for (const auto& pair : occurrences) {
                unique_counts.insert(pair.second);
            }
            
            return occurrences.size() == unique_counts.size();
        }
};