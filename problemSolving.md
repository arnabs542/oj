# [General Problem Solving Techniques Or Approaches](https://en.wikipedia.org/wiki/Problem_solving)

## Abstraction and MODELING - solving the problem in a model of the system before applying it to the real system
Convert practical problems into mathematical/algorithmic MODELS. 
For example, N Queens, Course Schedule, Word Ladder II, Integer Replacement are all problems that can be
abstracted into a graphical model.

1. Monotonic(sorting) model
2. Graph model
3. Bit representation and manipulation
4. Combinatoric model

## INDUCE
Enumerate test cases/examples, and INDUCE FROM EXAMPLES. This is the reverse
process of above approach.

## Reduce and Generalize - Transforming the problem into another problem for which solutions exist
Some problems may be so complicated that it's not easy to analyze the underlying
model with above approaches.
1. Reduce to the simplest form
2. Divide and conquer, factorize numbers
3. Make (greedy strategy) hypothesis, and prove it (by contradiction, mathematical induction...).

Then, derive the recurrence relation/state transition.

In this stage, we may ship naive solutions.

## Optimize From Naive Solutions
Once we figured out naive solutions, figure out the bottleneck in our naive
algorithm, then try to OPTIMIZE by resolving that.
1) Reduce duplicate computation with STATE TRANSITION/RECURRENCE RELATION
2) Optimize space usage with better REPRESENTATION

## Algorithm Brainstorm
To address a specific complexity problem, we can Hit and Try. Run through possible
solutions with specific time/space complexity, and try.

## Inspect in another perspective - Think Out of the Box
