import numpy as np

board = np.zeros((4, 4))    # 棋盘
t = 0   # 骨牌编号

def chess_board(tr, tc, dr, dc, size):
    '''
    @param:
        tr、tr : 最左上角坐标
        dr、dc : 特殊方块坐标
        size : 棋盘大小（最右边边界位置）
    '''
    global t    # 骨牌编号
    global board    # 棋盘
    
    if size == 1:   # 棋盘大小为 1 
        return
    t1 = t + 1  # 编号增加
    t = t1
    s = size // 2   # 分割棋盘（分治法）
    
    if dr < tr + s and dc < tc + s: # 当特殊方块在左上角
        chess_board(tr, tc, dr, dc, s)  # 递归进入左上角
    else:
        board[tr + s - 1][tc + s - 1] = t1  # 最右下角填入骨牌
        chess_board(tr, tc, tr+s-1, tc+s-1, s)  # 递归子棋盘
    
    if dr < tr + s and dc >= tc + s:
        chess_board(tr, tc+s, dr, dc, s)
    else:
        board[tr + s - 1][tc + s] = t1
        chess_board(tr, tc+s, tr+s-1, tc+s, s)
    
    if dr >= tr + s and dc < tc + s:
        chess_board(tr+s, tc, dr, dc, s)
    else:
        board[tr + s][tc + s - 1] = t1
        chess_board(tr+s, tc, tr+s, tc+s-1, s)
    
    if dr >= tr + s and dc >= tc + s:
        chess_board(tr+s, tc+s, dr, dc, s)
    else:
        board[tr + s][tc + s] = t1
        chess_board(tr+s, tc+s, tr+s, tc+s, s)

chess_board(0, 0, 1, 1, 4)
print(board)