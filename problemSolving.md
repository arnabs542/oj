# Problem Solving Approaches and Techniques
Problems you have never heard before may be hard to solve, so fact it, embrace it!

TAKE THE CHALLENGE!

### Examplify and INDUCE
Enumerate test cases/examples, to understand the problem, and maybe INDUCTIVELY REASON FROM EXAMPLES.

### Abstraction and MODELING - convert a problem into a model

#### Observe, State, Model
Observe the problem in different PERSPECTIVES, then different STATES will be tracked, and different MODELS apply!

Convert practical problems into mathematical/algorithmic MODELS.
For example, N Queens, Course Schedule, Word Ladder II, Integer Replacement are all problems that can be
abstracted into a graphical model.

#### General Mathematical Models
- Equality: Interval or ranges
- Binary representation: bitwise identities, manipulation
- Modulo operation: modulo can contain two information: a, r = div(n, b)
- Counting model
    - exhaust and find occurrence: O(n) time, O(1) space
    - hash count: O(n) time/space
    - count as sum: range sum query...
    - all condition converted maximum or minimum
- Ordering model
    - Sorting algorithms
        - brute force: bubble sort, insert sort
        - bucket: bucket sort
        - divide and conquer: quick sort, quick select partitioning, merge sort
        - tree: bst, heap
        - lexicographical sort: prefix tree, radix sort
    - Ordered data structure: augmented BST with rank
    - Monotonic analysis
    - Order statistics
- Substring and subsequence
    - Prefix or suffix
    - string searching: brute force, finite automate, kmp, rolling hash, trie?
    - longest common substring: brute force, dynamic programming(locally optimal ending here), suffix tree
    - longest common subsequence: dynamic programming(locally optimal within bound)
    - longest repeated substring
    - palindrome substring: brute force, dynamic programming 2D(locally optimal within bound of interval)
    - regular expression: dynamic programming, backtracking(dfs), finite automate
- Partition model
    - Pointers partition: quick sort partition, three way partition(dnf), divide and conquer
    - Binary split: binary search tree, segment tree
    - Exponential split: binary indexed tree
- Calculus: change rate
    - integration: cumulative function
    - differentiation: difference array
    - Monotonicity analysis(单调性): max/min function, cumulative sum/prefix sum
        - Binary search
        - Sliding window
        - monotone stack or monotone queue
    - Extrema points analysis: often related to monotonic stacks and queues
- combinatorics
    - PERMUTATION
    - COMBINATION: permutation without order
    - CARTESIAN PRODUCT
- probability: pdf, cdf, pmf, ...
    - joint, marginal, conditional probability


Data structures
- Data structures: array, buckets, linked list, stack and queue, trees, graphs, ...
    - Linear: array, linked list, stack, queue(deque), priority queue, double ended queue
        - Stack: FILO(First In Last Out). Backward processing, priority, monotonicity, depth first search.
        - Queue: FIFO(First In First Out). Breadth first search frontier.
    - Associative/mapping: hash table, buckets, inverted index
    - Tree: undirected ACYCLIC GRAPH, has RECURSIVE structure
        - (self-balancing)binary search tree, augmented self-balancing bst
        - Range query: segment tree, binary indexed tree
        - prefix tree(trie): suffix tree, bitwise prefix tree
        - kd-tree
        - implicit array representation of heap
        - Augment tree: order statistics tree, tree node contains number of child
    - Graph: vertexes and edges/connections
        - Characteristics: multiple branches, many to many connections
        - Algorithm
            - Depth first search: all paths, one path, backtracking
            - Breadth first search: all paths, shortest path, bidirectional search, backtracking with copies of state 
            - Union find: connected components
            - Cycle detection: dfs, bfs, tortoise and hare

