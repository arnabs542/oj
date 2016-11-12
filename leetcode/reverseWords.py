'''
Reverse Words in a String
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

click to show clarification.

Clarification:
    What constitutes a word?
    A sequence of non-space characters constitutes a word.
    Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or
    trailing spaces.
    How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.
    '''

class Solution:
    # @param s, a string
    # @return a string

    def reverseWords(self, s):
        if not isinstance(s, str):
            raise TypeError
        #words = s.split(' ')
        words = s.split()
        j = 0
        for i in range(len(words) - 1, j, -1):
            # print '%d,words[%d] is %s' % (j,i,words[i])
            # comment out debug outputs,which may cause "Output limit exceeded"
            # error on OJ
            if i <= j:
                break
            if words[i] != ' ':
                if words[j] != ' ':
                    tmp = words[j]
                    words[j] = words[i]
                    words[i] = tmp
                    j = j + 1
                else:
                    #words.remove(' ')
                    del words[i]
            else:
                words.remove(' ')

        new_s = ' '.join(words)
        return new_s

if __name__ == "__main__":
    a = Solution()
    ra = a.reverseWords('hello world    My name is onerhao')
    print(ra)
