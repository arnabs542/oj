/**
 *
621. Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].


==============================================================================================
SOLUTION

1. Brute force
Treat it as a GRAPH problem, at each interval, we need to choose what action to take: run some
task or being idle.

The state if the task count hash table. And the search step correspond to target intervals needed.

It shall be done with BFS or DFS, with BFS more preferably, since we're trying to find the
shortest path.

A drawback of this solution is complexity: Unnecessary duplicate search because of PERMUTATION
of tasks. For example, AB and BA are equivalent to each other but the graph search needs to
consider both of them.

2. Dynamic programming?
NO, this problem doesn't require the tasks be executed in order, actually it's only there number
of instances that matter.

3. Greedy strategy - Alternating tasks -  ordered data structure, like MAX HEAP, or bst.
The brute force solution involves many duplicates? A proper greedy strategy will simplify it.

The most simple case is when all tasks occur same times. Then we can shuffle by alternating
tasks in a sequence, in a round-robin manner.
Input: tasks = ["A","A","A","B","B","B"], n = 2
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

The point is to shuffle the tasks so that same tasks are at least n distance apart.

The tasks order doesn't matter, we can group the tasks, using a hash table <task, occurrence count>.
A greedy strategy is to assign tasks occur more frequently first.

Maintain a ordered structure containing tasks tuple (task count, task name).

1) Select the task with highest occurrence count, and pop it out from the ordered structure.
2) Repeat, until window size is n or the ordered structure is empty.
3) Construct the ordered tasks again.
4) Repeat for another cycle/round, until tasks queue is empty.

Problem: In each window, there won't be collision, how about two windows of size n?
Note that we are comparing the tasks using tuple <count, task name> so that tasks with
same occurrence count will be selected with consistent order, avoiding collision between
windows, like this: A -> B-> idle -> B -> A -> idle.

Complexity
Build heap: O(26), get top of heap: O(log26), insert: O(log26)
O(26N) = O(N)

4. Simplified implementation of above idea: count the idle slots

I have no idea......

==============================================================================================
SIMILAR QUESTIONS

http://www.geeksforgeeks.org/rearrange-a-string-so-that-all-same-characters-become-at-least-d-distance-away/


 *
 */

#include <debug.hpp>


class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int result = _leastIntervalGreedy(tasks, n);

        cout << "tasks: " << tasks << ", n: " << n << ", result: " << result << endl;

        return result;
    }

    int _leastIntervalGreedy(vector<char>& tasks, int n) {
        priority_queue<pair<int, char>> tasksPq; // tasks priority queue
        vector<pair<int, char>> tasksRemain; // remaining tasks
        unordered_map<char, int> tasksCount; // tasks number

        for (char task: tasks) {
            tasksCount[task] += 1;
        }
        for (auto e: tasksCount) {
            tasksPq.push(make_pair(e.second, e.first));
        } // A: 1, B: 1
        int result = 0;
        int k = n + 1; // window size // 1
        while (tasksPq.size()) {
            //cout << tasksPq.size() << ", " << k << endl;
            while (tasksPq.size() && k) { // A: 0, B: 1
                pair<int, char> task = tasksPq.top(); // alternate tasks in round-robin manner
                if (--task.first) {
                    tasksRemain.push_back(make_pair(task.first, task.second));
                }
                tasksPq.pop();
                --k; // 0
                ++result; // 2
            }
            // not finished yet
            if (tasksRemain.size()) {
                result += k; // insert idle // 2
                // reset state for next round
            }
            k = n + 1;
            for (auto task: tasksRemain) {
                tasksPq.push(task);
            }
            tasksRemain.clear();
        }
        return result;
    }
};

void test() {
    Solution solution;

    vector<char> tasks;
    int n = 0;
    int output = 0;

    tasks = {};
    n = 0;
    output = 0;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A'};
    n = 1;
    output = 1;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A', 'A'};
    n = 1;
    output = 3;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A', 'A'};
    n = 2;
    output = 4;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A', 'B'};
    n = 0;
    output = 2;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A', 'A', 'B'};
    n = 2;
    output = 4;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A', 'A', 'B', 'C'};
    n = 2;
    output = 4;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A', 'A', 'B', 'C', 'D'};
    n = 2;
    output = 5;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A', 'A', 'A', 'B', 'C', 'D'};
    n = 2;
    output = 7;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A', 'A', 'A', 'B', 'C', 'C', 'D'};
    n = 2;
    output = 7;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A','A','A','B','B','B'};
    n = 0;
    output = 6;
    assert(solution.leastInterval(tasks, n) == output);
    tasks = {'A','A','A','B','B','B'};
    n = 2;
    output = 8;
    assert(solution.leastInterval(tasks, n) == output);

    tasks = {'A','A','A','B','C','D'};
    n = 2;
    output = 8;

    cout << "self test passed!" << endl;

}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
