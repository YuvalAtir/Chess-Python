#
#  chessboard.py
#  ChessPy
#
#  Created by Yuval Atir
#

import defines
import piece
#from time import time
from tkinter import *
from tkinter import ttk #, messagebox
#from itertools import permutations

class Chessboard():
        
    def __init__(self, master):
    
        self._turn = 1
        self.n = 8    # length checkers on board
        self.wking_loc = [0]*2
        self.wking_loc[0] = 7
        self.wking_loc[1] = 4
        self.bking_loc = [0, 4]
        
#       self.game_board = [[piece.EmptyPiece()]*8]*8                                WRONG, duplicates the 1D list 8 times (same lists)
#       self.game_board = { (pp,qq):0 for pp in range(8) for qq in range(8) }       if were using a dictionary
        self.game_board = [ [ piece.EmptyPiece() for pp in range(8) ] for qq in range(8) ]        
    
        for s in range(0,8):
            self.game_board[6][s] = piece.Pawn(defines.white_piece, defines.pawn)
            self.game_board[1][s] = piece.Pawn(defines.black_piece, defines.pawn)

        self.game_board[7][4] = piece.King(defines.white_piece,defines.king)
        self.game_board[0][4] = piece.King(defines.black_piece,defines.king)
        self.game_board[7][3] = piece.Queen(defines.white_piece, defines.queen)
        self.game_board[0][3] = piece.Queen(defines.black_piece, defines.queen)
        self.game_board[7][0] = piece.Rook(defines.white_piece, defines.rook)
        self.game_board[0][0] = piece.Rook(defines.black_piece, defines.rook)
        self.game_board[7][7] = piece.Rook(defines.white_piece, defines.rook)
        self.game_board[0][7] = piece.Rook(defines.black_piece, defines.rook)  
        self.game_board[7][2] = piece.Bishop(defines.white_piece, defines.bishop)
        self.game_board[0][2] = piece.Bishop(defines.black_piece, defines.bishop)
        self.game_board[7][5] = piece.Bishop(defines.white_piece, defines.bishop)
        self.game_board[0][5] = piece.Bishop(defines.black_piece, defines.bishop)
        self.game_board[7][6] = piece.Knight(defines.white_piece, defines.knight)
        self.game_board[0][6] = piece.Knight(defines.black_piece, defines.knight)
        self.game_board[7][1] = piece.Knight(defines.white_piece, defines.knight)
        self.game_board[0][1] = piece.Knight(defines.black_piece, defines.knight)



        # Graphics        
        self.master = master
        self.master.title('ChessPy')
        self.master.configure(background = '#e1d8b9')
        self.master.minsize(400, 470)
        self.master.resizable(True, True)                
        self.master.bind('<Configure>', lambda e: self.draw_board())   # call draw_board() in the event of new Hight and Width window size

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9')

        self.board_canvas = Canvas(self.master)  # used to draw shapes: line, oval,...
        self.board_canvas.pack()   

        self.controls_frame = ttk.Frame(self.master)
        self.controls_frame.pack(side = TOP, pady = 20)

        
        self.n_var = StringVar()
        self.n_var.set(self.n)
