#include <debug.hpp>


class Solution {
public:
    void reverseWords(string &s) {
        cout << s;
        //_reverseWordsTwoPassesReverse(s);
        _reverseWordsTwoPassesReverseOpt(s);
        cout << " => " << s << endl;
    }

    /*
     *
     * Reverse the whole string first, then reverse each word.
     *
     */
    void _reverseWordsTwoPassesReverse(string &s) {
        // DONE: remove extra white spaces by overwriting with non-spaces.
        unsigned int i = 0, j = 0; // i: next pointer to write, pointer to read
        while (j < s.size() && s[j] == ' ') ++j; // first non empty character
        for (; j < s.size(); ++j) {
            if (s[j] == ' ' && j && s[j - 1] == ' ') continue; // don't copy extra space
            s[i++] = s[j];
        }
        s.erase(s.begin() + i, s.end()); // remove extra white spaces
        while( s.size() > 0 && s[s.size() - 1] == ' ' ) s.pop_back(); // same as above

        reverse(s.begin(), s.end()); // DONE: reverse all characters

        i = 0;
        while (i < s.size()) {
            for (j = i; j < s.size() && s[j] != ' '; ++j); // find word end pointer
            // DONE: two pointers reverse characters in each word
            reverse(s.begin() + i, s.begin() + j); // reverse
            i = j + 1; // update word begin pointer
        }
    }

    // TODO: the pass to eliminate the extra white spaces can be merged into
    // the pass to reverse characters each word.
    void _reverseWordsTwoPassesReverseOpt(string &s) {
        reverse(s.begin(), s.end()); // 1 pass: reverse the whole string
        unsigned int pWrite = 0, pRead = 0, wordLen = 0;
        while (pRead < s.size()) { // 2 pass: revers each word
            wordLen = 0;
            while(pRead < s.size() && s[pRead] == ' ') pRead++; // to word begin
            if (pWrite) s[pWrite++] = ' ';
            while (pRead < s.size() && s[pRead] != ' ') {
                s[pWrite++] = s[pRead++];
                ++wordLen;
            } // override white spaces to eliminate extra ones
            reverse(s.begin() + pWrite - wordLen, s.begin() + pWrite); // reverse each word
        }
        s.erase(s.begin() + pWrite, s.end());
        while (s.size() && s.back() == ' ') s.pop_back();
    }
};

void test() {
    Solution solution;

    string s;

    s = "hello world";
    solution.reverseWords(s);

    assert (s != "dlrow olleh");
    assert (s == "world hello");

    s = "   hello world   ";
    solution.reverseWords(s);
    assert (s == "world hello");

    s = "hello world    My name is Bishop";
    solution.reverseWords(s);
    assert (s == "Bishop is name My world hello");

    cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
