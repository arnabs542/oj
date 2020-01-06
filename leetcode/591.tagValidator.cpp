/*
 *
591. Tag Validator

Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:

1. The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
2. A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
3. A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
4. A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
5. A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
6. A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
7. The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
9. CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.

----------------------------------------------------------------------------------------------
Valid Code Examples:
    Input: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

    Output: True

    Explanation:

    The code is wrapped in a closed tag : <DIV> and </DIV>.

    The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata.

    Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.

    So TAG_CONTENT is valid, and then the code is valid. Thus return true.


    -------------------------------------------------------------
    Input: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

    Output: True

    Explanation:

    We first separate the code into : start_tag|tag_content|end_tag.

    start_tag -> "<DIV>"

    end_tag -> "</DIV>"

    tag_content could also be separated into : text1|cdata|text2.

    text1 -> ">>  ![cdata[]] "

    cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"

    text2 -> "]]>>]"


    The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
    The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.

----------------------------------------------------------------------------------------------
Invalid Code Examples:
    Input: "<A>  <B> </A>   </B>"
    Output: False
    Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.

    Input: "<DIV>  div tag is not closed  <DIV>"
    Output: False

    Input: "<DIV>  unmatched <  </DIV>"
    Output: False

    Input: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
    Output: False

    Input: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
    Output: False

    Input: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
    Output: False

----------------------------------------------------------------------------------------------
Note:
For simplicity, you could assume the input code (including the any characters mentioned above) only contain letters, digits, '<','>','/','!','[',']' and ' '.

==============================================================================================
SOLUTION

1. State Machine

STACK
----------------------------------------------------------------------------------------------
Nested structure implies that STACK data structure might be involved. Also, XML code is wrapped
from two ends, we can also utilize two pointers scan from two ends.

TOKENIZE
----------------------------------------------------------------------------------------------
TOKENIZING may make it easier, so that we can process that string in a larger granularity.
The state transition is complex: smaller module granularity like tags and whole code granularity.
If two different levels(character level and token level) of state transition are decoupled, it's simpler.

STATE MACHINE
----------------------------------------------------------------------------------------------
First step is sequence processing by TOKENIZING. This step can utilize Finite State Machine.

Some major states corresponding to composing parts of the code:

Start tag: Begin, Middle, End
End tag: Begin, Middle, End
Text: B, M, E
CDATA: B, M, E

Note that the state in this scenario is a compound one, a tuple, because some state transition
take in consideration of factors such as substring length.

Define general state as a tuple:
    two pointers i and j, indicating the token bound, current token state(TAG, TEXT, ...)

A trick here is that when calculating state transition, assume default next state is ILLEGAL.
Since possible situations are much less than negative situations. So we need to only consider
a small portion of positive state transition.


STACK or BIDIRECTIONAL SCANNING with tokens
----------------------------------------------------------------------------------------------
next step is tag matching , maybe with STACK.
By the way, because all start tags and end tags must be symmetric, we can scan from two ends as well.

NOTE: linear scan is wrong! Consider case "<A><B></B><C></C></A>"!
This is a NESTED STRUCTURE! Use recursive solution(STACK).

NOTE: the outermost tags must match, and the inner ones must reveal stack property!

----------------------------------------------------------------------------------------------
Complexity: O(n), O(n).

2. Do it one pass
Scan for ",", then there are several cases:
1. Start tag
2. End tag
3. CDATA
4. Invalid input

3. Recursive Parsing with regular expression
Parse outside most tags, then validate inner TAG_CONTENT.

Following is from https://leetcode.com/articles/tag-validator/
----------------------------------------------------------------------------------------------
Instead of manually checking the given codecode string for checking the validity of TAG_NAME, TAG_CONTENT and cdata, we can make use of an inbuilt java fuunctionality known as regular expressions.

A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. They can be used to search, edit, or manipulate text and data. The most common quantifiers used in regular expressions are listed below. A quantifier after a token (such as a character) or group specifies how often that preceding element is allowed to occur.

? The question mark indicates zero or one occurrences of the preceding element. For example, colou?r matches both "color" and "colour".

* The asterisk indicates zero or more occurrences of the preceding element. For example, ab*c matches "ac", "abc", "abbc", "abbbc", and so on.

+ The plus sign indicates one or more occurrences of the preceding element. For example, ab+c matches "abc", "abbc", "abbbc", and so on, but not "ac".

{n} The preceding item is matched exactly n times.

{min,} The preceding item is matched min or more times.

{min,max} The preceding item is matched at least min times, but not more than max times.

| A vertical bar separates alternatives. For example, gray|grey can match "gray" or "grey".

() Parentheses are used to define the scope and precedence of the operators (among other uses). For example, gray|grey and gr(a|e)y are equivalent patterns which both describe the set of "gray" or "grey".

[...] Matches any single character in brackets.

[^...] Matches any single character not in brackets.

Thus, by making use of regex, we can directly check the validity of the codecode string directly(except the nesting of the inner tags) by using the regex expression below:

<([A-Z]{1,9})>([^<]*((<\/?[A-Z]{1,9}>)|(<!\[CDATA\[(.*?)]]>))?[^<]*)*<\/\1>



 *
 */

