#
# defines.py
# ChessPy
# 
#   Created by Yuval Atir

white_piece, black_piece, piece_color_undefined = range(1,4)
nada, king, queen, rook, bishop, knight, pawn = range(0,7)

white_pieces = { 
                
    king   : "{Wking}  ", 
    queen  : "{Wquen}  ",
    rook   : "{Wrook}  ",
    bishop : "{Wbshp}  ",
    knight : "{Wknit}  ",
    pawn   : "{Wpawn}  ",
    
    }

black_pieces = { 
                
    king   : "[Bking]  ", 
    queen  : "[Bquen]  ",
    rook   : "[Brook]  ",
    bishop : "[Bbshp]  ",
    knight : "[Bknit]  ",
    pawn   : "[Bpawn]  ",
    
}