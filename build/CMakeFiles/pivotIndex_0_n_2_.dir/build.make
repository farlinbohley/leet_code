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
include CMakeFiles/pivotIndex_0_n_2_.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/pivotIndex_0_n_2_.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/pivotIndex_0_n_2_.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/pivotIndex_0_n_2_.dir/flags.make

CMakeFiles/pivotIndex_0_n_2_.dir/codegen:
.PHONY : CMakeFiles/pivotIndex_0_n_2_.dir/codegen

CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.o: CMakeFiles/pivotIndex_0_n_2_.dir/flags.make
CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.o: /Users/Chris/leet_code/Leetcode_75/pivotIndex_0(n^2).cpp
CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.o: CMakeFiles/pivotIndex_0_n_2_.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/Chris/leet_code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.o"
	/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT "CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.o" -MF "CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.o.d" -o "CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.o" -c "/Users/Chris/leet_code/Leetcode_75/pivotIndex_0(n^2).cpp"

CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.i"
	/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/Chris/leet_code/Leetcode_75/pivotIndex_0(n^2).cpp" > "CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.i"

CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.s"
	/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/Chris/leet_code/Leetcode_75/pivotIndex_0(n^2).cpp" -o "CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.s"

# Object files for target pivotIndex_0_n_2_
pivotIndex_0_n_2__OBJECTS = \
"CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.o"

# External object files for target pivotIndex_0_n_2_
pivotIndex_0_n_2__EXTERNAL_OBJECTS =

/Users/Chris/leet_code/Leetcode_75/output/pivotIndex_0_n_2_: CMakeFiles/pivotIndex_0_n_2_.dir/Leetcode_75/pivotIndex_0(n^2).cpp.o
/Users/Chris/leet_code/Leetcode_75/output/pivotIndex_0_n_2_: CMakeFiles/pivotIndex_0_n_2_.dir/build.make
/Users/Chris/leet_code/Leetcode_75/output/pivotIndex_0_n_2_: CMakeFiles/pivotIndex_0_n_2_.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/Chris/leet_code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /Users/Chris/leet_code/Leetcode_75/output/pivotIndex_0_n_2_"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pivotIndex_0_n_2_.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/pivotIndex_0_n_2_.dir/build: /Users/Chris/leet_code/Leetcode_75/output/pivotIndex_0_n_2_
.PHONY : CMakeFiles/pivotIndex_0_n_2_.dir/build

CMakeFiles/pivotIndex_0_n_2_.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/pivotIndex_0_n_2_.dir/cmake_clean.cmake
.PHONY : CMakeFiles/pivotIndex_0_n_2_.dir/clean

CMakeFiles/pivotIndex_0_n_2_.dir/depend:
	cd /Users/Chris/leet_code/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/Chris/leet_code /Users/Chris/leet_code /Users/Chris/leet_code/build /Users/Chris/leet_code/build /Users/Chris/leet_code/build/CMakeFiles/pivotIndex_0_n_2_.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/pivotIndex_0_n_2_.dir/depend

