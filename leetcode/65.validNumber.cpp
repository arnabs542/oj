/**
 *
65. Valid Number
Hard

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

================================================================================
SOLUTION

1. Rule based if branch
Error prone, ugly.

Complexity: O(N)

2. Finite state machine - graph state transition - deterministic finite automate(dfa)
Finite state machine! This can be modeled as a deterministic finite automata.
The state transition graph is illustrated in image: ./65.validNumber.png.

Complexity: O(N)

 *
 */
#include <debug.hpp>

class Solution {
public:
    bool isNumber(string s) {
        bool result;
        result = isNumberDfa(s);

        cout << s << " => " << result << endl;

        return result;
    }

    enum State {
        INI = 0, // initial empty state
        SGN, // +- sign
        PNT, // . point/dot, without number
        NUM, // number without point
        //N_P, // number and dot
        P_N, // number after point
        EXP, // exponential sign e
        SAE, // sign after exponential notation e
        NAE, // number after exponential notation e
        TSP, // trailing space
        ERR, // ERROR
    };

    //enum Input {
        //DIGIT,
        //E,
        //S,
        //DOT,
        //SPACE,
        //INVALID,
    //};

    inline State nextState(const State state, const char c) {
        // state transition table
        static const vector<vector<State>> transition = {
            // 0-9, e,  +-,  .,   \t, invalid
            {NUM, ERR, SGN, PNT, INI, ERR}, // INIT
            {NUM, ERR, ERR, PNT, ERR, ERR}, // SIGN
            {P_N, ERR, ERR, ERR, ERR, ERR}, // POINT
            {NUM, EXP, ERR, P_N, TSP, ERR}, // NUM
            {P_N, EXP, ERR, ERR, TSP, ERR}, // N_P
            //{P_N, EXP, ERR, ERR, ERR, ERR}, // P_N
            {NAE, ERR, SAE, ERR, ERR, ERR}, // EXP
            {NAE, ERR, ERR, ERR, ERR, ERR}, // SAE
            {NAE, ERR, ERR, ERR, TSP, ERR}, // NAE
            {ERR, ERR, ERR, ERR, TSP, ERR}, // TSP
            {ERR, ERR, ERR, ERR, ERR, ERR}, // ERR
        };
        // TODO: another way to represent the sparse graph is with edges.
        int input = classifyInput(c);

        return transition[state][input];
    }

    inline int classifyInput(const char c) {
        if ('0' <= c && c <= '9') {
            return 0;
        } else if (c  == 'e' || c == 'E') {
            return 1;
        } else if (c == '-' || c == '+') {
            return 2;
        } else if (c == '.') {
            return 3;
        } else if (c == ' ' || c == '\t') {
            return 4; // white space
        } else {
            return 5; // invalid
        }
    }

    bool isNumberDfa(string s) {
        static const vector<State> acceptable{NUM, P_N, NAE, TSP};
        State state = INI;
        for (const char c: s) {
            state = nextState(state, c);
        }
        return std::find(acceptable.begin(), acceptable.end(), state) != acceptable.end();
    }

};

int test() {
    Solution solution;

    string s;
    bool output;

    s = ""; output = false;
    assert(solution.isNumber(s) == output);

    s = "0"; output = true;
    assert(solution.isNumber(s) == output);
    s = "0   "; output = true;
    assert(solution.isNumber(s) == output);
    s = "0."; output = true;
    assert(solution.isNumber(s) == output);
    s = ".1"; output = true;
    assert(solution.isNumber(s) == output);

    s = "."; output = false;
    assert(solution.isNumber(s) == output);
    s = "0.0"; output = true;
    assert(solution.isNumber(s) == output);
    s = "-.1"; output = true;
    assert(solution.isNumber(s) == output);

    s = "1e+1"; output = true;
    assert(solution.isNumber(s) == output);
    s = "1e+"; output = false;
    assert(solution.isNumber(s) == output);
    s = "0.1e"; output = false;
    assert(solution.isNumber(s) == output);
    s = "0.e1"; output = true;
    assert(solution.isNumber(s) == output);
    s = ".e1"; output = false;
    assert(solution.isNumber(s) == output);

    s = "-.5364764e+3"; output = true;
    assert(solution.isNumber(s) == output);
    s = "-34342.e-3"; output = true;
    assert(solution.isNumber(s) == output);
    s = "-1e3.1"; output = false;
    assert(solution.isNumber(s) == output);
    s = "-e+3"; output = false;
    assert(solution.isNumber(s) == output);

    s = "G"; output = false;
    assert(solution.isNumber(s) == output);
    s = "G76"; output = false;
    assert(solution.isNumber(s) == output);

    cout << "test passed" << endl;
    return 0;
}

int main(int argc, char **argv) {
    test();

    return 0;
}
