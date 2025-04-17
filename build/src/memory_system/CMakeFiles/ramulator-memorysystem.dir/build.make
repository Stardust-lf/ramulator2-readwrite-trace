# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/fann/projects/ramulator2-readwrite-trace

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/fann/projects/ramulator2-readwrite-trace/build

# Include any dependencies generated for this target.
include src/memory_system/CMakeFiles/ramulator-memorysystem.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/memory_system/CMakeFiles/ramulator-memorysystem.dir/compiler_depend.make

# Include the progress variables for this target.
include src/memory_system/CMakeFiles/ramulator-memorysystem.dir/progress.make

# Include the compile flags for this target's objects.
include src/memory_system/CMakeFiles/ramulator-memorysystem.dir/flags.make

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.o: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/flags.make
src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.o: /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/bh_DRAM_system.cpp
src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.o: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/fann/projects/ramulator2-readwrite-trace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.o"
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.o -MF CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.o.d -o CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.o -c /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/bh_DRAM_system.cpp

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.i"
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/bh_DRAM_system.cpp > CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.i

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.s"
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/bh_DRAM_system.cpp -o CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.s

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.o: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/flags.make
src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.o: /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/dummy_memory_system.cpp
src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.o: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/fann/projects/ramulator2-readwrite-trace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.o"
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.o -MF CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.o.d -o CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.o -c /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/dummy_memory_system.cpp

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.i"
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/dummy_memory_system.cpp > CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.i

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.s"
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/dummy_memory_system.cpp -o CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.s

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.o: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/flags.make
src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.o: /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/generic_DRAM_system.cpp
src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.o: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/fann/projects/ramulator2-readwrite-trace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.o"
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.o -MF CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.o.d -o CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.o -c /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/generic_DRAM_system.cpp

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.i"
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/generic_DRAM_system.cpp > CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.i

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.s"
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fann/projects/ramulator2-readwrite-trace/src/memory_system/impl/generic_DRAM_system.cpp -o CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.s

ramulator-memorysystem: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/bh_DRAM_system.cpp.o
ramulator-memorysystem: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/dummy_memory_system.cpp.o
ramulator-memorysystem: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/impl/generic_DRAM_system.cpp.o
ramulator-memorysystem: src/memory_system/CMakeFiles/ramulator-memorysystem.dir/build.make
.PHONY : ramulator-memorysystem

# Rule to build all files generated by this target.
src/memory_system/CMakeFiles/ramulator-memorysystem.dir/build: ramulator-memorysystem
.PHONY : src/memory_system/CMakeFiles/ramulator-memorysystem.dir/build

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/clean:
	cd /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system && $(CMAKE_COMMAND) -P CMakeFiles/ramulator-memorysystem.dir/cmake_clean.cmake
.PHONY : src/memory_system/CMakeFiles/ramulator-memorysystem.dir/clean

src/memory_system/CMakeFiles/ramulator-memorysystem.dir/depend:
	cd /home/fann/projects/ramulator2-readwrite-trace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/fann/projects/ramulator2-readwrite-trace /home/fann/projects/ramulator2-readwrite-trace/src/memory_system /home/fann/projects/ramulator2-readwrite-trace/build /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system /home/fann/projects/ramulator2-readwrite-trace/build/src/memory_system/CMakeFiles/ramulator-memorysystem.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : src/memory_system/CMakeFiles/ramulator-memorysystem.dir/depend

