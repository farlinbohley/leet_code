cmake_minimum_required(VERSION 3.20)
project(leet_code)

set(CMAKE_CXX_STANDARD 17)

# Set debug flags for different platforms
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    if(MSVC)
        set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /Zi /Od")
    else()
        set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0")
    endif()
endif()

# Set the output directory for executables
# Place executables in the output folder under Leetcode_75
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/Leetcode_75/output)

# For multi-configuration generators (like Visual Studio on Windows)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})

# Option 2: Put executables in project root
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR})

# Option 3: Put executables in a custom folder
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/executables)

# Option 4: Put executables directly in build folder
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

# Also set CMAKE_EXPORT_COMPILE_COMMANDS to generate compile_commands.json
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Windows-specific settings
if(WIN32)
    # Set Windows subsystem to console for all executables
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /SUBSYSTEM:CONSOLE")
endif()

# Find all .cpp files in Leetcode_75 directory
file(GLOB CPP_FILES "Leetcode_75/*.cpp")

# Create executables for each .cpp file
foreach(CPP_FILE ${CPP_FILES})
    get_filename_component(EXEC_NAME ${CPP_FILE} NAME_WE)
    # Sanitize executable name by replacing invalid characters
    string(REPLACE "(" "_" EXEC_NAME ${EXEC_NAME})
    string(REPLACE ")" "_" EXEC_NAME ${EXEC_NAME})
    string(REPLACE "^" "_" EXEC_NAME ${EXEC_NAME})
    add_executable(${EXEC_NAME} ${CPP_FILE})
endforeach()

# Also compile C++ files in problems directory if needed
file(GLOB PROBLEM_CPP_FILES "problems/*/*.cpp")
foreach(CPP_FILE ${PROBLEM_CPP_FILES})
    get_filename_component(EXEC_NAME ${CPP_FILE} NAME_WE)
    get_filename_component(PARENT_DIR ${CPP_FILE} DIRECTORY)
    get_filename_component(PARENT_NAME ${PARENT_DIR} NAME)
    # Sanitize executable name
    string(REPLACE "(" "_" EXEC_NAME ${EXEC_NAME})
    string(REPLACE ")" "_" EXEC_NAME ${EXEC_NAME})
    string(REPLACE "^" "_" EXEC_NAME ${EXEC_NAME})
    # Create executable with parent directory name prefix to avoid name conflicts
    add_executable(${PARENT_NAME}_${EXEC_NAME} ${CPP_FILE})
endforeach()
