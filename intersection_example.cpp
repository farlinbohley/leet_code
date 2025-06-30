#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

// Function to find the intersection of two vectors
std::vector<int> findIntersection(const std::vector<int>& vec1, const std::vector<int>& vec2) {
    // 1. Create a hash set from the first vector for efficient lookup.
    // The constructor of std::unordered_set can take iterators.
    std::unordered_set<int> element_set(vec1.begin(), vec1.end());

    std::vector<int> intersection;

    // 2. Iterate through the second vector.
    for (int num : vec2) {
        // 3. Check if the element exists in the hash set.
        // The .count() method returns 1 if the element is present, and 0 otherwise.
        // This is a very common and readable way to check for existence.
        if (element_set.count(num)) {
            // 4. If it exists, add it to our result vector.
            intersection.push_back(num);

            // 5. Remove the element from the set to handle duplicates.
            // If vec2 has duplicate elements, this ensures we only add
            // the element to our intersection once. For example, if vec1 = {1, 2}
            // and vec2 = {1, 1}, the intersection is {1}, not {1, 1}.
            element_set.erase(num);
        }
    }

    return intersection;
}

int main() {
    std::vector<int> v1 = {1, 2, 2, 4, 5, 6};
    std::vector<int> v2 = {2, 3, 5, 7, 2};

    std::vector<int> result = findIntersection(v1, v2);

    std::cout << "Vector 1: ";
    for (int num : v1) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::cout << "Vector 2: ";
    for (int num : v2) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::cout << "Intersection: ";
    for (int num : result) {
        std::cout << num << " ";
    }
    std::cout << std::endl; // Should be 2 5

    // Another example
    std::vector<int> v3 = {4, 9, 5};
    std::vector<int> v4 = {9, 4, 9, 8, 4};
    result = findIntersection(v3, v4);

    std::cout << "\nVector 3: ";
    for (int num : v3) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::cout << "Vector 4: ";
    for (int num : v4) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::cout << "Intersection: ";
    for (int num : result) {
        std::cout << num << " ";
    }
    std::cout << std::endl; // Should be 9 4 or 4 9

    return 0;
} 