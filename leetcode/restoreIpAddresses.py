'''
Restore IP Addresses

Given a string containing only digits, restore it by returning all
possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''

'''
SOLUTION:
    1:backtrace
'''


class Solution:
    # @param s,a string
    # @return a list of strings

    def restoreIpAddresses(self, s):
        addrs = []
        l = len(s)
        a = [-1] * 4
        a[0] = 0
        top = 1
        while True:
            if a[top] == -1:
                a[top] = a[top - 1] + 1
            else:
                a[top] = a[top] + 1
            if self.isValidNumber(s[a[top - 1]:a[top]]):
                top += 1
                if top == 4:
                    # found a solution
                    valid = self.isValidNumber(s[a[top - 1]:l])
                    if valid:
                        ip = ''
                        ip = ip + s[a[0]:a[1]]
                        ip = ip + '.' + s[a[1]:a[2]]
                        ip = ip + '.' + s[a[2]:a[3]]
                        ip = ip + '.' + s[a[3]:l]
                        # s.insert()
                        addrs.append(ip)
                    else:
                        pass
                    top -= 1
            else:
                a[top] = -1
                top -= 1
                if top == 0:
                    return addrs

    def isValidNumber(self, s):
        if s[0] == '0':
            return False
        if int(s) > 255:
            return False
        return True

if __name__ == "__main__":
    print Solution().restoreIpAddresses("25525511135")
    print Solution().restoreIpAddresses("2552511135")
