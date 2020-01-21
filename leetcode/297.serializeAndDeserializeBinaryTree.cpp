#include "297.serializeAndDeserializeBinaryTree.hpp"

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));

int testBfs() {
    CodecBfs codec;
    string s;

    s = "";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "0,#,0";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,2";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,2,3";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,2,3,#,#,4,5";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "#,1,2,3";
    assert(codec.deserialize(s) == 0);

    //s = "1 # 2 # 3 # 4 # 5 #"; // right tree
    s = "1,#,2,#,3,#,4,#,5"; // right tree
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "1 # 2 # 3 # 4 # 5 # #";
    s = "1,#,2,#,3,#,4,#,5";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,6,2,7,#,#,3,#,#,#,4,8,5";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "3,5,1,6,2,0,8,null,null,7,4"; // binary search tree
    assert(codec.serialize(codec.deserialize(s)).compare("3,5,1,6,2,0,8,#,#,7,4") == 0);

    cout << "self test passed!" << endl;
    return 0;
}

int testDfsPreorder() {
    CodecDfsPreorder codec;
    string s;

    s = "";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "0,#,0";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,2";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,2,3";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,2,3,#,#,4,5";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "#,1,2,3";
    assert(codec.deserialize(s) == 0);

    //s = "1 # 2 # 3 # 4 # 5 #"; // right tree
    s = "1,#,2,#,3,#,4,#,5"; // right tree
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "1 # 2 # 3 # 4 # 5 # #";
    s = "1,#,2,#,3,#,4,#,5";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,6,2,7,#,#,3,#,#,#,4,8,5";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "3,5,1,6,2,0,8,null,null,7,4"; // binary search tree
    assert(codec.serialize(codec.deserialize(s)).compare("3,5,1,6,2,0,8,#,#,7,4") == 0);

    cout << "self test passed!" << endl;
    return 0;
}

int testDfsPostorder() {
    CodecDfsPostorder codec;
    string s;

    s = "";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "0,#,0";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "2,#,1"; // left tree
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "2,#,#,3,1";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,2,3,#,#,4,5";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "1 # 2 # 3 # 4 # 5 #"; // right tree
    s = "5,4,3,2,1"; // right tree
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "1 # 2 # 3 # 4 # 5 # #";
    s = "1,#,2,#,3,#,4,#,5"; // left tree
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "1,6,2,7,#,#,3,#,#,#,4,8,5";
    s = "7,#,6,#,#,8,5,4,3,2,1";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "3,5,1,6,2,0,8,#,#,7,4"; // binary search tree
    //assert(codec.serialize(codec.deserialize(s)).compare("3,5,1,6,2,0,8,#,#,7,4") == 0);

    cout << "self test passed!" << endl;
    return 0;
}

int testDfsInorder() {
    CodecDfsInorder codec;
    string s;

    s = "";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "(1)";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "0,#,0";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "2,#,1"; // left tree
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "2,#,#,3,1";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    s = "1,2,3,#,#,4,5";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "1 # 2 # 3 # 4 # 5 #"; // right tree
    s = "5,4,3,2,1"; // right tree
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "1 # 2 # 3 # 4 # 5 # #";
    s = "1,#,2,#,3,#,4,#,5"; // left tree
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "1,6,2,7,#,#,3,#,#,#,4,8,5";
    s = "7,#,6,#,#,8,5,4,3,2,1";
    assert(codec.serialize(codec.deserialize(s)).compare(s) == 0);

    //s = "3,5,1,6,2,0,8,#,#,7,4"; // binary search tree
    //assert(codec.serialize(codec.deserialize(s)).compare("3,5,1,6,2,0,8,#,#,7,4") == 0);

    cout << "self test passed!" << endl;
    return 0;
}

int main()
{
    testBfs();
    testDfsPreorder();
    testDfsPostorder();
    //testDfsInorder();
}
