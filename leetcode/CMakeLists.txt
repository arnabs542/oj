# In a minimal CMakeLists.txt, one line specifying add_executable will do
# Adding a Version Number and Configured Header File
cmake_minimum_required(VERSION 2.6)
#project (Leetcode)

# The version number.
#set (Leetcode_VERSION_MAJOR 1)
#set (Leetcode_VERSION_MINOR 0)

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
# enable sanitizer: -fsanitize=address,undefined,integer
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS} -O0 -ggdb -Wall -std=c++11 -fsanitize=address,undefined")
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
add_executable(regularExpressionMatching regularExpressionMatching.cpp)
add_executable(wildcardMatching wildcardMatching.cpp)
#add_executable(wordBreakII wordBreakII.cpp)
add_executable(minimumWindowString minimumWindowString.cpp)
add_executable(totalHammingDistance totalHammingDistance.cpp)
add_executable(sumOfTwoIntegers sumOfTwoIntegers.cpp)
add_executable(divide divide.cpp)
add_executable(longestPalindromicSubstring longestPalindromicSubstring.cpp)
add_executable(sortslist sortslist.cpp)
add_executable(searchRotatedSortedArray searchRotatedSortedArray.cpp)
add_executable(insertionSortList insertionSortList.cpp)
add_executable(magicalString magicalString.cpp)
add_executable(serializeAndDeserializeBinaryTree serializeAndDeserializeBinaryTree.cpp)
add_executable(onesAndZeroes onesAndZeroes.cpp)
add_executable(matchsticksToSquare matchsticksToSquare.cpp)
add_executable(minimumHeightTrees minimumHeightTrees.cpp)
add_executable(verifyPreorderSerializationOfABinaryTree verifyPreorderSerializationOfABinaryTree.cpp)
add_executable(tagValidator tagValidator.cpp)
add_executable(deleteNodeInABst deleteNodeInABst.cpp)
add_executable(stringCompression stringCompression.cpp)
add_executable(findMedianFromDataStream findMedianFromDataStream.cpp)
add_executable(slidingWindowMedian slidingWindowMedian.cpp)
#add_executable(largestPalindromeProduct largestPalindromeProduct.cpp)
add_executable(copyListWithRandomPointer copyListWithRandomPointer.cpp)
add_executable(replaceWords replaceWords.cpp)
add_executable(implementMagicDictionary implementMagicDictionary.cpp)
add_executable(taskScheduler taskScheduler.cpp)
add_executable(continuousSubarraySum continuousSubarraySum.cpp)
add_executable(longestPalindromicSubsequence longestPalindromicSubsequence.cpp)
add_executable(palindromicSubstrings palindromicSubstrings.cpp)
add_executable(reverseWordsInAString reverseWordsInAString.cpp)
add_executable(maximumXOROfTwoNumbersInAnArray maximumXOROfTwoNumbersInAnArray.cpp)
add_executable(expressionAddOperators expressionAddOperators.cpp)
add_executable(lfuCache lfuCache.cpp)
add_executable(allOoneDataStructure allOoneDataStructure.cpp)
add_executable(constructQuadTree constructQuadTree.cpp)
add_executable(wiggleSort wiggleSort.cpp)
add_executable(implementRand10UsingRand7 implementRand10UsingRand7.cpp)
add_executable(generateRandomPointInACircle generateRandomPointInACircle.cpp)
add_executable(circularArrayLoop circularArrayLoop.cpp)
add_executable(minimumGeneticMutation minimumGeneticMutation.cpp)
add_executable(poorPigs poorPigs.cpp)
add_executable(stoneGame stoneGame.cpp)
add_executable(stoneGameII stoneGameII.cpp)
add_executable(meetingRooms meetingRooms.cpp)
add_executable(meetingRoomsII meetingRoomsII.cpp)
add_executable(kthLargestElementInAnArray kthLargestElementInAnArray.cpp)
add_executable(heaters heaters.cpp)
add_executable(NaryTreeLevelOrderTraversal NaryTreeLevelOrderTraversal.cpp)
add_executable(licenseKeyFormatting licenseKeyFormatting.cpp)
add_executable(countOfRangeSum countOfRangeSum.cpp)
add_executable(maxConsecutiveOnes maxConsecutiveOnes.cpp)
add_executable(maxConsecutiveOnesII maxConsecutiveOnesII.cpp)
add_executable(maxConsecutiveOnesIII maxConsecutiveOnesIII.cpp)
add_executable(maxSumOfRectangleNoLargerThanK maxSumOfRectangleNoLargerThanK.cpp)
add_executable(maximumSideLengthOfASquareWithSumLessThanOrEqualToThreshold maximumSideLengthOfASquareWithSumLessThanOrEqualToThreshold.cpp)
add_executable(769.maxChunksToMakeSorted 769.maxChunksToMakeSorted.cpp)
add_executable(768.maxChunksToMakeSortedII 768.maxChunksToMakeSortedII.cpp)
add_executable(canIWin canIWin.cpp)
add_executable(359.loggerRateLimiter 359.loggerRateLimiter.cpp)
add_executable(932.beautifulArray 932.beautifulArray.cpp)
add_executable(507.perfectNumber 507.perfectNumber.cpp)
add_executable(812.largestTriangleArea 812.largestTriangleArea.cpp)

add_library(_type SHARED _type.cpp _tree.cpp _trieTree.cpp)
add_library(intersectionOfTwoLinkedLists SHARED intersectionOfTwoLinkedLists.cpp)
#add_library(maxPoints-anchor-hash SHARED maxPoints-anchor-hash.cpp)


# TEST
add_executable(testTree tests/test_tree.cpp)
add_executable(testTrie tests/test_trie.cpp)
target_link_libraries(testTree _type)
target_link_libraries(testTrie _type)
target_link_libraries(deleteNodeInABst _type)
target_link_libraries(replaceWords _type)

message(STATUS "leetcode WITH_TESTS: ${WITH_TESTS}")
if (WITH_TESTS)
  add_executable(_test tests/_test.cpp)
endif (WITH_TESTS)
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
add_test (wildcardMatchingRun wildcardMatching hello he*o)
add_test (testCPP _test.cpp)

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

