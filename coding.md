# Tips on white board coding or paper coding

## Reserver space
Don't crowd the code.
For example, start writing like this.
```cpp
bool        dfs(string word, Node *p)                           {
    Node *q;

    dfs(..., ...);
```

## Declare variables first
Just in case that you might need a variable to be in larger scope

## Use modular design
Define utility functions to make the code modular, and reduce the risk of writing crowded code.

## Ask questions to clarify
- How big is the size of the input?
- How big is the RANGE of values?
- What kind of values are there? Are there negative numbers? Floating points? Will there be empty inputs?
- Are there DUPLICATES within the input?
- What are some EXTREME cases of the input?
- How is the input stored? If you are given a dictionary of words, is it a list of strings or a trie?
