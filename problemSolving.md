# [General Problem Solving Approaches and Techniques](https://en.wikipedia.org/wiki/Problem_solving)
Problems you have never heard before may be hard to solve, so fact it, embrace it!

TAKE THE CHALLENGE!

## Examplify and INDUCE
Enumerate test cases/examples, to understand the problem, and maybe INDUCTIVELY REASON FROM EXAMPLES.

Backward induction.

## Abstraction and MODELING - solving the problem in a model of the system before applying it to the real system
Convert practical problems into mathematical/algorithmic MODELS.
For example, N Queens, Course Schedule, Word Ladder II, Integer Replacement are all problems that can be
abstracted into a graphical model.

General models:
- Counting model
- Sorting model: monotonic model
- Pointers model: two pointers, quick sort partition, ...
- Data structures: linked list, stack and queue, trees, graphs, ...
- GRAPH SEARCH model
- RECURRENCE RELATION / STATE TRANSITION: Divide and conquer, STATE MACHINE, Backward induction
- STATE REPRESENTATION: Bitwise, 

Try to exploit the problem in approaches like:
- Change PERSPECTIVES 
- Domain and range 
- Treat it as another model of problem
- Differentiation and integral (prefix sum)
- Analysis model(calculus, probability distribution density, etc)
- Combinatoric model

Refer to sections for more.

## Optimize From naive, brute force Solutions
When in doubt, use brute force.

Once we figured out SIMPLEST naive brute force solutions, figure out the bottleneck in our naive
algorithm, then try to OPTIMIZE by resolving that.
2) Optimize space usage with better REPRESENTATION

Remember, every problem has a naive brute force solution, regardless of complexity.

General optimization directions:
- Brute force method: GRAPH SEARCH, naive count
- Optimization directions:
    - Avoid unnecessary computation: GREEDY STRATEGY
    - Avoid duplicate computation
        - Space time trade off: Cache, dynamic programming
    - Enable efficient DATA REPRESENTATION with 
        - DATA STRUCTURE
        - Data representation
            - bit representation: bitmap
            - bit operation: XOR
            - modulo
            - arithmetic 
    - Refine STATE we are tracking to use STATE TRANSITION/RECURRENCE RELATION

## To analyze a problem, the key is to DEFINE STATE that exploits the problem structure!

## Reduce and Generalize - Transforming the problem into another problem for which solutions exist
Some problems may be so complicated that it's not easy to analyze the underlying
model with above approaches.
1. Reduce to the simpler form: divide and conquer, or to its simplest form
2. Find solution for simpler form
3. Make (greedy strategy) hypothesis, and prove it (by contradiction, mathematical induction...), and/or
4. Derive the RECURRENCE RELATION/STATE TRANSITION.

In this stage, we may ship naive solutions.

## Algorithm BRAINSTORM
When having no clue, BRAINSTORM.

To address a specific complexity problem, we can Hit and Try. Run through possible
solutions with specific time/space complexity, and try.

## Inspect in another perspective - Think Out of the Box

# To sum it up
In general APPROACH is to examplify and optimize from naive solution. 
To ANALYZE the problem, MODEL it, REDUCE and INDUCE.

# Common models for different kind of problems

## Basic data structures
- Bit representation or binary bit perspective
- Array
- Ordering sequence
- Hash table: hash count, 
- Two pointers: fast and slow pointers
- Buckets
- ...
- Tree
- Graph
- State Machine

### Linear data structure

Algorithms operating on linear data structure:
- Sort: bubble sort, quick sort, merge sort, bucket sort, radix sort...
- Count
- Two Pointers: fast and slow pointers
- Prefix sum
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

### Tree data structure

#### Aspects of trees
General tree search: preorder, inorder, postorder, level order.
Tree degrees

#### Heap
Tree structure with implicit data structure: array.

#### Binary search tree

#### Balanced binary search tree

#### Segment tree

#### Binary indexed tree
A tree structure dealing with prefix sum.

#### Disjoint set


## Analytical models
- Calculus: Differentiation and integral(prefix sum array, difference array)
- Probability distribution
- Number theory
- Binary search

