#include<string>
#include<vector>
#include<algorithm>
#include<limits>
#include<iostream>
using std::string;
using std::vector;
class Solution {
public:
    bool isVowel(char s){
        vector vowels = {'a', 'e', 'i', 'o', 'u'};
        if(std::find(vowels.begin(), vowels.end(), s) != vowels.end()){
            return true;
        }
        else{
            return false;
        }
    }
    int maxVowels(string s, int k) {
        int max_vowels = -std::numeric_limits<int>::infinity();
        int current_vowels = 0;
        for (int i = 0; i < k; i++){
            if(isVowel(s[i])){
                current_vowels ++;
            }
        }
        max_vowels = std::max(max_vowels, current_vowels);
        for (int i = 1; i <= s.size() - k; i++){
            if(isVowel(s[i-1])){
                current_vowels--;
            }
            if(isVowel(s[i+k-1])){
                current_vowels++;
            }
            max_vowels = std::max(max_vowels, current_vowels);
        }
        return max_vowels;
    }
};

int main() {
    Solution sol;
    
    // Test case 1
    string s1 = "abciiidef";
    int k1 = 3;
    int result1 = sol.maxVowels(s1, k1);
    std::cout << "Test 1: String \"" << s1 << "\" with k=" << k1 << " -> Max vowels: " << result1 << std::endl;
    
    // Test case 2
    string s2 = "aeiou";
    int k2 = 2;
    int result2 = sol.maxVowels(s2, k2);
    std::cout << "Test 2: String \"" << s2 << "\" with k=" << k2 << " -> Max vowels: " << result2 << std::endl;
    
    // Test case 3
    string s3 = "leetcode";
    int k3 = 3;
    int result3 = sol.maxVowels(s3, k3);
    std::cout << "Test 3: String \"" << s3 << "\" with k=" << k3 << " -> Max vowels: " << result3 << std::endl;
    
    return 0;
}