State transition technique
- STATE TRANSITION - the key is to model the problem and define proper state
    - state representation - PERSPECTIVE matters!
        - single variable state
            - integers: target number,
            - bits
            - string
        - interval state
            - Two ended interval state:
            - One ended interval state: optimal solution ending here(kmp, maximum subarray, covered range)
        - combinatorial state
            - sets state: vertices, edges, 
            - combination
            - permutation (most complex)
    - state definition
        - optimal solution so far (keep track of globally optimal so far)
        - optimal solution ending here: window, string problem
        - optimal solution within range: sequence problem
    - state transition technique 
        - STATE MACHINE
            - Deterministic finite automata(DFA)
            - Nondeterministic finite automata(NFA: regular expression, ...)
        -  RECURRENCE RELATION(递推关系)
            - Divide and conquer: partition into disjoint subproblems
            - Backward induction
            - DYNAMIC PROGRAMMING: overlapping subproblems
                - f(n): optimal solution of substructure ending here
                - f(p, q): optimal solution of substructure within range (p, q)
            - Greedy strategy
                - monotonic stack/queue
                - heap
    - state transition form
        - Sequential recurrence relation: one end dimensional dynamic programming
        - Partition recurrence relation: divide and conquer, two ends dynamic programming
        - Sliding window recurrence relation: offset and stride
        - Monotonic stack/queue

Try to exploit the problem in approaches like:
- Change PERSPECTIVES: backward induction, ...
- Domain and range 
- Treat it as another model of problem
- Differentiation and integral (prefix sum)
- Analysis model(calculus, probability distribution density, etc)
- Combinatoric model

Refer to sections for more.

A powerful idea is to trade space for time with state transition recurrence relation.

### Common models for different kind of problems

Basic data structures
=====================

- Bit representation or binary bit perspective
- Array
- Ordering sequence
- Hash table: hash count, 
- Buckets: optimization for hash table, but with defined domain
- Two pointers: fast and slow pointers
- ...
- Tree
- Graph
- State Machine

### Linear data structure

Algorithms operating on linear data structure:
- Count
- Sort: bubble sort, quick sort, merge sort, bucket sort, radix sort...
- Two Pointers: fast and slow pointers
- Prefix sum
- bucket: range within domain
- cycle detection: range within domain
- Bit
    - bit representation
    - bit manipulation
    - bit-wise perspective

#### Array - implementation
Query: O(1)
Update: O(1)
Delete: O(n)

#### Linked list - implementation
Query: O(n)
Update: O(n)
Delete: O(1) at both ends, O(n) on average.

#### Queue 
First In First Out data structure.

Applicable scenarios:
- Breadth first search

#### Stack
First In Last Out data structure.

Applicable scenarios:
- Depth first search
- Reverse problem
- Nested structure
- Monotonic/monotone sequence

#### Prefix sum 
This linear data structure contains F(x) where F(x) is integral of f(x) given by another array.

Query: O(1)
Range Sum query: O(1)
Update: O(n)
Delete: O(n)

#### Bucket

#### Tree data structure - special graph with only tree edges - graph without cycle!
The core idea of tree is divide and conquer: structure data in properly partitioned spaces.

Traversal:
- dfs(N)
    - preorder: NLH
    - inorder: LNH
    - postorder: LHN
- bfs

##### Aspects of trees
- General tree search: preorder, inorder, postorder, level order.
- Tree degrees

##### Heap
Tree structure with implicit data structure: array.

##### Binary search tree

##### Self balancing binary search tree
- Red black tree
- AVL tree
- Order statistics tree

##### Segment tree - range query

##### Binary indexed tree - range query
A tree structure dealing with prefix sum.
- Get last significant bit 1 mask(x) = x & (-x)
- parent(x) = x - (x&-x) = x & (x-1), removing least significant bit 1
- update sibling(x) = x + (x&-x), adding least significant bit 1

2D binary indexed tree: Cartesian product of 1d binary indexed tree.
Complexity: O(MNlog(M+N))

#### Prefix tree
- string prefix tree(trie)
- bitwise trie
- suffix tree: build a trie with suffixes

Optimization:
- compression


#### Disjoint set
- union(u, v)
- find(v)

Optimization:
- compression


### Analytical models
- Calculus: Differentiation and integral(prefix sum array, difference array)
- Probability distribution
- Number theory
- Binary search

## Optimize From naive, brute force Solutions
When in doubt, use brute force.

