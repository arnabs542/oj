#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
468. Validate IP Address

Total Accepted: 6325
Total Submissions: 30777
Difficulty: Medium
Contributors: Cyber233

Write a function to check whether an input string is a valid IPv4 address or IPv6 address
or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four
decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group
representing 16 bits. The groups are separated by colons (":"). For example, the address
2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading
zeros among four hexadecimal digits and some low-case characters in the address to upper-case
ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and
using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using
two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334
is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address
02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.

==============================================================================================
SOLUTION

1. String processing

2. Regular expression

'''

import re

class Solution(object):

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        result = self.validIPAddressRule(IP)
        print(result)
        return result

    def validIPAddressRule(self, IP):
        if not IP:
            return "Neither"
        groups = IP.split('.')
        if len(groups) == 4:
            for part in groups:
                if not self._validGroup4(part):
                    return 'Neither'
            return "IPv4"

        groups = IP.split(':')
        if len(groups) == 8:
            for part in groups:
                if not self._validGroup6(part):
                    return 'Neither'
            return 'IPv6'
        return "Neither"

    def _validGroup4(self, s):
        '''
        valid IPv4 group or not
        '''
        if not s:
            return False
        if not s.isdecimal():
            return False
        n = int(s)
        if n > 255:
            return False
        return (n > 0 and not s.startswith('0')) or (n == 0 and len(s) == 1)

    def _validGroup6(self, s):
        s = s.lower()
        # be aware of space in RE!
        m = re.match(r'^[0-9a-f]{1,4}$', s)
        return m is not None

    def validIPAddressRE(self, IP):
        # TODO: regular expression solution
        return

def test():
    solution = Solution()

    assert solution.validIPAddress("172.16.254.1") == 'IPv4'
    assert solution.validIPAddress("172.16.254.01") == 'Neither'
    assert solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") == 'IPv6'
    assert solution.validIPAddress("02001:0db8:85a3:0:0:8A2E:0370:7334") == 'Neither'
    assert solution.validIPAddress("256.256.256.256") == 'Neither'

    print("self test passed")

if __name__ == '__main__':
    test()
