cmake_minimum_required(VERSION 3.20)
project(leet_code)

set(CMAKE_CXX_STANDARD 17)

# Set the output directory for executables
# Place executables in the output folder under Leetcode_75
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Leetcode_75/output)

# Option 2: Put executables in project root
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR})

# Option 3: Put executables in a custom folder
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/executables)

# Option 4: Put executables directly in build folder
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

# Find all .cpp files in Leetcode_75 directory
file(GLOB CPP_FILES "Leetcode_75/*.cpp")

# Create executables for each .cpp file
foreach(CPP_FILE ${CPP_FILES})
    get_filename_component(EXEC_NAME ${CPP_FILE} NAME_WE)
    add_executable(${EXEC_NAME} ${CPP_FILE}
            Leetcode_75/longestSubarray.cpp
            Leetcode_75/longestSubarray.cpp
            Leetcode_75/longestSubarray.cpp
            Leetcode_75/largestAltitude.cpp
            "Leetcode_75/pivotIndex_0(n^2).cpp"
            Leetcode_75/pivotIndex.cpp)
endforeach()
