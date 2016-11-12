'''
273. Integer to English Words

Total Accepted: 22848
Total Submissions: 112022
Difficulty: Hard
Contributors: Admin

Convert a non-negative integer to its english words representation. Given input
is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Hint:

1. Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
1. Group the number by thousands (3 digits). You can write a helper function that takes a number
less than 1000 and convert just that chunk to words.
3. There are many edge cases. What are some good test cases? Does your code work with input
such as 0? Or 1000010? (middle chunk is zero and should not be printed out)

'''

class Solution(object):

    digit2word = {
        '0': ('', ''),
        '1': ('One', ''),
        '2': ('Two', 'Twenty'),
        '3': ('Three', 'Thirty'),
        '4': ('Four', 'Forty'),
        '5': ('Five', 'Fifty'),
        '6': ('Six', 'Sixty'),
        '7': ('Seven', 'Seventy'),
        '8': ('Eight', 'Eighty'),
        '9': ('Nine', 'Ninety'),
    }

    tens2word = {
        '10': 'Ten',
        '11': 'Eleven',
        '12': 'Twelve',
        '13': 'Thirteen',
        '14': 'Fourteen',
        '15': 'Fifteen',
        '16': 'Sixteen',
        '17': 'Seventeen',
        '18': 'Eighteen',
        '19': 'Nineteen',
    }

    magnitudes = ['', 'Thousand', 'Million', 'Billion']

    def chunkToWords(self, chunk):
        # XXX(done): parsing a 3-digit number one digit after another
        magnitudes = ['Hundred']
        n = len(chunk)
        words = []
        # hundred place
        if n == 3:
            if chunk[-n] != '0':
                words += [self.digit2word[chunk[-n]][0], 'Hundred']
            n -= 1

        if n == 2:
            # ten place
            if chunk[-n] == '1':
                words += [self.tens2word[chunk[-n:]]]
                return words
            elif chunk[-n] != '0':
                words += [self.digit2word[chunk[-n]][1]]
            n -= 1
        if n == 1 and chunk[-n] != '0':
            words.append(self.digit2word[chunk[-n]][0])
        return words

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # return self.numberToWords1(num)
        return self.numberToWordsMod(num)

    def numberToWords1(self, num):
        """
        :type num: int
        :rtype: str
        """
        words = []
        chunk_size = 3
        # group the number by chunks of size 3
        chunks = list(reversed([str(num)[max(0, i - chunk_size):i]
                                for i in range(len(str(num)), 0, -chunk_size)]))
        print(chunks)
        chunk_len = len(chunks)

        for i in range(-chunk_len, 0):
            chunk_words = self.chunkToWords(chunks[i])
            if chunk_words:
                chunk_words.append(self.magnitudes[-i - 1])
            words.extend(chunk_words)

        if not words:
            words.append('Zero')
        print(words)
        # print(' '.join(words).strip())
        return ' '.join(words).strip()

    def numberToWordsMod(self, num):
        '''
        Using modulo operation
        '''
        # XXX(done): parsing a number harnessing built-in modulo operation
        self.lessThan20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen"]
        self.tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

        if not num:
            return 'Zero'

        def helper(a):
            if a == 0:
                return []
            elif a < 20:
                return [self.lessThan20[a]]
            elif a < 100:
                return [self.tens[a // 10]] + helper(a % 10)
            else:
                return [self.lessThan20[a // 100], 'Hundred'] + helper(a % 100)

        words = []
        i = 0
        while num:
            num, remainder = divmod(num, 1000)
            if remainder:
                words = helper(remainder) + [self.thousands[i]] + words
            i += 1

        print(words)
        return ' '.join(words).strip()

def test():
    solution = Solution()
    assert solution.numberToWords(0) == 'Zero'
    assert solution.numberToWords(123) == 'One Hundred Twenty Three'
    assert solution.numberToWords(100003) == 'One Hundred Thousand Three'
    assert solution.numberToWords(
        12345) == "Twelve Thousand Three Hundred Forty Five"
    assert solution.numberToWords(
        1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    print('self test passed!')

if __name__ == '__main__':
    test()
