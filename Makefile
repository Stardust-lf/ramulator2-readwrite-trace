# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Default target executed when no arguments are given to make.
default_target: all
.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:

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
CMAKE_SOURCE_DIR = /home/fann/projects/ramulator2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/fann/projects/ramulator2

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target package
package: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Run CPack packaging tool..."
	/usr/bin/cpack --config ./CPackConfig.cmake
.PHONY : package

# Special rule for the target package
package/fast: package
.PHONY : package/fast

# Special rule for the target package_source
package_source:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Run CPack packaging tool for source..."
	/usr/bin/cpack --config ./CPackSourceConfig.cmake /home/fann/projects/ramulator2/CPackSourceConfig.cmake
.PHONY : package_source

# Special rule for the target package_source
package_source/fast: package_source
.PHONY : package_source/fast

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "No interactive CMake dialog available..."
	/usr/bin/cmake -E echo No\ interactive\ CMake\ dialog\ available.
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache
.PHONY : edit_cache/fast

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Running CMake to regenerate build system..."
	/usr/bin/cmake --regenerate-during-build -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache
.PHONY : rebuild_cache/fast

# Special rule for the target list_install_components
list_install_components:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Available install components are: \"Unspecified\""
.PHONY : list_install_components

# Special rule for the target list_install_components
list_install_components/fast: list_install_components
.PHONY : list_install_components/fast

# Special rule for the target install
install: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Install the project..."
	/usr/bin/cmake -P cmake_install.cmake
.PHONY : install

# Special rule for the target install
install/fast: preinstall/fast
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Install the project..."
	/usr/bin/cmake -P cmake_install.cmake
.PHONY : install/fast

# Special rule for the target install/local
install/local: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Installing only the local directory..."
	/usr/bin/cmake -DCMAKE_INSTALL_LOCAL_ONLY=1 -P cmake_install.cmake
.PHONY : install/local

# Special rule for the target install/local
install/local/fast: preinstall/fast
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Installing only the local directory..."
	/usr/bin/cmake -DCMAKE_INSTALL_LOCAL_ONLY=1 -P cmake_install.cmake
.PHONY : install/local/fast

# Special rule for the target install/strip
install/strip: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Installing the project stripped..."
	/usr/bin/cmake -DCMAKE_INSTALL_DO_STRIP=1 -P cmake_install.cmake
.PHONY : install/strip

# Special rule for the target install/strip
install/strip/fast: preinstall/fast
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --cyan "Installing the project stripped..."
	/usr/bin/cmake -DCMAKE_INSTALL_DO_STRIP=1 -P cmake_install.cmake
.PHONY : install/strip/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /home/fann/projects/ramulator2/CMakeFiles /home/fann/projects/ramulator2//CMakeFiles/progress.marks
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /home/fann/projects/ramulator2/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean
.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -P /home/fann/projects/ramulator2/CMakeFiles/VerifyGlobs.cmake
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named ramulator

# Build rule for target.
ramulator: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator
.PHONY : ramulator

# fast build rule for target.
ramulator/fast:
	$(MAKE) $(MAKESILENT) -f CMakeFiles/ramulator.dir/build.make CMakeFiles/ramulator.dir/build
.PHONY : ramulator/fast

#=============================================================================
# Target rules for targets named ramulator-exe

# Build rule for target.
ramulator-exe: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator-exe
.PHONY : ramulator-exe

# fast build rule for target.
ramulator-exe/fast:
	$(MAKE) $(MAKESILENT) -f CMakeFiles/ramulator-exe.dir/build.make CMakeFiles/ramulator-exe.dir/build
.PHONY : ramulator-exe/fast

#=============================================================================
# Target rules for targets named Experimental

# Build rule for target.
Experimental: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 Experimental
.PHONY : Experimental

# fast build rule for target.
Experimental/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/Experimental.dir/build.make _deps/yaml-cpp-build/CMakeFiles/Experimental.dir/build
.PHONY : Experimental/fast

#=============================================================================
# Target rules for targets named Nightly

# Build rule for target.
Nightly: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 Nightly
.PHONY : Nightly

# fast build rule for target.
Nightly/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/Nightly.dir/build.make _deps/yaml-cpp-build/CMakeFiles/Nightly.dir/build
.PHONY : Nightly/fast

