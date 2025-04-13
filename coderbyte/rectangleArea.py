# /****************************************************************
#  *             CODERBYTE RECTANGLE AREA CHALLENGE               *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function RectangleArea(strArr) take the array of    *
#  * strings stored in strArr, which will only contain 4 elements *
#  * and be in the form (x y) where x and y are both integers, and*
#  * return the area of the rectangle formed by the 4 points on a *
#  * Cartesian grid. The 4 elements will be in arbitrary order.   *
#  * For example: strArr is ["(0 0)", "(3 0)", "(0 2)", "(3 2)"]  *
#  * then your program should return 6 because the width of the   *
#  * rectangle is 3 and the height is 2 and the area of a         *
#  * rectangle is equal to the width * height.                    *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: ["(1 1)","(1 3)","(3 1)","(3 3)"]                   *
#  * Output 1: 4                                                  *
#  *                                                              *
#  * Input 2: ["(0 0)","(1 0)","(1 1)","(0 1)"]                   *
#  * Output 2: 1                                                  *
#  *                                                              *
#  ***************************************************************/

def RectangleArea(strArr):
    points = []
    for point in strArr:
        x, y = map(int, point[1:-1].split())
        points.append((x, y))

    width = max(x for x, y in points) - min(x for x, y in points)
    height = max(y for x, y in points) - min(y for x, y in points)
    area = width * height
    return area

print(RectangleArea(["(0 0)", "(3 0)", "(0 2)", "(3 2)"]))  # Output: 6
print(RectangleArea(["(1 1)", "(1 3)", "(3 1)", "(3 3)"]))  # Output: 4
print(RectangleArea(["(0 0)", "(1 0)", "(1 1)", "(0 1)"]))  # Output: 1