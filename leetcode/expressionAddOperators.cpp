/**
 *
282. Expression Add Operators

Hard

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []

SOLUTION
================================================================================

Apparently, this is a graph search problem.

The key is how to reduce the problem into optimal substructures.

There are two problems to concern.
1. A number may contain multiple digits
2. Multiply operator has a higher precedence than the addition and subtraction operators.
1 + 2 = 3
1 + 2 - 4 --> 3 - 4 --> -1
1 + 2 - 4 * 12 --> -1 * 12 --> -12 (WRONG!)
1 + 2 - 4 * 12 --> -1 - (-4) + (-4 * 12) --> 3 + (-48) --> -45 (CORRECT!)


To Reduce the problem into simpler ones, one intuition is to remove the last number x,
and transform the problem of (num[:n], target) into subproblems:
    (num[:n-i], target+x), searching for f(n-i)=target+x
    (num[:n-i], target-x), searching for f(n-i)=target-x
    (num[:n-i], target/x), searching for f(n-i)=target/x. (WRONG)
where i is the number of digits in x.

How about operator '*'?
For example, '2+3*2' = 8, can't be reduced to ('23', 4), since '*2' isn't the last
operation to calculate!
But the last operator '+' or '-' is always calculated last.

So we need to find the LAST SEQUENCE OF OPERATION NOT CONTAINING PLUS OR SUBTRACT.
So the expression takes form:
    (any possible expression) (+|-) (multiply chain or a single number).

Then the problem is reduced to:
  1. g(s): given a string s, find all numbers can be obtained with only '*', or no '*'.
  2. f(n, target) -> f(n - i, target+x), f(n-i, target-x), where x is g(num[n-i+1:n]).
Apparently, g(s) can be done with dfs(depth first search) too, with memoization.
g(s) -> int(s[0:i]) * g(s[i:]), for i = 0, ..., m-1, where len(s) == m.


 *
 */

#include <debug.hpp>

class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> results;

        results = addOperatorsDfs(num, target);

        cout << num << " " << target
            << " => " << results << endl;

        return results;
    }

    vector<string> addOperatorsDfs(string num, int target)
    {
        cachedProducts.clear();
        cachedExpressions.clear();
        vector<string> result = dfs(num, num.size() - 1, target);
        sort(result.begin(), result.end());

        return result;
    }

    // memoized function
    vector<pair<string, int>> findProducts(string num, int p, int q) {
        vector<pair<string, int>> products;

        // base case
        if (p == q) {
            //products.push_back(make_pair(to_string(num[p]), stoi(to_string(num[p]))));
            products.push_back(make_pair(string(1, num[p]), num[p] - '0'));
            return products;
        }

        // memoization
        if (cachedProducts.find(make_pair(p, q)) != cachedProducts.end()) {
            return cachedProducts[make_pair(p, q)];
        }
        // iterate, ending at k
        for (int k = p; k < q; ++k) {
            if (num[p] == '0' && k > p) break; // numbers with more digits can't start with 0
            vector<pair<string, int>> partialResults = findProducts(num, k + 1, q); // XXX: beware dead loop, k + 1
            for (size_t i = 0; i < partialResults.size() && i < 11; ++i) { // int has 10 digits at most
                string expr = num.substr(p, k - p + 1) + '*' + partialResults[i].first;
                try {
                    int operand = stoi(num.substr(p, k - p + 1));
                    if (operand  < 1.0 * numeric_limits<int>::max() / partialResults[i].second)
                        products.push_back(make_pair(expr, operand * partialResults[i].second));
                }catch(exception e) {
                    //cout << "output range error: " << num.substr(p, q - p + 1) << endl;
                }
            }
        }
        if(num[p] != '0') // k == q?
        {
            // XXX: check int! may out of range
            try { products.push_back(make_pair(num.substr(p, q - p + 1), stoi(num.substr(p, q - p + 1)))); }
            catch (exception e) {
                //cout << "output range error: " << num.substr(p, q - p + 1) << endl;
            }
        }
        cachedProducts[make_pair(p, q)] = products;

        return products;
    }

    /**
     * num: input string
     * k: ending index
     * target: target value
     */
    vector<string> dfs(string num, int k, int target)
    { // 12, 1, 2
        vector<string> results;

        // base case
        if (k == -1) {
            return vector<string> {};
        }
        if (k == 0 && num[0] - '0' == target) // careful: char to int
            return vector<string> {string(1, num[0])};

        // memoization
        if (cachedExpressions.find(make_pair(k, target)) != cachedExpressions.end()) return cachedExpressions[make_pair(k, target)];

        // recursive, processing backward
        for (int i = k; i >= 0; --i) { // 2
            vector<pair<string, int>> lastProducts = findProducts(num, i, k); // list of <expression, number>. {<3,3>}
            for (size_t j = 0; j < lastProducts.size(); ++j) {
                if (numeric_limits<int>::max() >= lastProducts[j].second + target) {
                    const vector<string> &partialResults1 = dfs(num, i - 1, target + lastProducts[j].second); // -
                    for (const string &partialExpr: partialResults1) {
                        results.push_back(partialExpr + "-" + lastProducts[j].first);
                    }
                }
                else cout << "overflow: " << target << "+" << lastProducts[j].second << " " << numeric_limits<int>::max() - target;

                if (target - lastProducts[j].second >= numeric_limits<int>::min()) {
                    const vector<string> &partialResults2 = dfs(num, i - 1, target - lastProducts[j].second); // +
                    for (const string &partialExpr: partialResults2) {
                        results.push_back(partialExpr + "+" + lastProducts[j].first);
                    }
                }
                else cout << "underflow: " << target << "-" << lastProducts[j].second << " " << (-numeric_limits<int>::min() + target);
                // XXX: dead end. i == 0? check solution!
                if (i == 0 && lastProducts[j].second == target)
                    results.push_back(lastProducts[j].first);
            }
        }

        cachedExpressions[make_pair(k, target)] = results;

        return results;
    }


    // memoization
    map<pair<int, int> , vector<pair<string, int>>> cachedProducts;// string to mutiplication
    map<pair<int, int>, vector<string>> cachedExpressions;
};