#=============================================================================
# Target rules for targets named Continuous

# Build rule for target.
Continuous: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 Continuous
.PHONY : Continuous

# fast build rule for target.
Continuous/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/Continuous.dir/build.make _deps/yaml-cpp-build/CMakeFiles/Continuous.dir/build
.PHONY : Continuous/fast

#=============================================================================
# Target rules for targets named NightlyMemoryCheck

# Build rule for target.
NightlyMemoryCheck: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 NightlyMemoryCheck
.PHONY : NightlyMemoryCheck

# fast build rule for target.
NightlyMemoryCheck/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/NightlyMemoryCheck.dir/build.make _deps/yaml-cpp-build/CMakeFiles/NightlyMemoryCheck.dir/build
.PHONY : NightlyMemoryCheck/fast

#=============================================================================
# Target rules for targets named NightlyStart

# Build rule for target.
NightlyStart: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 NightlyStart
.PHONY : NightlyStart

# fast build rule for target.
NightlyStart/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/NightlyStart.dir/build.make _deps/yaml-cpp-build/CMakeFiles/NightlyStart.dir/build
.PHONY : NightlyStart/fast

#=============================================================================
# Target rules for targets named NightlyUpdate

# Build rule for target.
NightlyUpdate: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 NightlyUpdate
.PHONY : NightlyUpdate

# fast build rule for target.
NightlyUpdate/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/NightlyUpdate.dir/build.make _deps/yaml-cpp-build/CMakeFiles/NightlyUpdate.dir/build
.PHONY : NightlyUpdate/fast

#=============================================================================
# Target rules for targets named NightlyConfigure

# Build rule for target.
NightlyConfigure: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 NightlyConfigure
.PHONY : NightlyConfigure

# fast build rule for target.
NightlyConfigure/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/NightlyConfigure.dir/build.make _deps/yaml-cpp-build/CMakeFiles/NightlyConfigure.dir/build
.PHONY : NightlyConfigure/fast

#=============================================================================
# Target rules for targets named NightlyBuild

# Build rule for target.
NightlyBuild: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 NightlyBuild
.PHONY : NightlyBuild

# fast build rule for target.
NightlyBuild/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/NightlyBuild.dir/build.make _deps/yaml-cpp-build/CMakeFiles/NightlyBuild.dir/build
.PHONY : NightlyBuild/fast

#=============================================================================
# Target rules for targets named NightlyTest

# Build rule for target.
NightlyTest: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 NightlyTest
.PHONY : NightlyTest

# fast build rule for target.
NightlyTest/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/NightlyTest.dir/build.make _deps/yaml-cpp-build/CMakeFiles/NightlyTest.dir/build
.PHONY : NightlyTest/fast

#=============================================================================
# Target rules for targets named NightlyCoverage

# Build rule for target.
NightlyCoverage: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 NightlyCoverage
.PHONY : NightlyCoverage

# fast build rule for target.
NightlyCoverage/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/NightlyCoverage.dir/build.make _deps/yaml-cpp-build/CMakeFiles/NightlyCoverage.dir/build
.PHONY : NightlyCoverage/fast

#=============================================================================
# Target rules for targets named NightlyMemCheck

# Build rule for target.
NightlyMemCheck: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 NightlyMemCheck
.PHONY : NightlyMemCheck

# fast build rule for target.
NightlyMemCheck/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/NightlyMemCheck.dir/build.make _deps/yaml-cpp-build/CMakeFiles/NightlyMemCheck.dir/build
.PHONY : NightlyMemCheck/fast

#=============================================================================
# Target rules for targets named NightlySubmit

# Build rule for target.
NightlySubmit: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 NightlySubmit
.PHONY : NightlySubmit

# fast build rule for target.
NightlySubmit/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/NightlySubmit.dir/build.make _deps/yaml-cpp-build/CMakeFiles/NightlySubmit.dir/build
.PHONY : NightlySubmit/fast

#=============================================================================
# Target rules for targets named ExperimentalStart

# Build rule for target.
ExperimentalStart: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ExperimentalStart
.PHONY : ExperimentalStart

# fast build rule for target.
ExperimentalStart/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ExperimentalStart.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ExperimentalStart.dir/build
.PHONY : ExperimentalStart/fast

#=============================================================================
# Target rules for targets named ExperimentalUpdate

