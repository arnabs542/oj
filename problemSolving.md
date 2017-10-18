# [General Problem Solving Techniques Or Approaches](https://en.wikipedia.org/wiki/Problem_solving)

## Abstraction and MODELING - solving the problem in a model of the system before applying it to the real system
Convert practical problems into mathematical/algorithmic MODELS.
For example, N Queens, Course Schedule, Word Ladder II, Integer Replacement are all problems that can be
abstracted into a graphical model.

- Monotonic(sorting) model
- Analysis model(calculus, probability distribution density, etc)
- Graph model
- Bit representation and manipulation
- Combinatoric model

## Reduce and Generalize - Transforming the problem into another problem for which solutions exist
Some problems may be so complicated that it's not easy to analyze the underlying
model with above approaches.
1. Reduce to the simplest form
2. Divide and conquer, factorize numbers
3. Make (greedy strategy) hypothesis, and prove it (by contradiction, mathematical induction...).

Then, derive the recurrence relation/state transition.

In this stage, we may ship naive solutions.

## INDUCE
Enumerate test cases/examples, and INDUCE FROM EXAMPLES. This is the reverse
process of above approach.

## Optimize From Naive Solutions
Once we figured out SIMPLEST naive brute force solutions, figure out the bottleneck in our naive
algorithm, then try to OPTIMIZE by resolving that.
1) Reduce duplicate computation with STATE TRANSITION/RECURRENCE RELATION
2) Optimize space usage with better REPRESENTATION

Remember, every problem has a naive brute force solution, regardless of complexity.

## Algorithm Brainstorm
To address a specific complexity problem, we can Hit and Try. Run through possible
solutions with specific time/space complexity, and try.

## Inspect in another perspective - Think Out of the Box

# To sum it up
In a word, model the problem, reduce and induce, then optimize.