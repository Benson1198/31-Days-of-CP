class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ans = True
        if len(coordinates) == 2:
            return ans
        else:
            x1 = coordinates[0][0]
            x2 = coordinates[1][0]
            y1 = coordinates[0][1]
            y2 = coordinates[1][1]

            

            for i in range(2,len(coordinates)):
                x = coordinates[i][0]
                y = coordinates[i][1]
                lhs = (y2-y1)*(x-x1)
                rhs = (y-y1)*(x2-x1)
                if lhs != rhs:
                    ans = False
                    break
        return ans