int main(int argc, char *argv[])
{
    Solution solution;

    string num;
    int target;
    vector<string> output;

    num = "";
    target = 0;
    output = {};
    assert(solution.addOperators(num, target) == output);

    num = "0";
    target = 0;
    output = {"0"};
    assert(solution.addOperators(num, target) == output);

    num = "00";
    target = 0;
    output = {"0*0", "0+0", "0-0"};
    assert(solution.addOperators(num, target) == output);

    num = "000";
    target = 0;
    output = {"0*0*0", "0*0+0", "0*0-0", "0+0*0", "0+0+0", "0+0-0", "0-0*0", "0-0+0", "0-0-0", };
    assert(solution.addOperators(num, target) == output);

    num = "12";
    target = 2;
    output = {"1*2"};
    assert(solution.addOperators(num, target) == output);

    num = "12";
    target = 3;
    output = {"1+2"};
    assert(solution.addOperators(num, target) == output);

    num = "123";
    target = 6;
    output = {"1*2*3", "1+2+3"};
    assert(solution.addOperators(num, target) == output);

    num = "232";
    target = 8;
    output = {"2*3+2", "2+3*2"};
    assert(solution.addOperators(num, target) == output);

    num = "105";
    target = 5;
    output = {"1*0+5","10-5"}; // "1+05"
    assert(solution.addOperators(num, target) == output);

    num = "110";
    target = 110;
    output = {"110"};
    assert(solution.addOperators(num, target) == output);

    num = "3456237490";
    target = 9191;
    output = {};
    assert(solution.addOperators(num, target) == output);

    num = "2147483647";
    target = 2147483647; // deal with overflow
    output = {"2147483647"};
    assert(solution.addOperators(num, target) == output);

    num = "2147483648";
    target = -2147483648;
    output = {};
    assert(solution.addOperators(num, target) == output);

    num = "0000";
    target = 0;
    output = {}; // 3 ^ (n-1) results
    cout << solution.addOperators(num, target).size() << " results for " << num << endl;


    cout << "self test passed";
    return 0;
}
