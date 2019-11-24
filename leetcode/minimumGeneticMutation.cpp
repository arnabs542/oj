/**
 *
433. Minimum Genetic Mutation
Medium

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.


Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1


Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2


Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3


Accepted
25K
Submissions
63.2K

SOLUTION
================================================================================

A shortest path problem can be solved with breadth first search in graph.

The key here is to find neighbour vertex efficiently.


 *
 */

#include <debug.hpp>

class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        int result = minMutationBfs(start, end, bank);

        cout << start << "=>" << end << " " << bank << " " << result << endl;

        return result;
    }

    int minMutationBfs(string start, string end, vector<string>& bank) {
        int minDepth = -1;
        vector<char> chars{'A', 'T', 'C', 'G'};
        unordered_map<string, int> depthMap{make_pair(start, 0)};
        queue<string> frontier; // queue for search frontier
        unordered_set<string> bankSet(bank.begin(), bank.end());

        frontier.push(start);
        while (!frontier.empty()) {
            //queue<string> frontier1; // new frontier
            //while (!frontier.empty()) {
                const string v = frontier.front();
                frontier.pop();
                if (v == end) return depthMap[v]; // check solution
                for (int i = 0; i < 8; ++i) {
                    for (int j = 0; j < (int)chars.size(); ++j) {
                        if (chars[j] == v[i]) continue;
                        string u = v;
                        u[i] = chars[j];
                        if (bankSet.count(u) && !depthMap.count(u)) {
                            depthMap[u] = depthMap[v] + 1;
                            //if (u == end) return depthMap[u]; // check solution
                            //frontier1.push(u);
                            frontier.push(u);
                        }
                    }
                }
            //}
            //frontier = std::move(frontier1);
        }

        return minDepth;
    }
};

int test() {
    string start, end;
    vector<string> bank;
    int result = 0;

    Solution solution;

    start = "AACCGGTT";
    end = "AACCGGTT";
    bank = {};
    result = 0;
    assert(solution.minMutation(start, end, bank) == result);

    start = "AACCGGTT";
    end = "AACCGGTT";
    bank = {"AACCGGTT"};
    result = 0;
    assert(solution.minMutation(start, end, bank) == result);

    start = "AACCGGTT";
    end = "AACCGGTA";
    bank = {"AACCGGTA"};
    result = 1;
    assert(solution.minMutation(start, end, bank) == result);

    start = "AACCGGTT";
    end = "AAACGGTA";
    bank = {"AACCGGTA", "AACCGCTA", "AAACGGTA"};
    result = 2;
    assert(solution.minMutation(start, end, bank) == result);

    start = "AAAAACCC";
    end = "AACCCCCC";
    bank = {"AAAACCCC", "AAACCCCC", "AACCCCCC"};
    result = 3;
    assert(solution.minMutation(start, end, bank) == result);

    return 0;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
