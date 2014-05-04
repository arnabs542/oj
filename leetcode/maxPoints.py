'''
Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Line:
    def __init__(self,a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
        def __init__(self,k=0,b=0):
            self.k = 0
            self.b = 0


class Solution:
    @classmethod
    def gcd(cls,a,b):
        a = abs(a)
        b = abs(b)
        if b > 0:
            return Solution.gcd(b, a % b)
        else:
            return a

    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        rmax = 0
        if len(points) <= 2:
            return len(points)
        for i in range(len(points)):
            # temperary maximum
            tmax = 0
            same = 1
            lines = dict()
            for j in range(i+1,len(points),1):
                #dx = points[j].x-points[i].x
                dx = points[j][0]-points[i][0]
                #dy = points[j].y-points[i].y
                dy = points[j][1]-points[i][1]

                g = Solution.gcd(dx,dy)
                #print "dx: %d,dy: %d,gcd: %d"%(dx,dy,g)
                if g != 0:
                    dx /= g
                    dy /= g
                    if dx == 0 or dy == 0:
                        dx = abs(dx)
                        dy = abs(dy)
                    else:
                        flag = dx/abs(dx)
                        dx /= flag
                        dy /= flag

                    if lines.has_key((dx,dy)):
                        lines[(dx,dy)] = lines[(dx,dy)] + 1
                    else:
                        lines[(dx,dy)] = 1

                    tmax = max(tmax,lines[(dx,dy)])
                    #print "(%d,%d): %d,tmax: %d"%(dx,dy,lines[(dx,dy)],tmax)

                else:
                    dx = 0
                    dy = 0
                    same = same + 1
                    #print "same: %d"%same



            rmax = max(tmax + same,rmax)

        return rmax

if __name__ == "__main__":
    print Solution().maxPoints([(3,1),(12,3),(3,1),(-6,-1)])
    #print Solution().maxPoints([(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)])
    #print Solution().maxPoints([(2,3),(3,3),(-5,3)])
    print Solution().maxPoints([(-4,1),(-7,7),(-1,5),(9,-25)])
