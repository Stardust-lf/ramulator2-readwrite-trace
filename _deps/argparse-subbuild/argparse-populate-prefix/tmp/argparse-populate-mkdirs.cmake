# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/fann/projects/ramulator2/ext/argparse"
  "/home/fann/projects/ramulator2/_deps/argparse-build"
  "/home/fann/projects/ramulator2/_deps/argparse-subbuild/argparse-populate-prefix"
  "/home/fann/projects/ramulator2/_deps/argparse-subbuild/argparse-populate-prefix/tmp"
  "/home/fann/projects/ramulator2/_deps/argparse-subbuild/argparse-populate-prefix/src/argparse-populate-stamp"
  "/home/fann/projects/ramulator2/_deps/argparse-subbuild/argparse-populate-prefix/src"
  "/home/fann/projects/ramulator2/_deps/argparse-subbuild/argparse-populate-prefix/src/argparse-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/fann/projects/ramulator2/_deps/argparse-subbuild/argparse-populate-prefix/src/argparse-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/fann/projects/ramulator2/_deps/argparse-subbuild/argparse-populate-prefix/src/argparse-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
