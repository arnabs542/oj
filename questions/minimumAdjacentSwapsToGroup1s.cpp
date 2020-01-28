/**
 *
 * Given an array containing only 0s and 1s, what's the minimum swaps to groups 1s together?
 * Only adjacent elements can be swapped every time.
 *
 * Reference:
 * Given an array of 0 and 1, find minimum no. of swaps to bring all 1s together (only adjacent swaps allowed).
 * https://stackoverflow.com/questions/38748760/given-an-array-of-0-and-1-find-minimum-no-of-swaps-to-bring-all-1s-together-o
 *
 * Examples:
 * 10001 => 3
 * 1 => 0
 * 0 => 0
 * 0010010001 => 5
 * 0101010101 => 5
 *
 * SOLUTION
 * ===============================================================================
 *
 * First UNDERSTAND AND EXPLOIT THE PROCESS BY COMING UP WITH A BRUTE FORCE SOLUTION.
 *
 * 1. Brute force - count 0s with prefix sum - exhaust all possible center
 *
 * How to group 1s together? We can find a center index c, and move 1s towards it by
 * swapping.
 *
 * For each index i containing 1, how many swaps are needed to to move it
 * to the destination so that 1s are together?
 * It's the number of 0s between center and source index i.
 * To query count number occurrences, we can build a prefix sum array for range sum query.
 *
 * Mathematical objective - L1 norm
 * --------------------------------------------------------------------------------
 *     argmin_c{Σ_i{count of 0s between i and c, inclusively}},
 * where i is in [0, n-1], and nums[i] = 1.
 * We need to find such index c to minimize the summing result.
 *
 * How to determine such center c?
 * We can brute force iterate all possible indices(indices of 0s can be skipped, easily).
 *
 * -------------------------------------------------------------------------------
 * Also it can be transformed into a MATHEMATICAL MODEL:
 * Given m points(m-1 distances) in a line represented by an array p, find a
 * such point c that sum of distances to c, Σ_i(abs(distance(c, i))) is minimized,
 * where i is in [0, m-1], and distance(c, i) corresponds to prefix sum difference,
 * indicting number of 0s between c and i.
 *
 * It's equivalent to the problem:
 * Given an increasing array arr, find such index c that f=Σ_i(abs(arr[i]-arr[c]))
 * is minimized, where i in [0, n-1].
 *
 * If objective function is sum of squares, f = Σ_i(arr[i]-arr[c])²,
 * the solution is the mean value.
 * Now it's sum of absolute deviation, the solution is the median?
 *
 * Refer to: https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-l-1-norm
 *
 * The MEDIAN MINIMIZES THE SUM OF ABSOLUTE DEVIATIONS(L1 norm)
 *
 * Objective:
 *     \arg \min_{x} \sum_{i = 1}^{N} \left| {s}_{i} - x \right|
 * Note:
 *     \frac{\mathrm{d} \left | x \right | }{\mathrm{d} x} = \operatorname{sign} \left( x \right)
 * (Being more rigorous would say it is a Sub Gradient of the non smooth 𝐿1 Norm function)
 * Taking the derivative:
 *     \sum_{i = 1}^{N} \operatorname{sign} \left( {s}_{i} - x \right)
 * This equals to zero only when the number of positive items equals the number of negative which happens when x=median{s1,s2,⋯,s𝑁}
 *
 * -------------------------------------------------------------------------------
 * Second REDUCE TO THE SIMPLEST FORM AND DERIVE PATTERNS, RECURRENCE OR GREEDY.
 *
 * 0 1s in the array: output 0
 * 1 1s in the array: output 0
 * 2 1s in the array: j - i - 1, number of 0s between two 1s. Center: any c in [i, j].
 * 3 1s in the array(i, j, k): (j-i-1)+(k-j-1)=(k-i-2). Center: j
 * Why the center j is the middle/median one?
 * Well this is a mathematical model: sum of segment lengths in geometry!
 * The intuition is the choose a middle point as center.
 *
 * 2. Count as sum with prefix sum range sum query - MEDIAN position as center
 * Collect all indices of 1s into a list, and choose the median index as center index c.
 *
 * Complexity: O(N)
 *
 *
 */

#include <debug.hpp>

class Solution {
public:
	int minSwaps(vector<int> &nums) {
		int result = 0;

		//result = minSwapsPrefixSumBruteForce(nums);
		result = minSwapsPrefixSumMedianAsCenter(nums);

		cout << nums << " " << result << endl;

		return result;
	}

	int minSwapsPrefixSumBruteForce(vector<int> &nums) {
		const int n = nums.size();
		vector<int> ps(n + 1, 0); // prefix sum, count number of 0s, [0, n]
		for (int i = 1; i <= n; ++i) ps[i] = ps[i-1] + (nums[i-1] == 0);

		int result = std::numeric_limits<int>::max(); // XXX: initialization and corner case

		if (ps[n] == 0 || ps[n] == n) return 0; // all 0s or all 1s
		for (int i = 0; i < n; ++i) { // exhaust all center points
			int nSwaps = 0;
			if (nums[i] == 0) continue; // XXX: larger nSwaps for nums[i]==0, but will affect final answer.
			for (int j = 0; j < n; ++j) {
				if (nums[j] == 0) continue;
				if (i < j) {
					nSwaps += ps[j+1] - ps[i]; // [i, j]
				} else if (i > j) {
					nSwaps += ps[i+1] - ps[j]; // [i, j]
				}
			}
			result = min(result, nSwaps);
		}

		return result;
	}

	int minSwapsPrefixSumMedianAsCenter(vector<int> &nums) {
		int n = nums.size();
		vector<int> ps(n + 1, 0); // prefix sum, count number of 0s, [0, n]
		for (int i = 1; i <= n; ++i) ps[i] = ps[i-1] + (nums[i-1] == 0);

		vector<int> indices; // indices of 1s
		for (int i = 0; i < n; ++i) {
			if (nums[i] == 1) indices.push_back(i);
		}
		if (indices.empty()) return 0; // all 0s
		int center = indices[indices.size() / 2];

		int result = std::numeric_limits<int>::max();
		int i = center;
		{ // exhaust all center points
			int nSwaps = 0;
			for (int j = 0; j < n; ++j) {
				if (nums[j] == 0) continue;
				if (i < j) {
					nSwaps += ps[j+1] - ps[i]; // [i, j]
				} else if (i > j) {
					nSwaps += ps[i+1] - ps[j]; // [i, j]
				}
			}
			result = min(result, nSwaps);
		}

		return result;
	}
};

int test() {

	Solution solution;

	vector<int> nums;
	int output;

	nums = {};
	output = 0;
	assert(solution.minSwaps(nums) == output);

	nums = {0};
	output = 0;
	assert(solution.minSwaps(nums) == output);

	nums = {1};
	output = 0;
	assert(solution.minSwaps(nums) == output);

	nums = {1, 0, 1};
	output = 1;
	assert(solution.minSwaps(nums) == output);

	nums = {1,1,0,0,0,0,0,1};
	output = 5;
	assert(solution.minSwaps(nums) == output);

	cout << "test passed" << endl;
	return 0;
}

int main(int argc, char **argv) {
	test();

	return 0;
}
