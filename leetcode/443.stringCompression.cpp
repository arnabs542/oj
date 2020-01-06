/**
 *
443. String Compression

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.

==============================================================================================
SOLUTION

1. Remove from front and push back (append)
Sort the list. (NOTE: actually it should be sorted, in this problem)
Scan the list, and erase the whole group of same characters while maintaining the group count.
Then append the compressed group to the end of the list.

2. Two pointers
Replace elements in the front.

 */

#include <debug.hpp>

class Solution {
public:
    int compress(vector<char>& chars) {
        cout << chars;
        int result = _compressRemove(chars);
        cout << result << " => " << chars << endl;
        return result;
    }

    int _compressRemove(vector<char>& chars) {
        //sort(chars.begin(), chars.end());
        int n = chars.size();
        char c = n ? chars[0]: 0; // current character c
        int nc = 0; // number of character c
        for (int i = 0; i < n + 1; ++i) {
            //cout << nc << ", " << c << endl;
            if (i == n || chars[0] != c){
                if (nc) chars.push_back(c);
                if (nc > 1) for (char x:to_string(nc)) chars.push_back(x);
                if (i == n) { break; }
                c = chars[0];
                nc = 1;
            } else if (chars[0] == c) {
                ++nc;
            }
            if (i != n) chars.erase(chars.begin());
        }

        return chars.size();
    }
};

void test() {

    Solution solution;

    vector<char> chars;
    int n = 0;

    chars = vector<char>({});
    assert(solution.compress(chars) == 0);

    chars = vector<char>({'a'});
    assert(solution.compress(chars) == 1);
    assert(chars == vector<char>({'a'}));

    chars = vector<char>({'a', 'a'});
    assert(solution.compress(chars) == 2);
    assert(chars == vector<char>({'a', '2'}));

    chars = vector<char>({'a','a','b','b','c','c','c'});
    n = solution.compress(chars);
    assert(n == 6);
    //assert(std::equal(chars.begin(), chars.begin() + n,
                //vector<char>({'a','2','b','2','c','3'}).begin()));
    assert(vector<char>({'a','2','b','2','c','3'}) == chars);

    chars = vector<char>({'a','b','b','b','b','b','b','b','b','b','b','b','b'});
    assert(solution.compress(chars) == 4);
    assert(chars == vector<char>({'a','b','1','2'}));

    chars = vector<char>({'a','a','a','b','b','a','a'});
    assert(solution.compress(chars) == 6);
    assert(chars == vector<char>({'a', '3', 'b', '2', 'a', '2'}));

    cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
