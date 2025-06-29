#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int isSubsequence(string s, string t) {
        int count = 0;
        for(int i = 0; i < t.size(); i++){
            if (count < s.size() && s[count] == t[i]){
                count++;
            }
        }
        return count == s.size();
    }
};


// Test function
int main() {
    Solution solution;
    
    // Test cases
    string s1 = "abc", t1 = "aebdc";
    cout << "Test 1: " << (solution.isSubsequence(s1, t1) ? "true" : "false") << endl;
   
    
    string s2 = "acb", t2 = "ahbgdc";
    //cout << solution.isSubsequence(s2, t2);
    cout << "Test 2: " << (solution.isSubsequence(s2, t2) ? "true" : "false") << endl;
    
    return 0;
}