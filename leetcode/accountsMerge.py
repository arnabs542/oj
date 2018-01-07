#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.


Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.


Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].

================================================================================
SOLUTION

Many-to-many connections form a graph. And this problem can be thought as a
undirected bipartite, where vertices are people and email addresses.

The task is to find connected components.

1. Graph search - dfs or bfs

2. Union find


"""

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        result = self._accountsMergeDfs(accounts)

        print(accounts, "=>", result)

        return result

    def _accountsMergeDfs(self, accounts):
        visited = [0 for _ in range(len(accounts))]
        def dfs(v):
            if visited[v]: return []
            alts = [] # alternative accounts
            visited[v] = True
            for mail in accounts[v][1:]:
                for u in mail2account[mail]:
                    # if u == v: continue
                    ret = dfs(u)
                    alts += ret
            alts.append(v)
            return alts
        # build graph
        mail2account = defaultdict(list)
        for i, account in enumerate(accounts):
            for mail in account[1:]:
                mail2account[mail].append(i)
        accountsMerged = []
        for i, _ in enumerate(accounts):
            alts = dfs(i)
            if not alts: continue
            merged = [accounts[alts[0]][0]]
            emailList = []
            for alt in alts:
                emailList += accounts[alt][1:]
            emailList = list(set(emailList))
            emailList.sort()
            merged += emailList

            accountsMerged.append(merged)

        return accountsMerged

    # TODO: union find solution

def test():
    solution = Solution()

    accounts = []
    assert solution.accountsMerge(accounts) == []

    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"]]
    assert solution.accountsMerge(accounts) == [["John", "john00@mail.com", "johnsmith@mail.com"]]
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    assert solution.accountsMerge(accounts) == [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

    print("self test passed")

if __name__ == '__main__':
    test()
