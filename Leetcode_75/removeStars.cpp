#include <string>
#include <vector>
#include "iostream"
#include <algorithm> // for std::sort
using std::vector;
using std::string;
class Solution {
public:
    /*
    // Alternative stack-based approach
    string removeStars(string s) {
        string result = "";
        for (char c : s) {
            if (c == '*') {
                if (!result.empty()) {
                    result.pop_back();
                }
            } else {
                result.push_back(c);
            }
        }
        return result;
    }
    */
    string removeStars(string s) {
        vector<int> needToBeErased;
        //finding what needs to be erased
        for (int i = 0; i <= s.size() - 1; i++) {
            if ((s[i-1] != '*' && i > 0)) {
                int count = 0;
                int m = i;
                while (s[m] == '*') {
                count++;
                m++;
                }
                for (int j = 0; j <= count - 1; j++) {
                needToBeErased.push_back(i+j);
                needToBeErased.push_back(i-j-1);
                }
            }
            else if(s[0] == '*' && i == 0){
                needToBeErased.push_back(0);
            }
        }
        
        // Sort in descending order
        // rbegin() and rend() are "reverse iterators" that make sort work backwards
        std::sort(needToBeErased.rbegin(), needToBeErased.rend()); 
        // needToBeErased is now {5, 3, 2}

        // Erase from the back
        for (int index : needToBeErased) {
            s.erase(s.begin() + index);
        }
        
        return s;
    }
};

int main() {
    Solution solution;
    
    // Test case 1
    string test1 = "leet**cod*e";
    string result1 = solution.removeStars(test1);
    std::cout << "Input: \"" << test1 << "\"" << std::endl;
    std::cout << "Output: \"" << result1 << "\"" << std::endl;
    std::cout << "Expected: \"lecoe\"" << std::endl;
    std::cout << std::endl;
    
    // Test case 2
    string test2 = "erase*****";
    string result2 = solution.removeStars(test2);
    std::cout << "Input: \"" << test2 << "\"" << std::endl;
    std::cout << "Output: \"" << result2 << "\"" << std::endl;
    std::cout << "Expected: \"\"" << std::endl;
    std::cout << std::endl;
    
    return 0;
}