#include <debug.hpp>

bool isupper(string s) {
    return !s.empty() && isupper(s[0]);
}

bool beginWith(string s, string t) {
    return s.size() >= t.size() && s.substr(0, t.size()) == t;
}

enum State {
    INIT,
    TAG_BEGIN,

    START_TAG,
    END_TAG,
    CDATA_TAG,
    TEXT, // text outside CDATA

    START_TAG_END,
    END_TAG_END,
    CDATA_TAG_END,

    SUCCESS,
    ILLEGAL,
};

class Solution {
public:
    bool isValid(string code) {
        bool result = _isValidTokenStack(code);

        cout << (result ? "true":"false") << "\t" << code << endl << endl;

        return result;
    }

    /*
     * Parse the XML code into a list of tag tokens, and discard TEXT, CDATA.
     * Making use of Finite State Machine.
     *
     * Returns
     * whether tokenization is successful
     */
    bool _tokenize(string code, vector<string>& tokens) {
        State state = INIT;
        string buffer;
        string token;
        unsigned int i = 0, j = 0;

        auto f = [&](State s, char c) {
            State state_new = ILLEGAL;
            switch (s) {
                case INIT:
                    if (c == EOF) { state_new = SUCCESS; }
                    else if (c == '<') { state_new = TAG_BEGIN; }
                    break;
                case TAG_BEGIN: // "<"
                    if (c == EOF) { state_new = ILLEGAL; }
                    else if (isupper(c)) { state_new = START_TAG; }
                    else if (c == '/') { state_new = END_TAG; }
                    else if (c == '!') { state_new = CDATA_TAG; }
                    break;
                case START_TAG: // "<X"
                    if (c == EOF) { state_new = ILLEGAL; }
                    else if (c == '>') { state_new = START_TAG_END; }
                    else { state_new = (isupper(c) && j - i <= 9) ? s : ILLEGAL; }
                    break;
                case END_TAG: // "</"
                    if (c == EOF) { state_new = ILLEGAL; }
                    else if (c == '>') { state_new = END_TAG_END; }
                    else { state_new = isupper(c) && j - i <= 10 ? s : ILLEGAL; }
                    break;
                case CDATA_TAG:
                    if (j - i > 8) {
                        if ( c != '>') { state_new = CDATA_TAG; }
                        else { state_new = code.substr(j - 2, 3) == "]]>" ? CDATA_TAG_END : CDATA_TAG; }
                    } else if ("<![CDATA["[j - i] == c){ state_new = CDATA_TAG; }
                    break;
                case START_TAG_END:
                case END_TAG_END:
                case CDATA_TAG_END:
                    if (c == EOF) { state_new = (state == CDATA_TAG_END?ILLEGAL:SUCCESS); }
                    else if (c == '<') { state_new = TAG_BEGIN; }
                    else { state_new = TEXT; }
                    break;
                case TEXT:
                    if (c == '<') { state_new = TAG_BEGIN; }
                    else { state_new = s; }
                    break;
                default:
                    break;
            }
            return state_new;
        };

        while (j < code.size()) {
            char c = code[j];
            state = f(state, c);
            if (state == ILLEGAL) {
                cout << "ILLEGAL: " << code.substr(i, j - i + 1) << endl;
                //cout << "tokens: " << tokens << endl;
                return false;
            }
            if (state == START_TAG_END || state == END_TAG_END || state == CDATA_TAG_END) {
                token = code.substr(i, j - i + 1);
                tokens.push_back(token); // can't discard TEXT here...
                //cout << "token: " << token << ", i, j: " << i << ", " << j<< endl;
                i = j + 1;
            }
            else if (state == TAG_BEGIN) {
                 //confidently discard text content
                //if (j > i) {
                    //token = code.substr(i, j - i);
                    //tokens.push_back(token);
                //}
                i = j;
            }
            ++j;
        }
        state = f(state, EOF); // feed end of file

        //cout << "tokens: " << tokens << endl;

        return state == SUCCESS;
    }

