#include "../serializeAndDeserializeBinaryTree.hpp"


int main()
{
    Codec codec;
    TreeNode *root = NULL;
    string s;

    s = "";
    root = codec.deserialize(s);
    root->print();

    s = "1";
    root = codec.deserialize(s);
    root->print();

    s = "1 2";
    root = codec.deserialize(s);
    root->print();

    s = "1 2 3";
    root = codec.deserialize(s);
    root->print();

    s = "1 2 3 # # 4 5";
    root = codec.deserialize(s);
    root->print();

    s = "# 1 2 3";
    codec.deserialize(s);
    root->print();

    //s = "1 # 2 # 3 # 4 # 5 #"; // right tree
    s = "1 # 2 # 3 # 4 # 5"; // right tree
    root = codec.deserialize(s);
    root->print();

    //s = "1 # 2 # 3 # 4 # 5 # #";
    s = "1 # 2 # 3 # 4 # 5";
    root = codec.deserialize(s);
    root->print();

    s = "1 6 2 7 # # 3 # # # 4 8 5";
    root = codec.deserialize(s);
    root->print();


    s = "3 5 1 6 2 0 8 null null 7 4"; // binary search tree
    root = codec.deserialize(s);
    root->print();

    s = "";
    for (int i = 1; i < (1 << 5); ++i) {
        s += to_string(i) + " ";
    }
    root = codec.deserialize(s);
    root->print();

    cout << "self test passed!" << endl;
}
