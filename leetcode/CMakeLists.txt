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
add_executable(179.largestNumber 179.largestNumber.cpp)
add_executable(1140.stoneGameII 1140.stoneGameII.cpp)
add_executable(1292.maximumSideLengthOfASquareWithSumLessThanOrEqualToThreshold 1292.maximumSideLengthOfASquareWithSumLessThanOrEqualToThreshold.cpp)
#add_executable(160.intersectionOfTwoLinkedLists 160.intersectionOfTwoLinkedLists.cpp)
add_executable(215.kthLargestElementInAnArray 215.kthLargestElementInAnArray.cpp)
add_executable(224.basicCalculator 224.basicCalculator.cpp)
add_executable(253.meetingRoomsII 253.meetingRoomsII.cpp)
add_executable(266.palindromePermutataion 266.palindromePermutation.cpp)
add_executable(267.palindromePermutataionII 267.palindromePermutationII.cpp)
add_executable(280.wiggleSort 280.wiggleSort.cpp)
add_executable(282.expressionAddOperators 282.expressionAddOperators.cpp)
add_executable(295.findMedianFromDataStream 295.findMedianFromDataStream.cpp)
add_executable(31.nextPermutation 31.nextPermutation.cpp)
add_executable(310.minimumHeightTrees 310.minimumHeightTrees.cpp)
#add_executable(311.sparseMatrixMultiplication 311.sparseMatrixMultiplication.cpp)
add_executable(327.countOfRangeSum 327.countOfRangeSum.cpp)
add_executable(33.searchRotatedSortedArray 33.searchRotatedSortedArray.cpp)
add_executable(331.verifyPreorderSerializationOfABinaryTree 331.verifyPreorderSerializationOfABinaryTree.cpp)
add_executable(347.topKFrequentElements 347.topKFrequentElements.cpp)
add_executable(359.loggerRateLimiter 359.loggerRateLimiter.cpp)
add_executable(363.maxSumOfRectangleNoLargerThanK 363.maxSumOfRectangleNoLargerThanK.cpp)
add_executable(427.constructQuadTree 427.constructQuadTree.cpp)
add_executable(429.NaryTreeLevelOrderTraversal 429.NaryTreeLevelOrderTraversal.cpp)
add_executable(432.allOoneDataStructure 432.allOoneDataStructure.cpp)
add_executable(433.minimumGeneticMutation 433.minimumGeneticMutation.cpp)
add_executable(44.wildcardMatching 44.wildcardMatching.cpp)
add_executable(443.stringCompression 443.stringCompression.cpp)
add_executable(450.deleteNodeInABst 450.deleteNodeInABst.cpp)
add_executable(457.circularArrayLoop 457.circularArrayLoop.cpp)
add_executable(458.poorPigs 458.poorPigs.cpp)
add_executable(460.lfuCache 460.lfuCache.cpp)
add_executable(473.matchsticksToSquare 473.matchsticksToSquare.cpp)
add_executable(474.onesAndZeroes 474.onesAndZeroes.cpp)
add_executable(475.heaters 475.heaters.cpp)
add_executable(477.totalHammingDistance 477.totalHammingDistance.cpp)
add_executable(478.generateRandomPointInACircle 478.generateRandomPointInACircle.cpp)
add_executable(480.slidingWindowMedian 480.slidingWindowMedian.cpp)
add_executable(481.magicalString 481.magicalString.cpp)
add_executable(482.licenseKeyFormatting 482.licenseKeyFormatting.cpp)
add_executable(485.maxConsecutiveOnes 485.maxConsecutiveOnes.cpp)
add_executable(5.longestPalindromicSubstring 5.longestPalindromicSubstring.cpp)
add_executable(54.spiralMatrix 54.spiralMatrix.cpp)
add_executable(507.perfectNumber 507.perfectNumber.cpp)
add_executable(523.continuousSubarraySum 523.continuousSubarraySum.cpp)
add_executable(528.randomPickWithWeight 528.randomPickWithWeight.cpp)
#add_executable(568.maximumVacationDays 568.maximumVacationDays.cpp)
add_executable(591.tagValidator 591.tagValidator.cpp)
add_executable(621.taskScheduler 621.taskScheduler.cpp)
add_executable(647.palindromicSubstrings 647.palindromicSubstrings.cpp)
add_executable(648.replaceWords 648.replaceWords.cpp)
add_executable(676.implementMagicDictionary 676.implementMagicDictionary.cpp)
add_executable(743.networkDelayTime 743.networkDelayTime.cpp)
add_executable(753.crackingTheSafe 753.crackingTheSafe.cpp)
add_executable(768.maxChunksToMakeSortedII 768.maxChunksToMakeSortedII.cpp)
add_executable(769.maxChunksToMakeSorted 769.maxChunksToMakeSorted.cpp)
add_executable(774.minimizeMaxDistanceToGasStation 774.minimizeMaxDistanceToGasStation.cpp)
add_executable(787.cheapestFlightsWithinKStops 787.cheapestFlightsWithinKStops.cpp)
add_executable(802.findEventualSafeStates 802.findEventualSafeStates.cpp)
add_executable(812.largestTriangleArea 812.largestTriangleArea.cpp)
add_executable(835.imageOverlap 835.imageOverlap.cpp)
add_executable(877.stoneGame 877.stoneGame.cpp)
add_executable(932.beautifulArray 932.beautifulArray.cpp)
#add_executable(binaryTreePreorderTraversal binaryTreePreorderTraversal.cpp)
add_executable(canIWin canIWin.cpp)
#add_executable(conv conv.cpp)
add_executable(138.copyListWithRandomPointer 138.copyListWithRandomPointer.cpp)
add_executable(divide divide.cpp)
add_executable(implementRand10UsingRand7 implementRand10UsingRand7.cpp)
add_executable(implementTriePrefixTree implementTriePrefixTree.cpp)
add_executable(insertionSortList insertionSortList.cpp)
add_executable(longestPalindromicSubsequence longestPalindromicSubsequence.cpp)
add_executable(maxConsecutiveOnesII maxConsecutiveOnesII.cpp)
add_executable(maxConsecutiveOnesIII maxConsecutiveOnesIII.cpp)
#add_executable(maxPoints-anchor-hash maxPoints-anchor-hash.cpp)
add_executable(maximumXOROfTwoNumbersInAnArray maximumXOROfTwoNumbersInAnArray.cpp)
add_executable(meetingRooms meetingRooms.cpp)
#add_executable(mergeTwoSortedLists mergeTwoSortedLists.cpp)
add_executable(minimumWindowString minimumWindowString.cpp)
#add_executable(optimalAccountBalancing optimalAccountBalancing.cpp)
add_executable(partitionPalindromeII-zhaohongze partitionPalindromeII-zhaohongze.cpp)
add_executable(regularExpressionMatching regularExpressionMatching.cpp)
add_executable(reverseWordsInAString reverseWordsInAString.cpp)
#add_executable(sentenceSimilarity sentenceSimilarity.cpp)
#add_executable(sentenceSimilarityII sentenceSimilarityII.cpp)
add_executable(297.serializeAndDeserializeBinaryTree 297.serializeAndDeserializeBinaryTree.cpp)
#add_executable(shortestCommonSupersequence shortestCommonSupersequence.cpp)
add_executable(sortslist sortslist.cpp)
add_executable(sumOfTwoIntegers sumOfTwoIntegers.cpp)
#add_executable(tests tests.cpp)

add_library(_type SHARED _type.cpp _tree.cpp _trieTree.cpp)
add_library(160.intersectionOfTwoLinkedLists SHARED 160.intersectionOfTwoLinkedLists.cpp)
add_library(maxPoints-anchor-hash SHARED maxPoints-anchor-hash.cpp)


# TEST
#add_executable(testTree tests/test_tree.cpp)
#add_executable(testTrie tests/test_trie.cpp)
#target_link_libraries(testTree _type)
#target_link_libraries(testTrie _type)
target_link_libraries(450.deleteNodeInABst _type)
target_link_libraries(648.replaceWords _type)

message(STATUS "leetcode WITH_TESTS: ${WITH_TESTS}")
if (WITH_TESTS)
  #add_executable(_test tests/_test.cpp)
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

