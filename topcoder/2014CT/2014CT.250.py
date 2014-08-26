

class WaiterTipping:

    def maxPercent(self, total, taxPercent, money):
        l = 0
        r = 100 * money / total
        while l <= r:
            md = (l + r) >> 1
            if self.checkEnough(total, taxPercent, money, md):
                l = md + 1
            else:
                r = md - 1
        return r
       # return (money - total - int(total * taxPercent / 100)) * 100 / total

    def checkEnough(self, total, taxPercent, money, tip):
        if total + int(total * taxPercent / 100) + total * tip / 100 <= money:
            return True
        else:
            return False

if __name__ == "__main__":
    print WaiterTipping().maxPercent(500, 10, 600)
    print WaiterTipping().maxPercent(226, 48, 584)
    print WaiterTipping().maxPercent(850, 8, 870)
    print WaiterTipping().maxPercent(226, 48, 584)
    print WaiterTipping().maxPercent(123, 52, 696)
    print WaiterTipping().maxPercent(500, 10, 550)