Once we figured out SIMPLEST naive brute force solutions, figure out the bottleneck in our naive
algorithm, then try to OPTIMIZE by resolving that.
2) Optimize space usage with better REPRESENTATION

Remember, every problem has a naive brute force solution, regardless of complexity.

#### Optimization directions
- Brute force method: GRAPH SEARCH(permutation, combination subsets), naive count
- Avoid duplicate computation: order invariant, overlapping subproblem
    - Solve it by brute force permutation:  O(P(n, k)), special case is O(P(n, n)) = O(n!).
    - Reduce PERMUTATION to COMBINATION (SUBSETS) by RESTRICTING ORDER (ORDER INVARIANT) or memoization, \sum_k{P(n, k)} -> \sum_k{C(n, k)} = 2ⁿ, or O(n!) -> O(C(n, k))
    - Reduce COMBINATION (SUBSETS) to CARTESIAN PRODUCT by eliminate OVERLAPPING subproblem: C(n, k) -> polynomial(n): O(2ⁿ) -> O(n^k)
        - Space time trade off: MEMOIZE
            - Collection data structure not easy to hash
                - Convert to string
                - Alternative state representation: ordered integer indices, ranges or intervals
        - Recurrence relation
    - Reduce COMBINATION or CARTESIAN PRODUCT STATE to RANGE STATE: states in different search branches form a contiguous interval
    - Divide and conquer: reduce combination complexity to log, O(n) -> O(logn)
- Avoid unnecessary computation: GREEDY STRATEGY
    - Greedy strategy: reduce dynamic programming to greedy strategy if items share same gain 
        - Order related
        - Maximum/minimum: heap data structure, ...
- Efficient DATA REPRESENTATION 
    - DATA STRUCTURE
    - Data representation
        - bit representation: bitmap
        - bit operation: XOR
        - modulo
        - arithmetic 
- Refine STATE we are tracking to use STATE TRANSITION/RECURRENCE RELATION
    - Define state that WON'T LOSE INFORMATION for state transition function
    - Use range state if discrete states form a continuous interval 
    - Define state that's TRACTABLE
    - Augment/ADD STATE by another dimension of if current dimensions are insufficient

For example, refer to "course schedule III", "knapsack problems". In 0-1 knapsack problem, 
items have different cost(weight) and gain(value), so it should be solved with dynamic programming.
But if each item have same cost, then it can be done with greedy strategy to maximize sum of gain.

### To analyze a problem, the key is to DEFINE STATE that exploits the problem structure!

### Reduce and Generalize - Transforming the problem into another problem for which solutions exist
Some problems may be so complicated that it's not easy to analyze the underlying
model with above approaches.
1. Reduce to the simpler form: divide and conquer, or to its simplest form
2. Find solution for simpler form
3. Make (greedy strategy) hypothesis, and prove it (by contradiction, mathematical induction...), and/or
4. Derive the RECURRENCE RELATION/STATE TRANSITION.

In this stage, we may ship naive solutions.

### Brainstorm
When having no clue, BRAINSTORM.

Run algorithm brainstorm.
Exhaust all possible decisions.

To address a specific complexity problem, we can Hit and Try. Run through possible
solutions with specific time/space complexity, and try.

### Inspect in another perspective - Think Out of the Box
...

### To sum it up
Examplify and optimize from naive solution by ANALYZING, MODELING, REDUCING and INDUCING the problem.


# General bugs in code
- off-by-one bug
- edge case failure
- using 'if' instead of expected loop should be used
- missing TAIL INCREMENT STATEMENT in iteration
- wrong order of statements of assigning values
- missing bound check while incrementing 
- Multithreaded
    - Exception causes sub-thread to exit without core dump
    - illegal memory writes(dangling reference/pointer)
    - data race

# How to debug code
- Run it under difference scenarios(in your thinking)!

# How to read code
- Read the *STATE/DATA* representation, layout, concurrent logic
- Keep track *variables*(core state): input arguments, return result, etc. Don't read line by line all the time.
- Understand how data is manipulated, transferred between functions, threads
- The same way as debugging it: run the code in different scenarios from simple to complex one, in your thinking!