# Build rule for target.
ExperimentalUpdate: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ExperimentalUpdate
.PHONY : ExperimentalUpdate

# fast build rule for target.
ExperimentalUpdate/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ExperimentalUpdate.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ExperimentalUpdate.dir/build
.PHONY : ExperimentalUpdate/fast

#=============================================================================
# Target rules for targets named ExperimentalConfigure

# Build rule for target.
ExperimentalConfigure: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ExperimentalConfigure
.PHONY : ExperimentalConfigure

# fast build rule for target.
ExperimentalConfigure/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ExperimentalConfigure.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ExperimentalConfigure.dir/build
.PHONY : ExperimentalConfigure/fast

#=============================================================================
# Target rules for targets named ExperimentalBuild

# Build rule for target.
ExperimentalBuild: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ExperimentalBuild
.PHONY : ExperimentalBuild

# fast build rule for target.
ExperimentalBuild/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ExperimentalBuild.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ExperimentalBuild.dir/build
.PHONY : ExperimentalBuild/fast

#=============================================================================
# Target rules for targets named ExperimentalTest

# Build rule for target.
ExperimentalTest: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ExperimentalTest
.PHONY : ExperimentalTest

# fast build rule for target.
ExperimentalTest/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ExperimentalTest.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ExperimentalTest.dir/build
.PHONY : ExperimentalTest/fast

#=============================================================================
# Target rules for targets named ExperimentalCoverage

# Build rule for target.
ExperimentalCoverage: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ExperimentalCoverage
.PHONY : ExperimentalCoverage

# fast build rule for target.
ExperimentalCoverage/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ExperimentalCoverage.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ExperimentalCoverage.dir/build
.PHONY : ExperimentalCoverage/fast

#=============================================================================
# Target rules for targets named ExperimentalMemCheck

# Build rule for target.
ExperimentalMemCheck: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ExperimentalMemCheck
.PHONY : ExperimentalMemCheck

# fast build rule for target.
ExperimentalMemCheck/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ExperimentalMemCheck.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ExperimentalMemCheck.dir/build
.PHONY : ExperimentalMemCheck/fast

#=============================================================================
# Target rules for targets named ExperimentalSubmit

# Build rule for target.
ExperimentalSubmit: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ExperimentalSubmit
.PHONY : ExperimentalSubmit

# fast build rule for target.
ExperimentalSubmit/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ExperimentalSubmit.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ExperimentalSubmit.dir/build
.PHONY : ExperimentalSubmit/fast

#=============================================================================
# Target rules for targets named ContinuousStart

# Build rule for target.
ContinuousStart: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ContinuousStart
.PHONY : ContinuousStart

# fast build rule for target.
ContinuousStart/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ContinuousStart.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ContinuousStart.dir/build
.PHONY : ContinuousStart/fast

#=============================================================================
# Target rules for targets named ContinuousUpdate

# Build rule for target.
ContinuousUpdate: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ContinuousUpdate
.PHONY : ContinuousUpdate

# fast build rule for target.
ContinuousUpdate/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ContinuousUpdate.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ContinuousUpdate.dir/build
.PHONY : ContinuousUpdate/fast

#=============================================================================
# Target rules for targets named ContinuousConfigure

# Build rule for target.
ContinuousConfigure: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ContinuousConfigure
.PHONY : ContinuousConfigure

# fast build rule for target.
ContinuousConfigure/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ContinuousConfigure.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ContinuousConfigure.dir/build
.PHONY : ContinuousConfigure/fast

#=============================================================================
# Target rules for targets named ContinuousBuild

# Build rule for target.
ContinuousBuild: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ContinuousBuild
.PHONY : ContinuousBuild

# fast build rule for target.
ContinuousBuild/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ContinuousBuild.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ContinuousBuild.dir/build
.PHONY : ContinuousBuild/fast

#=============================================================================
# Target rules for targets named ContinuousTest

# Build rule for target.
ContinuousTest: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ContinuousTest
.PHONY : ContinuousTest

# fast build rule for target.
ContinuousTest/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ContinuousTest.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ContinuousTest.dir/build
.PHONY : ContinuousTest/fast

#=============================================================================
# Target rules for targets named ContinuousCoverage

# Build rule for target.
ContinuousCoverage: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ContinuousCoverage
.PHONY : ContinuousCoverage