    /*
     *
     * Match start and end tags with two pointers
     *
     */
    bool _isValidTokenStack(string code) {

        vector<string> tokens;
        stack<string> tokenStack;
        if (!_tokenize(code, tokens)) {
            return false;
        };
        auto match = [](string t1, string t2) {
            return t1.substr(1, t1.size() - 1) == t2.substr(2, t2.size() - 2);
        };

        if (tokens.size() == 1) { // edge case: size 1
            return false;
        }
        if (tokens.size() >= 2 && !match(tokens[0], tokens[tokens.size() - 1])) {
            cout << "outer tags don't match!" << endl;
            return false;
        }
        for (int i = 1; i < (int)tokens.size() - 1; ++i) {
            string token = tokens[i];
            if (token.empty()) {
                continue;
            }
            if (token[1] == '!') {
                continue;
            }
            else if (token[1] != '/') {
                tokenStack.push(token);
            } else if (!tokenStack.size()) {
                return false;
            }
            else {
                string token0 = tokenStack.top();
                if (match(token0, token)) {
                    tokenStack.pop();
                } else return false;
            }
        }
        //cout << to_string(tokens) << endl;
        return tokenStack.size() == 0;
    }
};

void test() {
    Solution solution;
    string code;
    bool result;

    // positive samples
    code = "";
    result = solution.isValid(code);
    assert(result);

    code = "<A></A>";
    result = solution.isValid(code);
    assert(result);

    code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>";
    result = solution.isValid(code);
    assert(result);

    code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>";
    result = solution.isValid(code);
    assert(result);

    code = "<HTML><BODY><P>Hi there, how are you doing? <![CDATA[<div><<div><![CDATA[]]]]> </P> </BODY></HTML>";
    result = solution.isValid(code);
    assert(result);

    code = "<A><A>456</A>  <A> 123  !!  <![CDATA[]]>  123 </A>   <A>123</A></A>";
    result = solution.isValid(code);
    assert(result);

    code = "<A><B></B><C></C></A>";
    result = solution.isValid(code);
    assert(result);


    // false samples;
    code = "HELLO";
    result = solution.isValid(code);
    assert(!result);

    code = "<";
    result = solution.isValid(code);
    assert(!result);

    code = "<<";
    result = solution.isValid(code);
    assert(!result);

    code = ">";
    result = solution.isValid(code);
    assert(!result);

    code = ">>";
    result = solution.isValid(code);
    assert(!result);

    code = "<>";
    result = solution.isValid(code);
    assert(!result);

    code = "<a>";
    result = solution.isValid(code);
    assert(!result);

    code = "<A>";
    result = solution.isValid(code);
    assert(!result);

    code = "<A></A><B></B>";
    result = solution.isValid(code);
    assert(!result);

    code = "<A><A></A></A></A>";
    result = solution.isValid(code);
    assert(!result);

    code = "<![CDATA[ABC]]><TAG>sometext</TAG>";
    result = solution.isValid(code);
    assert(!result);

    code = "<A></A>HELLOWORLD";
    result = solution.isValid(code);
    assert(!result);

    code = "<A>HELLOWORLD";
    result = solution.isValid(code);
    assert(!result);

    code = "<A><![CDATA[HELLOWORLD]]>";
    result = solution.isValid(code);
    assert(!result);

    code = "<![CDATA[HELLO]]>";
    result = solution.isValid(code);
    assert(!result);

    code = "<A>  <B> </A>   </B>";
    result = solution.isValid(code);
    assert(!result);

    code = "<TRUe><![CDATA[123123]]]]><![CDATA[>123123]]></TRUe>";
    result = solution.isValid(code);
    assert(!result);

    code = "<A><></A>";
    result = solution.isValid(code);
    assert(!result);

    code = "<ABCDEFGHIJKLMNOPQ></ABCDEFGHIJKLMNOPQ>";
    result = solution.isValid(code);
    assert(!result);

    code = "<DIV>  div tag is not closed  <DIV>";
    result = solution.isValid(code);
    assert(!result);

    code = "<DIV>  unmatched <  </DIV>";
    result = solution.isValid(code);
    assert(!result);

    code = "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>";
    result = solution.isValid(code);
    assert(!result);

    code = "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>";
    result = solution.isValid(code);
    assert(!result);

    code = "<Html><BODY><P>Hi there, how are you doing? <![CDATA[<div><<div><![CDATA[]]]]> </P> </BODY></Html>";
    result = solution.isValid(code);
    assert(!result);

    code = "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>";
    result = solution.isValid(code);
    assert(!result);

    cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
