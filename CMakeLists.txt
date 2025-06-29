cmake_minimum_required(VERSION 3.10)
project(leet_code)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Set output directory
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Add executable for two_sums.cpp


# Add executables for Leetcode_75 problems
add_executable(compress Leetcode_75/compress.cpp)
add_executable(isSubsequence Leetcode_75/isSubsequence.cpp)
add_executable(moveZeroes Leetcode_75/moveZeroes.cpp)

# Optional: Add compile flags for better debugging and warnings

target_compile_options(compress PRIVATE -Wall -Wextra -g)
target_compile_options(isSubsequence PRIVATE -Wall -Wextra -g)
target_compile_options(moveZeroes PRIVATE -Wall -Wextra -g) 