class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows - 1

        # Binary search over rows
        while top <= bottom:
            middle_vert = (top + bottom) // 2
            row = matrix[middle_vert]

            if target < row[0]:
                # target smaller than smallest in row, search top half
                bottom = middle_vert - 1
                continue
            elif target > row[-1]:
                # target bigger than largest in row, search bottom half
                top = middle_vert + 1
                continue
            else:
                # target in the row
                left = 0
                right = cols - 1
                while left <= right:
                    middle_hor = (left + right) // 2
                    if row[middle_hor] == target:
                        return True
                    elif row[middle_hor] < target:
                        left = middle_hor + 1
                    else:
                        right = middle_hor - 1
                # searched the only possible row, not found
                return False
        return False
