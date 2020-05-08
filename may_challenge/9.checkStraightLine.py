# ----------------------------------------------------------------------
# Name:        Check If It Is a Straight Line
# Author(s):   Trinity Nguyen
# ----------------------------------------------------------------------

"""
    You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
    Check if these points make a straight line in the XY plane.

    Example 1:
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: True

    Example 2:
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false
 

    Constraints:
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point

    Hint #1:
    If there're only 2 points, return true.

    Hint #2:
    Check if all other points lie on the line defined by the first 2 points.

    Hint #3:
    Use cross product to check collinearity.

"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (len(coordinates) <= 2):
            return True

        slope = 0
        for i in range(1, len(coordinates)):
            p1_x, p1_y = coordinates[i-1][0], coordinates[i-1][1]
            p2_x, p2_y = coordinates[i][0], coordinates[i][1]

            try:
                temp_slope = (p2_y - p1_y) / (p2_x - p1_x)
            except ZeroDivisionError:
                temp_slope = 0

            if i > 1 and slope != temp_slope:
                return False
            else:
                slope = temp_slope
        return True