#         Spinbox(self.controls_frame, from_ = 4, to = 99, width = 2,
#                 font = 'Verdana 10 bold', textvariable = self.n_var).grid(row = 0, column = 1)


        self.from_row_var = StringVar()       
        self.from_col_var = StringVar()
        self.to_row_var = StringVar()       
        self.to_col_var = StringVar()
        #self.to_col_var.set('0')
        
        """ location entry widgets """
        ttk.Label(self.controls_frame, text = 'Move From Row:',
            font = 'Verdana 10 bold').grid(row = 0, column = 0, sticky= (W),padx=10) # , sticky= (E)
        self.from_row_entry = ttk.Entry(self.controls_frame, width=10, #textvariable = self.from_row_var,
            font = 'Verdana 10') #, sticky = (W)
        self.from_row_entry.grid(row = 0, column = 1, sticky= (W))
               
        ttk.Label(self.controls_frame, text = 'Move From Column:',
            font = 'Verdana 10 bold').grid(row = 1, column = 0, sticky= (W),padx=10)
        self.from_col_entry = ttk.Entry(self.controls_frame, width=10, #textvariable = self.from_col_var,
            font = 'Verdana 10')
        self.from_col_entry.grid(row = 1, column = 1, sticky = (W))
             
        ttk.Label(self.controls_frame, text = 'Move To Row:',
            font = 'Verdana 10 bold').grid(row = 2, column = 0, sticky= (W),padx=10)
        self.to_row_entry = ttk.Entry(self.controls_frame, width=10, #textvariable = self.to_row_var,
            font = 'Verdana 10')
        self.to_row_entry.grid(row = 2, column = 1, sticky = (W))
             
        ttk.Label(self.controls_frame, text = 'Move To Column:',
            font = 'Verdana 10 bold').grid(row = 3, column = 0, sticky= (W),padx=10)
        self.to_col_entry = ttk.Entry(self.controls_frame, width=10, #textvariable = self.to_col_var,
            font = 'Verdana 10')       
        self.to_col_entry.grid(row = 3, column = 1, sticky = (W))  
        
#         self.from_row_entry.pack()
#         self.from_col_entry.pack()
#         self.to_row_entry.pack()
#         self.to_col_entry.pack()
#         
        self.from_row_entry["textvariable"] = self.from_row_var
        self.from_col_entry["textvariable"] = self.from_col_var
        self.to_row_entry["textvariable"] = self.to_row_var
        self.to_col_entry["textvariable"] = self.to_col_var
        
        # and here we get a callback when the user hits return.
        #self.to_col_entry.bind('<Key-Return>',self.move_callback)
        #self.to_col_var.get()
        
        """ Move button """ 
        ttk.Button(self.controls_frame, text = 'Enter Move',
           command = self.move_callback).grid(row = 4, column = 1, columnspan = 2, sticky = (W), padx = 10, pady = 10)  
        
        ttk.Label(self.controls_frame, text = 'to exit type q',
                  font = 'Verdana 8').grid(row = 7, column = 0, sticky= (W),pady=10) # , sticky= (E)    
