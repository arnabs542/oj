/**
 *
648. Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Note:
The input will only have lower-case letters.
    1. 1 <= dict words number <= 1000
    2. 1 <= sentence words number <= 1000
    3. 1 <= root length <= 100
    4. 1 <= sentence words length <= 1000

==============================================================================================
SOLUTION

1. Brute force

In the replacement stage, we have two method.
1) Build the dictionary by doing nothing, representing the dictionary as a string list.
For each word, iterate all possible roots in the dictionary, and take the shortest one.

Complexity: O(n\sum{w_i^2}), O(n)

2) Build the dictionary by representing the dictionary as a string hash set.
For each word, iterate all possible prefixes, check whether the prefix is in the dictionary.

Complexity: O(\sum{w_i^2}), O(n)
where w_i is the length of the i-th word. We might check every prefix, the i-th of which
is O(w_i^2) considering the hashing complexity.
And n is the length of trie node.

Complexity:
O(mnl), where l is the average word length.
O(ml), where l is the average length in the dictionary.


3. Trie - prefix tree
Obviously, prefixes are involved. Prefix tree supports O(m) time complexity query time
for a target word of length m.

For each word in the sentence, we find the shortest prefix word in the trie tree, and replace!

Complexity: O(m), O(n), where m is the length of sentence and n in the size of dictionary.
 *
 */
#include <debug.hpp>
#include "_tree.hpp"

class Solution {
public:
    string replaceWords(vector<string>& dict, string sentence) {
        string result =  _replaceWrodsTrie(dict, sentence);
        cout << sentence << " => " << result << endl;
        return result;
    }

    string _replaceWrodsTrie(vector<string>& dict, string sentence) {
        string result = "";
        Trie trie(dict);

        istringstream iss(sentence);
        string word;
        string root;

        while(getline(iss, word, ' ')) {
            root = trie.shortestPrefix(word);
            if (root == "") {
                root = word;
            }
            result += (result.size()?" ": "") + root;
        }

        return result;
    }
};


void test() {
    Solution solution;
    vector<string> dict;
    string sentence;
    string output;
    string result;

    dict = {};
    sentence = "";
    output = "";
    result = solution.replaceWords(dict, sentence);
    assert(result == output);

    dict = {};
    sentence = "the cattle was rattled by the battery";
    output = sentence;
    result = solution.replaceWords(dict, sentence);
    assert(result == output);

    dict = {"up", "upload", "upper"};
    sentence = "the cattle was destroyed while uploading the battery";
    output = "the cattle was destroyed while up the battery";
    result = solution.replaceWords(dict, sentence);
    assert(result == output);

    dict = {"cat", "bat", "rat"};
    sentence = "the cattle was rattled by the battery";
    output = "the cat was rat by the bat";
    result = solution.replaceWords(dict, sentence);
    assert(result == output);

    cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
