# -*- coding: utf-8 -*-
'''
Valid Number

Validate if a given string is numeric.

Some examples:

"0" => true

" 0.1 " => true

"abc" => false

"1 a" => false

"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You
should gather all requirements up front before implementing one.
'''

'''
Solution:
    @1:
        1.Beginning and trailing white spaces can be left out
        2.The most complex situation is when a number is in scientific
        notation:
            <float number>e<integer>

    AeB or AEB代表A * 10 ^ B
    A可以是小数也可以是整数，可以带正负号
    .35, 00.等的都算valid小数；就'.'单独一个不算
    B必须是整数，可以带正负号
    有e的话，A,B就必须同时存在

    @2 finite automata
        To construct a finite automata transition diagram.We classify the
        states:
            0:initial state
            1:sign
            2:digit
            3:point
            4:point and digit
            5:'e' or 'E'
            6:sign after 'e' or 'E'
            7:digit after 5
            8:space after 7
'''


class Solution:
    # @param s, a string
    # @return a boolean

    def isNumber(self, s):
        state = 0
        for i in xrange(0, len(s)):
            state = self.nextState(state, s[i])
            if state == -1:
                return False
        # To finish the state transition manually
        state = self.nextState(state, ' ')
        return state == 8

    def nextState(self, state, char):
        # transition function
        #               0space,1digit,2sign,3dot,4e,5il
        transititionTable = [[0, 2,  1,  3, -1, -1],  # 0
                             [-1, 2, -1,  3, -1, -1],  # 1
                             [8, 2, -1,  4,  5, -1],  # 2
                             [-1, 4, -1, -1, -1, -1],  # 3
                             [8, 4, -1, -1,  5, -1],  # 4
                             [-1, 7,  6, -1, -1, -1],  # 5
                             [-1, 7, -1, -1, -1, -1],  # 6
                             [8, 7, -1, -1, -1, -1],  # 7
                             [8, -1, -1, -1, -1, -1]]  # 8
        return transititionTable[state][self.getSymbol(char)]

    def getSymbol(self, char):
        if char == ' ' or char == '\t':
            return 0
        if char.isdigit():
            return 1
        if char == '+' or char == '-':
            return 2
        if char == '.':
            return 3
        if char == 'E' or char == 'e':
            return 4
        return 5

if __name__ == "__main__":
    print "-.5364764e+3 is %s" % Solution().isNumber("-.5364764e+3")
    print "-34342.e-3 is %s" % Solution().isNumber("-34342.e-3")
