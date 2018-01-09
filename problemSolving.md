# [General Problem Solving Approaches and Techniques](https://en.wikipedia.org/wiki/Problem_solving)
Problems you have never heard before may be hard to solve, so fact it, embrace it!

TAKE THE CHALLENGE!

## Examplify and INDUCE
Enumerate test cases/examples, to understand the problem, and maybe INDUCTIVELY REASON FROM EXAMPLES.

Backward induction.

## Abstraction and MODELING - solving the problem in a model of the system before applying it to the real system

### Observe, State, Model
Observe the problem in different PERSPECTIVES, then different STATES will be tracked, and different MODELS apply!

Convert practical problems into mathematical/algorithmic MODELS.
For example, N Queens, Course Schedule, Word Ladder II, Integer Replacement are all problems that can be
abstracted into a graphical model.

### General Models
- Counting model: hash count, count as sum
- Sorting model: sorting algorithms, augmented BST with rank, monotonic analysis
    - Order statistics
- Pointers model: two pointers, ...
- Prefix or suffix
- Partition
- Data structures: array, buckets, linked list, stack and queue, trees, graphs, ...
    - Linear: array, linked list, stack, queue(deque), priority queue, 
    - Associative/mapping: hash table, buckets, inverted index
    - tree: (balanced)binary search tree, kd-tree, range query tree, implicit representation of heap
    - Range query: segment tree, binary indexed tree
    - graph
- GRAPH model: multiple branches, many to many connections
    - Depth first search: all paths, one path, backtracking
    - Breadth first search: all paths, shortest path, bidirectional search, backtracking with copies of state 
    - Union find: connected components
- STATE TRANSITION RECURRENCE RELATION
    - Sequential recurrence relation
        - Backward induction
        - DYNAMIC PROGRAMMING
        - STATE MACHINE
        - Greedy strategy
    - Partition recurrence relation
        - Dynamic programming: overlapping subproblems
        - divide and conquer: partition into disjoint subproblems
        - Greedy strategy
    - Sliding window recurrence relation: offset and stride
- STATE REPRESENTATION: Bitwise,
- Mathematical analysis model
    - Order
    - Equality: Interval or ranges
    - Calculus: change rate
        - integration
        - differentiation
        - Monotonicity analysis: max/min function, prefix sum
        - Extrema points analysis: often related to monotonic stacks and queues
    - combinatorics
        - PERMUTATION
        - COMBINATION
        - CARTESIAN PRODUCT
    - probability: pdf, cdf, pmf, ...

Try to exploit the problem in approaches like:
- Change PERSPECTIVES: backward induction, ...
- Domain and range 
- Treat it as another model of problem
- Differentiation and integral (prefix sum)
- Analysis model(calculus, probability distribution density, etc)
- Combinatoric model

Refer to sections for more.

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

#### Stack

#### Prefix sum 
This linear data structure contains F(x) where F(x) is integral of f(x) given by another array.

Query: O(1)
Range Sum query: O(1)
Update: O(n)
Delete: O(n)

#### Bucket

Tree data structure - special graph with only tree edges
===================
The core idea of tree is divide and conquer: structure data in properly partitioned spaces.

#### Aspects of trees
- General tree search: preorder, inorder, postorder, level order.
- Tree degrees

#### Heap
Tree structure with implicit data structure: array.

#### Binary search tree

#### Balanced binary search tree

#### Segment tree - range query

#### Binary indexed tree - range query
A tree structure dealing with prefix sum.

#### Disjoint set


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

### Optimization directions
- Brute force method: GRAPH SEARCH, naive count
- Avoid duplicate computation: order invariant, overlapping subproblem
    - Solve it by brute force permutation:  O(P(n, k)), special case is O(P(n, n)) = O(n!).
    - Reduce PERMUTATION to COMBINATION (SUBSETS) by RESTRICTING ORDER (ORDER INVARIANT), \sum_k{P(n, k)} -> \sum_k{C(n, k)} = 2ⁿ, or O(n!) -> O(C(n, k))
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
    - Define state that's TRACTABLE
    - Augment/ADD STATE by another dimension of if current dimensions are insufficient

For example, refer to "course schedule III", "knapsack problems". In 0-1 knapsack problem, 
items have different cost(weight) and gain(value), so it should be solved with dynamic programming.
But if each item have same cost, then it can be done with greedy strategy to maximize sum of gain.

## To analyze a problem, the key is to DEFINE STATE that exploits the problem structure!

## Reduce and Generalize - Transforming the problem into another problem for which solutions exist
Some problems may be so complicated that it's not easy to analyze the underlying
model with above approaches.
1. Reduce to the simpler form: divide and conquer, or to its simplest form
2. Find solution for simpler form
3. Make (greedy strategy) hypothesis, and prove it (by contradiction, mathematical induction...), and/or
4. Derive the RECURRENCE RELATION/STATE TRANSITION.

In this stage, we may ship naive solutions.

## BRAINSTORM
When having no clue, BRAINSTORM.

Run algorithm brainstorm.
Exhaust all possible decisions.

To address a specific complexity problem, we can Hit and Try. Run through possible
solutions with specific time/space complexity, and try.

## Inspect in another perspective - Think Out of the Box

## To sum it up
In general APPROACH is to examplify and optimize from naive solution. 
To ANALYZE the problem, MODEL it, REDUCE and INDUCE.


## General bugs in code
- off-by-one bug
- edge case failure
- using 'if' instead of expected loop should be used
- missing TAIL INCREMENT STATEMENT in iteration
- wrong order of statements of assigning values
- missing bound check while incrementing 

