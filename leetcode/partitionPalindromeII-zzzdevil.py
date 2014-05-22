class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        """
        Input: a string s[0..n-1], where n = len(s)

        DP solution: use an array B[0..n-1]
        B[i] presents a list of break positions for string s[0..i].
        In the list B[i], each break position j (0 < j < i) means
        s[0..i] = s[0..j-1] + s[j..i] where s[0..j] can be partitioned
        into palindromes and s[j+1..i] is a palindrome.
        Note that B[i]=[] means s[0..i] cannot be partitioned into palindromes,
        and 0 in B[i] means s[0..i] is a palindrome.

        Additional we may need a 2D boolean array P[0..n-1][0..n-1] to tell if s[i..j-1] is a palindromes
        """
        n = len(s)
        # Special case: s is ""
        if n == 0:
            return []

        # P[i][j] denotes whether s[i..j] is a palindrome
        P = []
        for _ in xrange(n):
            P.append([False]*n)
            # Compute P[][], T(n) = O(n^2) and S(n) = O(n^2)
            for mid in xrange(n):
                P[mid][mid] = True
                # Check strings with the mid of s[mid]
                i = mid - 1
                j = mid + 1
                while i >= 0 and j < n and s[i] == s[j]:
                    P[i][j] = True
                    i -= 1
                    j += 1
                    # Check strings with mid "s[mid]s[mid+1]"
                    i = mid
                    j = mid + 1
                    while i >= 0 and j < n and s[i] == s[j]:
                        P[i][j] = True
                        i -= 1
                        j += 1

        # Compute B[]
        B = [None] * n
        for i in xrange(0, n):
            if P[0][i]:
                B[i] = [0]
            else:
                B[i] = []
                # s[0 .. i] = s[0 .. j-1] + s[j .. i]
                j = 1
                while j <= i:
                    if B[j-1] != [] and P[j][i]:
                        B[i].append(j)
                        j += 1

        # BFS in the graph
        res = []
        # Last breaks
        breaks = [ [x, n] for x in B[n-1] ]
        while breaks:
            temp = []
            for lst in breaks:
                if lst[0] == 0:
                    res.append([ s[lst[i]:lst[i+1]] for i in xrange(len(lst)-1) ])
                else:
                    # s[0..i] = s[0..j-1] + s[j..i]
                    for j in B[lst[0]-1]:
                        temp.append([j]+lst)
                        breaks = temp
                        return res

if __name__ == "__main__":
    print Solution().partition("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")
