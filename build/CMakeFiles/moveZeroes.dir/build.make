# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 4.0

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/Chris/leet_code

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/Chris/leet_code/build

# Include any dependencies generated for this target.
include CMakeFiles/moveZeroes.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/moveZeroes.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/moveZeroes.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/moveZeroes.dir/flags.make

CMakeFiles/moveZeroes.dir/codegen:
.PHONY : CMakeFiles/moveZeroes.dir/codegen

CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.o: CMakeFiles/moveZeroes.dir/flags.make
CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.o: /Users/Chris/leet_code/Leetcode_75/moveZeroes.cpp
CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.o: CMakeFiles/moveZeroes.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/Chris/leet_code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.o"
	/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.o -MF CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.o.d -o CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.o -c /Users/Chris/leet_code/Leetcode_75/moveZeroes.cpp

CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.i"
	/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/Chris/leet_code/Leetcode_75/moveZeroes.cpp > CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.i

CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.s"
	/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/Chris/leet_code/Leetcode_75/moveZeroes.cpp -o CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.s

# Object files for target moveZeroes
moveZeroes_OBJECTS = \
"CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.o"

# External object files for target moveZeroes
moveZeroes_EXTERNAL_OBJECTS =

/Users/Chris/leet_code/Leetcode_75/output/moveZeroes: CMakeFiles/moveZeroes.dir/Leetcode_75/moveZeroes.cpp.o
/Users/Chris/leet_code/Leetcode_75/output/moveZeroes: CMakeFiles/moveZeroes.dir/build.make
/Users/Chris/leet_code/Leetcode_75/output/moveZeroes: CMakeFiles/moveZeroes.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/Chris/leet_code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /Users/Chris/leet_code/Leetcode_75/output/moveZeroes"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/moveZeroes.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/moveZeroes.dir/build: /Users/Chris/leet_code/Leetcode_75/output/moveZeroes
.PHONY : CMakeFiles/moveZeroes.dir/build

CMakeFiles/moveZeroes.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/moveZeroes.dir/cmake_clean.cmake
.PHONY : CMakeFiles/moveZeroes.dir/clean

CMakeFiles/moveZeroes.dir/depend:
	cd /Users/Chris/leet_code/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/Chris/leet_code /Users/Chris/leet_code /Users/Chris/leet_code/build /Users/Chris/leet_code/build /Users/Chris/leet_code/build/CMakeFiles/moveZeroes.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/moveZeroes.dir/depend