# fast build rule for target.
ContinuousCoverage/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ContinuousCoverage.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ContinuousCoverage.dir/build
.PHONY : ContinuousCoverage/fast

#=============================================================================
# Target rules for targets named ContinuousMemCheck

# Build rule for target.
ContinuousMemCheck: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ContinuousMemCheck
.PHONY : ContinuousMemCheck

# fast build rule for target.
ContinuousMemCheck/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ContinuousMemCheck.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ContinuousMemCheck.dir/build
.PHONY : ContinuousMemCheck/fast

#=============================================================================
# Target rules for targets named ContinuousSubmit

# Build rule for target.
ContinuousSubmit: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ContinuousSubmit
.PHONY : ContinuousSubmit

# fast build rule for target.
ContinuousSubmit/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/ContinuousSubmit.dir/build.make _deps/yaml-cpp-build/CMakeFiles/ContinuousSubmit.dir/build
.PHONY : ContinuousSubmit/fast

#=============================================================================
# Target rules for targets named yaml-cpp

# Build rule for target.
yaml-cpp: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 yaml-cpp
.PHONY : yaml-cpp

# fast build rule for target.
yaml-cpp/fast:
	$(MAKE) $(MAKESILENT) -f _deps/yaml-cpp-build/CMakeFiles/yaml-cpp.dir/build.make _deps/yaml-cpp-build/CMakeFiles/yaml-cpp.dir/build
.PHONY : yaml-cpp/fast

#=============================================================================
# Target rules for targets named spdlog

# Build rule for target.
spdlog: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 spdlog
.PHONY : spdlog

# fast build rule for target.
spdlog/fast:
	$(MAKE) $(MAKESILENT) -f _deps/spdlog-build/CMakeFiles/spdlog.dir/build.make _deps/spdlog-build/CMakeFiles/spdlog.dir/build
.PHONY : spdlog/fast

#=============================================================================
# Target rules for targets named ramulator-base

# Build rule for target.
ramulator-base: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator-base
.PHONY : ramulator-base

# fast build rule for target.
ramulator-base/fast:
	$(MAKE) $(MAKESILENT) -f src/base/CMakeFiles/ramulator-base.dir/build.make src/base/CMakeFiles/ramulator-base.dir/build
.PHONY : ramulator-base/fast

#=============================================================================
# Target rules for targets named ramulator-test

# Build rule for target.
ramulator-test: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator-test
.PHONY : ramulator-test

# fast build rule for target.
ramulator-test/fast:
	$(MAKE) $(MAKESILENT) -f src/test/CMakeFiles/ramulator-test.dir/build.make src/test/CMakeFiles/ramulator-test.dir/build
.PHONY : ramulator-test/fast

#=============================================================================
# Target rules for targets named ramulator-frontend

# Build rule for target.
ramulator-frontend: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator-frontend
.PHONY : ramulator-frontend

# fast build rule for target.
ramulator-frontend/fast:
	$(MAKE) $(MAKESILENT) -f src/frontend/CMakeFiles/ramulator-frontend.dir/build.make src/frontend/CMakeFiles/ramulator-frontend.dir/build
.PHONY : ramulator-frontend/fast

#=============================================================================
# Target rules for targets named ramulator-translation

# Build rule for target.
ramulator-translation: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator-translation
.PHONY : ramulator-translation

# fast build rule for target.
ramulator-translation/fast:
	$(MAKE) $(MAKESILENT) -f src/translation/CMakeFiles/ramulator-translation.dir/build.make src/translation/CMakeFiles/ramulator-translation.dir/build
.PHONY : ramulator-translation/fast

#=============================================================================
# Target rules for targets named ramulator-memorysystem

# Build rule for target.
ramulator-memorysystem: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator-memorysystem
.PHONY : ramulator-memorysystem

# fast build rule for target.
ramulator-memorysystem/fast:
	$(MAKE) $(MAKESILENT) -f src/memory_system/CMakeFiles/ramulator-memorysystem.dir/build.make src/memory_system/CMakeFiles/ramulator-memorysystem.dir/build
.PHONY : ramulator-memorysystem/fast

#=============================================================================
# Target rules for targets named ramulator-addrmapper

# Build rule for target.
ramulator-addrmapper: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator-addrmapper
.PHONY : ramulator-addrmapper

