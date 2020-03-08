# Tips on white board coding or paper coding

## Ask questions to CLARIFY
- How is input data REPRESENTATION?
- How big is the SIZE of the input?
- What is the RANGE of values? Positive values or negative values?
- What kind of values are there? Are there negative numbers? Floating points? Will there be empty inputs?
- Are there DUPLICATES within the input?
- What are some EXTREME cases of the input?
- How is the input stored? If you are given a dictionary of words, is it a list of strings or a trie?

## Write down TEST CASES, examples
Develop algorithm based on these test cases or examples.

## To implement the algorithm: INITIALIZATION, MAINTENANCE, TERMINATION.
- Be clear input data, function signature
- Initialization logic
- Maintenance: STATE TRANSITION recurrence relation before writing
    - Beware bounds of data
- Termination condition
- Write state transition RECURRENCE RELATION before writing code!

## Use modular design
Define utility functions to make the code modular, and reduce the risk of writing crowded code.

## Review code
Use a top down approach.
- Check modular logic
- Check INITIALIZATION
    - larger value initialization and corner case(following for not executed)
- Check STATE TRANSITION(maintenance of procedure): initialization in a loop, jump/break state
    - Check BRANCHES: use nested branch or logical AND condition?
    - Check DUPLICATE VALUES: MEMORY ALIASING/OVERLAPPING, e.g. swap(a, a), a = a.
    - Check OUT OF BOUND errors: keep track of variables RANGE
    - Check infinite loop
        - cycle
        - forgot incrementing  (i++)
    - Check statements after break/continue
- Check TERMINATION STATE
- Check TYPO, VARIABLE name misuse
- Check OFF BY ONE error
- Check numeric pitfalls: unsigned int arithmetic, overflow/underflow, float to int loses precision
- Check return and break state!
- Write function return statement first, since compiler may not warn you that.
- Write COMMENTS first for to clarify program logic
- Run TEST cases


### Types of software bugs
https://en.wikipedia.org/wiki/Software_bug#Types
- Typo
- Arithmetic
    - division by zero
    - overflow/underflow
    - loss of precision
- Logic
    - infinite loops
    - off by one error
- Resource: memory access violation

## Reserve space
Don't crowd the code.
For example, start writing like this, reserving space.
```cpp
bool        dfs(string word, Node *p)                           {
    Node *q;

    dfs(..., ...);
```

## Declare variables first
Just in case that you might need a variable to be in larger scope

