class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Track current box
        currentBox = 0

        # Hashes for each number freq count: row, col, and box
        rowHash = {}
        colHash = {}
        boxHash = {}

        for rowInd in range(len(board)):
            row = board[rowInd]
            for colInd in range(len(row)):
                number = row[colInd]
                if number == ".": continue
                boxInd = (colInd // 3) + 3 * (rowInd // 3)

                if (rowInd, number) in rowHash:
                    return False
                rowHash[(rowInd, number)] = True
                if (colInd, number) in colHash:
                    return False
                colHash[(colInd, number)] = True
                if (boxInd, number) in boxHash:
                    return False
                boxHash[(boxInd, number)] = True
        return True