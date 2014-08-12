'''
Valid Number

Validate if a given string is numeric.

Some examples:

"0" => true

" 0.1 " => true

"abc" => false

"1 a" => false

"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
'''

'''
Solution:
    1.Beginning and trailing white spaces can be left out
    2.The most complex situation is when a number is in scientific notation:
        <float number>e<integer>
'''
