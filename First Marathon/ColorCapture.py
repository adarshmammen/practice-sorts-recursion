import random
def getColor(c):
    return ord(c) - ord('A')
class ColorCapture:
    def __init__(self):
        random.seed(12345)
    def makeTurn(self, board, timeLeftMs):
        D = len(board)
        # get list of all colors present on the board adjacent to area controlled by player
        # bfs starting with corner cell already controlled by player
        r = [0] * (D * D)
        c = [0] * (D * D)
        vis = [[False for x in range(D)] for y in range(D)]
        n = 0
        incase = 0
        r0 = c0 = 0
        playerColor = board[r0][c0]
        vis[r0][c0] = True
        r[n] = r0
        c[n] = c0
        n += 1

        colors = set();
        maxC = 4
        dr = (0, 1, 0, -1)
        dc = (-1, 0, 1, 0)
        ind = 0
        while ind < n:
            for d in range(4):
                newr = r[ind] + dr[d]
                newc = c[ind] + dc[d]
                if newr < 0 or newc < 0 or newr >= D or newc >= D:
                    continue

                if not vis[newr][newc]:
                    if board[newr][newc] == playerColor:
                        vis[newr][newc] = True
                        r[n] = newr
                        c[n] = newc
                        n += 1
                    else:
                        # adjacent to one of player's cells but of different color - keep
                        col = getColor(board[newr][newc])
                        colors.add(col)
                        if (col > maxC):
                            maxC = col
            ind += 1
        incase = sum(x.count(True) for x in vis)
        # can't switch to colors currently used by players
        col0 = getColor(board[0][0])
        col1 = getColor(board[D - 1][D - 1])
        colors.discard(col0)
        colors.discard(col1)
        # Reducing from NP hard
        if colors:
			temp = list(colors)
			if D <=10:
				return max(set(temp),key=temp.count)

			elif D<=30:
				if incase%4==0:
					return temp[len(temp)//2]
				elif incase%4==2:
					return temp[-1]
				else:
					return max(set(temp),key=temp.count)
			else:
				if incase <=int(D*D*0.50):
					if incase%5==0 or incase%5==2:
						return temp[len(temp)//2]
					elif incase%5==4:
						return temp[-1]
					else:
						return max(set(temp),key=temp.count)
				else:
					return max(set(temp),key=temp.count)									



        # if there are no good moves, do something
        cret = random.randrange(maxC - 2)
        if cret >= min(col0, col1):
            cret += 1
        if cret >= max(col0, col1):
            cret += 1
        return cret
# -------8<------- end of solution submitted to the website -------8<-------

import sys
while True:
    cc = ColorCapture()
    N = int(raw_input())
    board = [""] * N
    for i in range(N):
        board[i] = raw_input().strip()
    timeLeftMs = int(raw_input())
    ret = cc.makeTurn(board, timeLeftMs)
    print ret
    sys.stdout.flush()
