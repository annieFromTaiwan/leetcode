class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        turn = 1
        for i, j in moves:
            r[i] += turn
            c[j] += turn
            if i == j:
                d[0] += turn
            if i+j == 2:
                d[1] += turn
            if (3*turn) in (r[i], c[j], d[0], d[1]):
                return 'A' if turn == 1 else 'B'
            turn *= -1
        return 'Draw' if len(moves) == 9 else 'Pending'
