#include <stdio.h>
#include <vector>
#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        int write_pos = 0;  // Position to write compressed data
        int i = 0;          // Position to read from
        
        while (i < chars.size()) {
            char current_char = chars[i];
            int count = 1;
            
            // Count consecutive occurrences
            while (i + count < chars.size() && chars[i + count] == current_char) {
                count++;
            }
            
            // Write the character
            chars[write_pos++] = current_char;
            
            // Write the count if > 1
            if (count > 1) {
                string count_str = to_string(count);
                for (int j = 0; j < count_str.length(); j++) {
                    chars[write_pos++] = count_str[j];
                }
            }
            
            // Move to next group
            i += count;
        }
        
        return write_pos;
    }
};  

int main(){
    Solution solution;
    
    // Test case 1: ["a","a","b","b","c","c","c"] -> ["a","2","b","2","c","3"]
    vector<char> test1;
    test1.push_back('a');
    test1.push_back('a');
    test1.push_back('b');
    test1.push_back('b');
    test1.push_back('c');
    test1.push_back('c');
    test1.push_back('c');
    
    cout << "Test 1 - Original: ";
    for (int i = 0; i < test1.size(); i++) {
        cout << test1[i] << " ";
    }
    cout << endl;
    
    int result1 = solution.compress(test1);
    cout << "Test 1 - Compressed: ";
    for (int i = 0; i < result1; i++) {
        cout << test1[i] << " ";
    }
    cout << "| Length: " << result1 << endl;
    
    // Test case 2: ["a"] -> ["a"]
    vector<char> test2;
    test2.push_back('a');
    
    cout << "\nTest 2 - Original: ";
    for (int i = 0; i < test2.size(); i++) {
        cout << test2[i] << " ";
    }
    cout << endl;
    
    int result2 = solution.compress(test2);
    cout << "Test 2 - Compressed: ";
    for (int i = 0; i < result2; i++) {
        cout << test2[i] << " ";
    }
    cout << "| Length: " << result2 << endl;
    
    // Test case 3: ["a","b","b","b","b","b","b","b","b","b","b","b","b"] -> ["a","b","1","2"]
    vector<char> test3;
    test3.push_back('a');
    for (int i = 0; i < 12; i++) {
        test3.push_back('b');
    }
    
    cout << "\nTest 3 - Original: ";
    for (int i = 0; i < test3.size(); i++) {
        cout << test3[i] << " ";
    }
    cout << endl;
    
    int result3 = solution.compress(test3);
    cout << "Test 3 - Compressed: ";
    for (int i = 0; i < result3; i++) {
        cout << test3[i] << " ";
    }
    cout << "| Length: " << result3 << endl;
    
    return 0;
} 