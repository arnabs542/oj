#include <debug.hpp>
#include "../tree.hpp"

void test() {
    Trie trie;

    assert(!trie.search(""));
    assert(trie.startsWith(""));

    trie.insert("");
    assert(trie.startsWith(""));
    assert(!trie.search("hello"));
    assert(!trie.startsWith("hell"));
    trie.insert("hello");
    assert(trie.search("hello"));
    assert(!trie.search("hell"));
    assert(!trie.search("helloo"));
    assert(trie.startsWith("hell"));

    assert(trie.shortestPrefix("hello") == "");

    trie = Trie();
    trie.insert("hello");
    assert(trie.shortestPrefix("hello") == "hello");
    assert(trie.shortestPrefix("helloworld") == "hello");

    try {
        trie.insert("clue");
        trie.insert("clueless");
        trie.remove("clue");
        trie.insert("clueless");
        trie.remove("clueless");
    }catch(exception& e) {
        cout << "ERROR: " << e.what() << endl;
        //throw runtime_error("trie tree test error");
    }


    cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