# fast build rule for target.
ramulator-addrmapper/fast:
	$(MAKE) $(MAKESILENT) -f src/addr_mapper/CMakeFiles/ramulator-addrmapper.dir/build.make src/addr_mapper/CMakeFiles/ramulator-addrmapper.dir/build
.PHONY : ramulator-addrmapper/fast

#=============================================================================
# Target rules for targets named ramulator-dram

# Build rule for target.
ramulator-dram: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator-dram
.PHONY : ramulator-dram

# fast build rule for target.
ramulator-dram/fast:
	$(MAKE) $(MAKESILENT) -f src/dram/CMakeFiles/ramulator-dram.dir/build.make src/dram/CMakeFiles/ramulator-dram.dir/build
.PHONY : ramulator-dram/fast

#=============================================================================
# Target rules for targets named ramulator-controller

# Build rule for target.
ramulator-controller: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 ramulator-controller
.PHONY : ramulator-controller

# fast build rule for target.
ramulator-controller/fast:
	$(MAKE) $(MAKESILENT) -f src/dram_controller/CMakeFiles/ramulator-controller.dir/build.make src/dram_controller/CMakeFiles/ramulator-controller.dir/build
.PHONY : ramulator-controller/fast

src/main.o: src/main.cpp.o
.PHONY : src/main.o

# target to build an object file
src/main.cpp.o:
	$(MAKE) $(MAKESILENT) -f CMakeFiles/ramulator-exe.dir/build.make CMakeFiles/ramulator-exe.dir/src/main.cpp.o
.PHONY : src/main.cpp.o

src/main.i: src/main.cpp.i
.PHONY : src/main.i

# target to preprocess a source file
src/main.cpp.i:
	$(MAKE) $(MAKESILENT) -f CMakeFiles/ramulator-exe.dir/build.make CMakeFiles/ramulator-exe.dir/src/main.cpp.i
.PHONY : src/main.cpp.i

src/main.s: src/main.cpp.s
.PHONY : src/main.s

# target to generate assembly for a file
src/main.cpp.s:
	$(MAKE) $(MAKESILENT) -f CMakeFiles/ramulator-exe.dir/build.make CMakeFiles/ramulator-exe.dir/src/main.cpp.s
.PHONY : src/main.cpp.s

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... edit_cache"
	@echo "... install"
	@echo "... install/local"
	@echo "... install/strip"
	@echo "... list_install_components"
	@echo "... package"
	@echo "... package_source"
	@echo "... rebuild_cache"
	@echo "... Continuous"
	@echo "... ContinuousBuild"
	@echo "... ContinuousConfigure"
	@echo "... ContinuousCoverage"
	@echo "... ContinuousMemCheck"
	@echo "... ContinuousStart"
	@echo "... ContinuousSubmit"
	@echo "... ContinuousTest"
	@echo "... ContinuousUpdate"
	@echo "... Experimental"
	@echo "... ExperimentalBuild"
	@echo "... ExperimentalConfigure"
	@echo "... ExperimentalCoverage"
	@echo "... ExperimentalMemCheck"
	@echo "... ExperimentalStart"
	@echo "... ExperimentalSubmit"
	@echo "... ExperimentalTest"
	@echo "... ExperimentalUpdate"
	@echo "... Nightly"
	@echo "... NightlyBuild"
	@echo "... NightlyConfigure"
	@echo "... NightlyCoverage"
	@echo "... NightlyMemCheck"
	@echo "... NightlyMemoryCheck"
	@echo "... NightlyStart"
	@echo "... NightlySubmit"
	@echo "... NightlyTest"
	@echo "... NightlyUpdate"
	@echo "... ramulator"
	@echo "... ramulator-addrmapper"
	@echo "... ramulator-base"
	@echo "... ramulator-controller"
	@echo "... ramulator-dram"
	@echo "... ramulator-exe"
	@echo "... ramulator-frontend"
	@echo "... ramulator-memorysystem"
	@echo "... ramulator-test"
	@echo "... ramulator-translation"
	@echo "... spdlog"
	@echo "... yaml-cpp"
	@echo "... src/main.o"
	@echo "... src/main.i"
	@echo "... src/main.s"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -P /home/fann/projects/ramulator2/CMakeFiles/VerifyGlobs.cmake
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system

