# In a minimal CMakeLists.txt, one line specifying add_executable will do
# Adding a Version Number and Configured Header File
cmake_minimum_required(VERSION 2.6)
project (Leetcode)

# The version number.
set (Leetcode_VERSION_MAJOR 1)
set (Leetcode_VERSION_MINOR 0)

#=============================================================================================
# project settings 
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "DEBUG")
endif (NOT CMAKE_BUILD_TYPE)

# compiler FLAGS
#set(CMAKE_CXX_FLAGS_DEBUG "put your flags")
#set(CMAKE_CXX_FLAGS_MINSIZEREL "put your flags")
#set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "put your flags")
#set(CMAKE_CXX_FLAGS_RELEASE "put your flags")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS} -O0 -ggdb -Wall -std=c++11")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS} -O3 -std=c++11")
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -ggdb -Wall -std=c++11")

message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
if (${CMAKE_BUILD_TYPE} MATCHES "DEBUG")
	message(STATUS "Build flags for debug: ${CMAKE_CXX_FLAGS_DEBUG}")
else ()
	message(STATUS "Build flags for release: ${CMAKE_CXX_FLAGS_RELEASE}")
endif ()


 
# configure a header file to pass some of the CMake settings
# to the source code
#configure_file (
	#"${PROJECT_SOURCE_DIR}/LeetcodeConfig.h.in"
	#"${PROJECT_BINARY_DIR}/LeetcodeConfig.h"
  #)
 
# add the binary tree to the search path for include files
# so that we will find LeetcodeConfig.h
include_directories("${PROJECT_BINARY_DIR}")
 
#=======================================BUILD TARGETS==========================================

# add the executable target
add_executable(WildcardMatching WildcardMatching.cpp)
add_executable(wordBreakII wordBreakII.cpp)
add_executable(minimumWindowString minimumWindowString.cpp)
add_executable(totalHammingDistance totalHammingDistance.cpp)
add_executable(sumOfTwoIntegers sumOfTwoIntegers.cpp)
add_executable(divide divide.cpp)
add_executable(longestPalindrome longestPalindrome.cpp)
add_executable(sortslist sortslist.cpp)
add_executable(searchRotatedSortedArray searchRotatedSortedArray.cpp)
add_executable(insertionSortList insertionSortList.cpp)
add_executable(magicalString magicalString.cpp)
add_executable(serializeAndDeserializeBinaryTree serializeAndDeserializeBinaryTree.cpp)

add_library(intersectionOfTwoLinkedLists SHARED intersectionOfTwoLinkedLists.cpp)
add_library(maxPoints-anchor-hash SHARED maxPoints-anchor-hash.cpp)

#=============================================================================================
# the following is not used yet, serving as tutorial template
# add library target
#add_library(alg alg.cpp)
#target_link_libraries (a.out alg)


#=============================================================================================
# install
#install (TARGETS MathFunctions DESTINATION bin)
#install (FILES MathFunctions.h DESTINATION include)

# add test
include(CTest)

# does the application run
add_test (WildcardMatchingRun WildcardMatching hello he*o)

#=============================================================================================
# Options: control statement
# should we use our own math functions?
option (USE_MYMATH 
	"Use tutorial provided math implementation" OFF) 

# add the MathFunctions library?
#
if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
  add_subdirectory (MathFunctions)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)
