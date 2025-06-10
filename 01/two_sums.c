#include <stdio.h>
#include <stdlib.h>

// Structure to represent a key-value pair for our hash map
typedef struct {
    int key;    // The number from the array
    int value;  // The index of that number
    int used;   // Flag to indicate if this slot is occupied
} HashEntry;

// Simple hash function
int hash(int key, int size) {
    return abs(key) % size;
}

// Function to find a number in our hash table
int findInHash(HashEntry* hashTable, int size, int key) {
    int index = hash(key, size);
    int original_index = index;
    
    // Linear probing to handle collisions
    while (hashTable[index].used) {
        if (hashTable[index].key == key) {
            return hashTable[index].value;  // Found the key, return its value (index)
        }
        index = (index + 1) % size;  // Move to next slot
        
        // If we've cycled through all slots, key doesn't exist
        if (index == original_index) {
            break;
        }
    }
    return -1;  // Key not found
}

// Function to insert a key-value pair into our hash table
void insertInHash(HashEntry* hashTable, int size, int key, int value) {
    int index = hash(key, size);
    
    // Linear probing to find an empty slot
    while (hashTable[index].used) {
        index = (index + 1) % size;
    }
    
    hashTable[index].key = key;
    hashTable[index].value = value;
    hashTable[index].used = 1;
}

// Two Sum function
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // Allocate memory for the result array
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 0;  // Initialize return size
    
    // Create a hash table (using a simple array-based approach)
    int hashSize = numsSize * 2;  // Make it larger to reduce collisions
    HashEntry* hashTable = (HashEntry*)calloc(hashSize, sizeof(HashEntry));
    
    // Iterate through the array
    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        int complement = target - num;
        
        // Check if complement exists in hash table
        int complementIndex = findInHash(hashTable, hashSize, complement);
        if (complementIndex != -1) {
            // Found the pair!
            result[0] = complementIndex;
            result[1] = i;
            *returnSize = 2;
            free(hashTable);
            return result;
        }
        
        // Insert current number and its index into hash table
        insertInHash(hashTable, hashSize, num, i);
    }
    
    // No solution found
    free(hashTable);
    *returnSize = 0;
    return result;
}

// Helper function to print an array
void printArray(int* arr, int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]\n");
}

// Test function
void testTwoSum(int* nums, int numsSize, int target, const char* testName) {
    printf("Test: %s\n", testName);
    printf("Array: ");
    printArray(nums, numsSize);
    printf("Target: %d\n", target);
    
    int returnSize;
    int* result = twoSum(nums, numsSize, target, &returnSize);
    
    if (returnSize == 2) {
        printf("Result: [%d, %d]\n", result[0], result[1]);
        printf("Verification: nums[%d] + nums[%d] = %d + %d = %d\n", 
               result[0], result[1], nums[result[0]], nums[result[1]], 
               nums[result[0]] + nums[result[1]]);
    } else {
        printf("No solution found\n");
    }
    
    free(result);
    printf("\n");
}

int main() {
    printf("Two Sum Problem - C Implementation\n");
    printf("==================================\n\n");
    
    // Test case 1
    int nums1[] = {2, 7, 11, 15};
    testTwoSum(nums1, 4, 9, "Case 1");
    
    // Test case 2
    int nums2[] = {3, 2, 4};
    testTwoSum(nums2, 3, 6, "Case 2");
    
    // Test case 3
    int nums3[] = {3, 3};
    testTwoSum(nums3, 2, 6, "Case 3");
    
    // Test case 4 - No solution
    int nums4[] = {1, 2, 3};
    testTwoSum(nums4, 3, 7, "Case 4 (No solution)");
    
    return 0;
}