#         ttk.Label(self.controls_frame).grid(row = 0, column = 2, padx = 10) # spacer
        
        turn_color = "WHITE" if self._turn == 1 else "BLACK"
        ttk.Label(self.controls_frame, text = turn_color + ' turn',
                  font = 'Verdana 8').grid(row = 6, column = 0, sticky= (W),pady=10)
                  
        self.draw_board()
    

    def draw_board(self):             
        maxboardsize = min(self.master.winfo_height() - 70, self.master.winfo_width())
        cellsize = maxboardsize // self.n
        self.board_canvas.config(height = self.n*cellsize, width = self.n*cellsize)      
        #self.board_canvas.delete('all')

        # color in black board cells
        for row in range(self.n):
            for col in range(self.n):
                if ((row % 2) and (col % 2) or
                    (not (row % 2) and not (col % 2)) ): # black cell
                    self.board_canvas.create_rectangle(row*cellsize, col*cellsize,
                        row*cellsize+cellsize, col*cellsize+cellsize, fill = 'black')
                else:
                    self.board_canvas.create_rectangle(row*cellsize, col*cellsize,
                        row*cellsize+cellsize, col*cellsize+cellsize, fill = '#e1d8b9' )

        for row in range(self.n):
            for col in range(self.n):
                if ( self.game_board[row][col].get_color() == defines.black_piece ):
                    color_fore_str = 'blue'
                elif ( self.game_board[row][col].get_color() == defines.white_piece ):
                    color_fore_str = 'orange'
                else:
                    color_fore_str = 'white'
    
                if (self.game_board[row][col].get_type() == defines.king):
                    # draw a king  
                    self.board_canvas.create_text(col*cellsize+cellsize//2, row*cellsize+cellsize//2,
                        text = u'\u265A', font = ('Arial', cellsize//2), fill = color_fore_str)
                elif (self.game_board[row][col].get_type() == defines.queen):
                    # draw a queen  
                    self.board_canvas.create_text(col*cellsize+cellsize//2, row*cellsize+cellsize//2,
                        text = u'\u265B', font = ('Arial', cellsize//2), fill = color_fore_str)
                elif (self.game_board[row][col].get_type() == defines.rook):
                    # draw a rook  
                    self.board_canvas.create_text(col*cellsize+cellsize//2, row*cellsize+cellsize//2,
                        text = u'\u265C', font = ('Arial', cellsize//2), fill = color_fore_str)
                elif (self.game_board[row][col].get_type() == defines.bishop):
                    # draw a bishop  
                    self.board_canvas.create_text(col*cellsize+cellsize//2, row*cellsize+cellsize//2,
                        text = u'\u265D', font = ('Arial', cellsize//2), fill = color_fore_str)
                elif (self.game_board[row][col].get_type() == defines.knight):
                    # draw a knight  
                    self.board_canvas.create_text(col*cellsize+cellsize//2, row*cellsize+cellsize//2,
                        text = u'\u265E', font = ('Arial', cellsize//2), fill = color_fore_str)
                elif (self.game_board[row][col].get_type() == defines.pawn):
                    # draw a pawn  
                    self.board_canvas.create_text(col*cellsize+cellsize//2, row*cellsize+cellsize//2,
                        text = u'\u265F', font = ('Arial', cellsize//2), fill = color_fore_str)    
                else:
                    pass  
                          
    
    def move_callback(self):
                
        def check_n_convert(usr_in_str):
            
            input_val = int(usr_in_str.get()) 
            
            if ( usr_in_str.get() in ('x', 'q' ) ):
                messagebox.showerror(title = 'User Exit',
                                     message = 'Exit Chess')
                
            try:  
                if ( input_val < 0 or input_val > 7 ):
                    print("Not in range (0,7)")
            except:
                    messagebox.showerror(title = 'Invalid Input',
                                         message = 'Must enter a number')
            
    
        turn_color = "WHITE" if self._turn == 1 else "BLACK"
        ttk.Label(self.controls_frame, text = turn_color + ' turn',
                  font = 'Verdana 8').grid(row = 6, column = 0, sticky= (W),pady=10)
                  
        from_row = int(self.from_row_var.get())
        from_col = int(self.from_col_var.get())
        to_row = int(self.to_row_var.get())
        to_col = int(self.to_col_var.get())
        
        if ( self.get_piece(from_row,from_col).get_color() != self._turn ):
            ttk.Label(self.controls_frame, text = 'pick a ' + turn_color + ' piece       ',
                  font = 'Verdana 8').grid(row = 5, column = 0, sticky= (W),pady=10)
            return
    
        if  ( self.get_piece(from_row,from_col).get_type() == defines.nada ):
            ttk.Label(self.controls_frame, text = 'pick a piece               ',
                  font = 'Verdana 8').grid(row = 5, column = 0, sticky= (W),pady=10)
            return
    
        if self.move_piece(from_row,from_col, to_row, to_col):
            self._turn = defines.black_piece if self._turn == defines.white_piece else defines.white_piece         # change turn
            turn_color = "WHITE" if self._turn == 1 else "BLACK"
            ttk.Label(self.controls_frame, text = turn_color + ' turn',
                  font = 'Verdana 8').grid(row = 6, column = 0, sticky= (W),pady=10)
        else:
            ttk.Label(self.controls_frame, text = 'pick another piece              ',
                  font = 'Verdana 8').grid(row = 5, column = 0, sticky= (W),pady=10)

        self.draw_board()
        
    
    def get_piece(self,row,col):
        
        return self.game_board[row][col]
    
    def insert_piece(self,in_piece, row, col):

        if (row < 0 or row > 7 or col < 0 or col > 7 ):
            print("Out of bounds")
            return False
    
    
        if ( self.game_board[row][col].get_type() != defines.nada ): 
            print("illegal place: allready occupied")
            #cin.ignore()
            return False
    
            self.game_board[row][col] = in_piece
            return True


    def move_piece(self,from_row, from_col, to_row,  to_col):

        if ( self.get_piece(from_row, from_col).get_type() != defines.nada):
    
            if ( self.get_piece(from_row, from_col).is_legal(from_row, from_col, to_row, to_col) ):
                if ( self.is_legal_board(from_row, from_col, to_row, to_col) ):
    
                    if ( ( self.get_piece(to_row,to_col).get_type() != defines.pawn ) or
                            ( ( self.get_piece(to_row,to_col).get_type() == defines.pawn ) and
                                    ( self.get_piece(to_row,to_col).get_type() != defines.nada ) ) ):
                    
                        self.game_board[to_row][to_col] = self.get_piece(from_row,from_col)
                        self.game_board[from_row][from_col] = piece.EmptyPiece()
                        return True
            
            if ( self.get_piece(from_row, from_col).get_type() == defines.pawn ):
                if ( self.get_piece(from_row, from_col).is_legal_pawn_kill(self, from_row,from_col,to_row,to_col)==1 ): 
                    self.game_board[to_row][to_col] = self.get_piece(from_row,from_col)
                    self.game_board[from_row][from_col] = piece.EmptyPiece()
                    return True    
        
        ttk.Label(self.controls_frame, text = 'Illegal move           ',
                  font = 'Verdana 8').grid(row = 4, column = 0, sticky= (W),pady=10)
        return False


    def is_legal_board(self,from_row,from_col,to_row,to_col): # const

        def is_legal_board_rook():
            
            z = 0   # y,z == sign
            if ( to_row == from_row ):
                x_range = abs( to_col - from_col )
                z = (to_col - from_col ) // abs( to_col - from_col )                              #sign col,can be 0
            elif  ( to_col == from_col ):
                x_range = abs( to_row - from_row )
                y = ( to_row - from_row ) // abs( to_row - from_row )                             #sign row,can be 0    
            else:
                return False 

            for x in range(0,x_range):                                                                  # both axis'

                if ( self.game_board[from_row+y*x][from_col+z*x].get_type() != defines.nada ):
                    if ( self.game_board[from_row][from_col].get_type() == defines.rook ):
                        return False;
                    else:                                                                                # which means its a queen
                        if ( y == 0 or z == 0 ):
                            return False                                                                 # not diagonal
                return True
    
        def is_legal_board_bishop():
            
            for r in range(1,8):
                cond = r < abs( to_row - from_row ) and r < abs( to_col - from_col )
                if not cond: break
                y = ( to_row - from_row ) // abs( to_row - from_row )                                         #sign row,can be 0
                z = ( to_col - from_col ) // abs( to_row - from_row )                                        #sign row,can be 0
                if ( self.game_board[from_row+y*r][from_col+z*r].get_type() != defines.nada ):
                    return False
            return True                

        def is_legal_board_queen():
            
            if is_legal_board_bishop() or is_legal_board_rook():
                return True
            else:
                return False
        
        def is_legal_board_pawn():
            
            if ( self.game_board[from_row][from_col].get_color() == defines.white_piece):
                if ( ( from_row == 6 ) and ( self.game_board[5][from_col].get_type() != defines.nada ) ):
                    return False
            else:                                                                                               # black
                if ( ( from_row == 1 ) and ( self.game_board[2][from_col].get_type() != defines.nada ) ):
                    return False
            return True

        if self.game_board[from_row][from_col].get_type() == defines.queen :
            return is_legal_board_queen()
        elif self.game_board[from_row][from_col].get_type() == defines.rook :
            return is_legal_board_rook()
        elif self.game_board[from_row][from_col].get_type() == defines.bishop :
            return is_legal_board_bishop()
        elif self.game_board[from_row][from_col].get_type() == defines.pawn :
            return is_legal_board_pawn()
        else:
            return True

