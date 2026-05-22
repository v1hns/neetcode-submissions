class Solution:
    def rowchecker(self, board):
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in s: return False
                    else: s.add(board[i][j])
        return True

    def colchecker(self, board):
        board2 = [['' for i in range(9)] for i in range(9)]
        print(board2)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board2[j][i] = board2[j][i] + board[i][j]
        return self.rowchecker(board2)
    
    def boxchecker(self, board):
        board2 = [[] for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                bi = i // 3
                bj = j // 3
                n = bi + bj * 3
                board2[n].append(board[i][j])
        return self.rowchecker(board2)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.rowchecker(board) and self.colchecker(board) and self.boxchecker(board)