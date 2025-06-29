#include<string>
#include<unordered_map>
#include<algorithm>
#include<vector>
#include<unordered_set>

using std::string;
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if(word1.size() != word2.size()){
            return false;
        }
        std::unordered_set <char> s1, s2;
        std::unordered_map <char, int> freq1, freq2;
        std::vector <int> v_freq1, v_freq2;
        for (char c : word1){
            s1.insert(c);
            freq1[c] ++;
        }
        for (char c: word2){
            s2.insert(c);
            freq2[c] ++;
        }
        for (const auto& pair : freq1){
            v_freq1.push_back(pair.second);
        }
        for (const auto& pair : freq2){
            v_freq2.push_back(pair.second);
        }
        std::sort(v_freq1.begin(), v_freq1.end());
        std::sort(v_freq2.begin(), v_freq2.end());
        if (s1 != s2){
            return false;
        }
        if(v_freq1 == v_freq2){
            return true;
        }
        return false;
    }
        
};