#include "../serializeAndDeserializeBinaryTree.hpp"

void testVisualize() {

    Codec codec;
    TreeNode *root = NULL;
    string s;
    vector<int> result;

    s = "";
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << result << endl;
    assert(equal(result.begin(), result.end(), vector<int>({}).begin()));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    assert(result == vector<int>({}));
    assert(result == root->postorderTraversal(true));

    s = "1";
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << result << endl;
    assert(result == vector<int>({1}));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    assert(result == vector<int>({1}));
    assert(result == root->postorderTraversal(true));

    s = "1,2";
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << result << endl;
    assert(result == vector<int>({2, 1}));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    assert(result == vector<int>({2, 1}));
    assert(result == root->postorderTraversal(true));

    s = "1,2,3";
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << "inorder: " << result << endl;
    assert(result == vector<int>({2, 1, 3}));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    cout << result << endl;
    assert(result == vector<int>({2, 3, 1}));
    assert(result == root->postorderTraversal(true));

    //s = "1 # 2 # 3 # 4 # 5 #"; // right tree
    s = "1,#,2,#,3,#,4,#,5"; // right tree
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << "inorder: " << result << endl;
    assert(result == vector<int>({1, 2, 3, 4, 5}));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    cout << result << endl;
    assert(result == vector<int>({5, 4, 3, 2, 1}));
    assert(result == root->postorderTraversal(true));

    s = "1,2,3,#,#,4,5";
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << "inorder: " << result << endl;
    assert(result == vector<int>({2, 1, 4, 3, 5}));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    cout << result << endl;
    assert(result == vector<int>({2, 4, 5, 3, 1}));
    assert(result == root->postorderTraversal(true));

    s = "#,1,2,3";
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << "inorder: " << result << endl;
    assert(result == vector<int>({}));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    assert(result == vector<int>({}));
    assert(result == root->postorderTraversal(true));
    cout << result << endl;

    s = "1,6,2,7,#,#,3,#,#,#,4,8,5";
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << "inorder: " << result << endl;
    assert(result == vector<int>({7, 6, 1, 2, 3, 8, 4, 5, }));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    cout << result << endl;
    assert(result == vector<int>({7, 6, 8, 5, 4, 3, 2, 1}));
    assert(result == root->postorderTraversal(true));


    s = "3,5,1,6,2,0,8,null,null,7,4";
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << "inorder: " << result << endl;
    assert(result == vector<int>({6, 5, 7, 2, 4, 3, 0, 1, 8, }));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    cout << result << endl;
    assert(result == root->postorderTraversal(true));

    s = "8,4,12,2,6,10,14,1,3,5,7,9,11,13,15"; // binary search tree
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << "inorder: " << result << endl;
    assert(result == vector<int>({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, }));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    cout << result << endl;
    assert(result == root->postorderTraversal(true));

    s = "";
    for (int i = 1; i < (1 << 5); ++i) {
        s += to_string(i) + ",";
    }
    root = codec.deserialize(s);
    root->print();
    result = root->inorderTraversal(true);
    cout << "inorder: " << result << endl;
    assert(result == vector<int>({16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22, 11, 23, 1, 24, 12, 25, 6, 26, 13, 27, 3, 28, 14, 29, 7, 30, 15, 31, }));
    assert(result == root->inorderTraversal(false));
    result = root->postorderTraversal(false);
    cout << result << endl;
    assert(result == root->postorderTraversal(true));

    cout << "self test[visualize] passed!" << endl;
}

void testPreorder() {
    Codec codec;
    TreeNode *root = NULL;
    string s;

    s = "";
    root = codec.deserialize(s);
}

int main()
{
    testVisualize();
    cout << "self test passed!" << endl;
}
