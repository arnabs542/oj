'''
Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
    Although the above answer is in lexicographical order, your answer could be in any order you want.
    '''

'''
Solution:
    Similar to N-Queen problem.It can be solved with backtracking with recursion or depth-first search.
    '''

class Solution:
    # @return a list of strings,[s1,s2]
    def letterCombinations(self,digits):
        letter_map = {'2':"abc", '3':"def", '4':"ghi",
                      '5':"jkl", '6':"mno", '7':"pqrs",
                      '8':"tuv", '9':"wxyz"}

        n = len(digits)
        if n == 0:
            return []
        res = []
        s = ['']*n
        top = -1
        s[0]=(letter_map[digits[0]][0])
        top += 1
        while top >= 0:
            if top == n - 1:
                res.append(''.join(s))
                while s[top] == letter_map[digits[top]][len(letter_map[digits[top]])-1]:
                    top -= 1
                    if top == -1:
                        break

                s[top] = chr(ord(s[top])+1)
                #top += 1
                continue

            s[top+1]=letter_map[digits[top+1]][0]
            top += 1

        return res

if __name__ == "__main__":
    print(Solution().letterCombinations("243"))
