class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        l=len(board)
        board.reverse()
        def intpos(sq) :
            r = (sq-1) // l 
            c = (sq-1) % l
            if r%2 :
                c = l-1-c
            return [r,c]
        q=deque()
        vis=set()
        q.append([1,0])
        while q :
            sqr,mov = q.popleft()
            for i in range(1,7) :
                nxtsqr = sqr + i 
                r,c = intpos (nxtsqr)
                if board[r][c] != -1 :
                    nxtsqr=board[r][c]
                if nxtsqr == l*l :
                    return mov+1
                if nxtsqr not in vis :
                    vis.add(nxtsqr)
                    q.append([nxtsqr,mov+1])
        return -1