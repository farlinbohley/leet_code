#include <vector>
using std::vector;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;
        for (int current_asteroid : asteroids) {
            // A collision happens when a right-moving asteroid (positive) on the stack
            // meets a left-moving one (negative) that we are currently processing.
            bool destroyed = false;
            while (!stack.empty() && current_asteroid < 0 && stack.back() > 0) {
                // The one on the stack is smaller than the current one. It gets destroyed.
                if (stack.back() < -current_asteroid) {
                    stack.pop_back();
                    continue; // The current asteroid continues to the next on the stack.
                } 
                // Both are the same size. Both are destroyed.
                else if (stack.back() == -current_asteroid) {
                    stack.pop_back();
                    destroyed = true;
                }
                // The one on the stack is bigger. The current one is destroyed.
                else { // stack.back() > -current_asteroid
                    destroyed = true;
                }
                break; // Collision is resolved.
            }

            if (!destroyed) {
                stack.push_back(current_asteroid);
            }
        }
        return stack;
    }
};

#include <iostream>

int main() {
    Solution solution;
    
    // Test case 1
    vector<int> asteroids1 = {5, 10, -5};
    vector<int> result1 = solution.asteroidCollision(asteroids1);
    std::cout << "Test 1 - Input: [5,10,-5], Output: [";
    for (int i = 0; i < result1.size(); i++) {
        std::cout << result1[i];
        if (i < result1.size() - 1) std::cout << ",";
    }
    std::cout << "]" << std::endl;
    
    // Test case 2
    vector<int> asteroids2 = {8, -8};
    vector<int> result2 = solution.asteroidCollision(asteroids2);
    std::cout << "Test 2 - Input: [8,-8], Output: [";
    for (int i = 0; i < result2.size(); i++) {
        std::cout << result2[i];
        if (i < result2.size() - 1) std::cout << ",";
    }
    std::cout << "]" << std::endl;
    
    // Test case 3
    vector<int> asteroids3 = {10, 2, -5};
    vector<int> result3 = solution.asteroidCollision(asteroids3);
    std::cout << "Test 3 - Input: [10,2,-5], Output: [";
    for (int i = 0; i < result3.size(); i++) {
        std::cout << result3[i];
        if (i < result3.size() - 1) std::cout << ",";
    }
    std::cout << "]" << std::endl;
    
    return 0;
}
