# 
#   piece.py
#   ChessPy
# 
#   Created by Yuval Atir

import defines
# import chessboard as cb

class Piece():
		
	def __init__(self, bwb = defines.piece_color_undefined, pt = defines.nada): 
		self._bw = bwb
		self._ptype = pt

	#virtual ~Piece() {};

	#virtual bool is_legal(int,int,int,int) const = 0;
	#virtual bool is_legal_pawn_kill(Chessboard*,int,int,int,int) const {return true;};

	def get_color(self):
		return self._bw

	def get_type(self): 
		return self._ptype

	def set_color(self, piece_color_in):
		self._bw = piece_color_in

	def set_type(self,piece_type_in): 
		self._ptype = piece_type_in


class King(Piece):

	def __init__(self,piece_color_in, piece_type_in = defines.king):
		
		self.set_color(piece_color_in)
		self.set_type(piece_type_in)

	def is_legal(self,from_row, from_col, to_row, to_col): # const

		if ( ( to_row >= 0 and to_col >= 0 ) and ( to_row <= 7 and to_col <= 7 ) ):    		# within bounds	
			if ( ( ( abs( from_row-to_row ) == 1 and abs( to_col - from_col ) == 1) or		# one step diagonal
			( abs( from_row - to_row ) == 1 and ( to_col == from_col ) ) or				# one step vertical
			( ( from_row == to_row ) and abs( to_col - from_col ) == 1 ) ) and			# one step horizontal
			not ( ( from_col == to_col ) and ( to_row == from_row ) ) ):						# not the same location
				if ( ( abs( from_row-to_row ) == 1 and abs( to_col - from_col ) == 1) or
					( abs( from_row - to_row ) == 1 and ( to_col == from_col ) ) ):
					return True
				else: 
					return False
			
				return False


class Pawn(Piece):
	
	def __init__(self,piece_color_in, piece_type_in = defines.pawn):
		
		self.set_color(piece_color_in)
		self.set_type(piece_type_in)
	

	def is_legal(self, from_row, from_col,  to_row,  to_col ):   # const

		if ( ( to_row >= 0 and to_col >= 0) and ( to_row <= 7 and to_col <= 7) ):
		
			if from_row in (1,6):
				if ( ( (abs( from_row - to_row ) == 2 ) or ( abs( from_row - to_row ) == 1 ) )
				and ( to_col == from_col ) ):
					if ( ( ( self.get_color() == defines.black_piece) and (to_row-from_row > 0) ) or
					( ( self.get_color() == defines.white_piece ) and ( to_row-from_row < 0) ) ):
						return True
				return False
			else:
				if ( ( abs( from_row - to_row ) == 1 ) and ( to_col == from_col ) ):
					if ( ( ( self.get_color() == defines.black_piece ) and ( to_row - from_row > 0 ) ) or
					( ( self.get_color() == defines.white_piece ) and ( to_row - from_row < 0) ) ):
						return True;
			return False
		
		return False


	def is_legal_pawn_kill(self, pboard, from_row, from_col, to_row, to_col):   # const

		if ( pboard.get_piece(from_row,from_col).get_color() == defines.black_piece ):
			if ( pboard.get_piece(from_row,from_col).get_type() == defines.pawn ):
				if ( ( to_row-from_row == 1 ) and ( abs( to_col - from_col ) == 1 ) ):
					return True
				
		if ( pboard.get_piece(from_row,from_col).get_color() == defines.white_piece ):
			if ( pboard.get_piece(from_row,from_col).get_type() == defines.pawn ):
				if ( ( from_row-to_row == 1 ) and ( abs( to_col-from_col ) == 1 ) ):
					return True
		return False


class Rook(Piece):

	def __init__(self,piece_color_in, piece_type_in = defines.rook):
		self.set_color(piece_color_in)
		self.set_type(piece_type_in)
		
	def is_legal(self, from_row, from_col,  to_row,  to_col):   # const

		if ( ( to_row >= 0 and to_col >= 0 ) and ( to_row <= 7 and to_col <= 7 ) ):  
			if ( ( ( from_row == to_row ) or ( from_col == to_col ) ) and ( not ( ( from_row == to_row ) and ( from_col == to_col ) ) ) ):
				return True
			else:
				return False
		return False


class Bishop(Piece):

	def __init__(self,piece_color_in, piece_type_in = defines.bishop):
		self.set_color(piece_color_in)
		self.set_type(piece_type_in)
		
	def is_legal(self, from_row,  from_col,  to_row,  to_col): #const
		
		if ( ( to_row >= 0 and to_col >= 0) and ( to_row <= 7 and to_col <= 7) ) :
			if ( ( abs( to_row - from_row ) == abs( to_col - from_col ) ) and ( to_row - from_row != 0 ) ):
				return True
			else: 
				return False
			return False


class Queen(Piece):

	def __init__(self,piece_color_in, piece_type_in = defines.queen):
		self.set_color(piece_color_in)
		self.set_type(piece_type_in)
	
	def is_legal(self, from_row,  from_col,  to_row,  to_col): 	# const

		if ( ( to_row >= 0 and to_col >= 0 ) and ( to_row <= 7 and to_col <= 7 ) ):  
			if ( ( ( (abs( to_row - from_row ) == abs( to_col - from_col ) ) and ( to_row - from_row != 0 ) ) or  	# bishop condition
					( ( from_row == to_row ) or ( from_col == to_col ) ) ) and         								# rook condition
					( not ( ( from_row == to_row ) and ( from_col == to_col ) ) ) ):    									# same place not allowed
				return True
			else:
				return False
		return False

class Knight(Piece):

	def __init__(self, piece_color_in, piece_type_in = defines.knight):
		
		self.set_color(piece_color_in)
		self.set_type(piece_type_in)

	def is_legal(self, from_row, from_col, to_row, to_col):   # const
		
		if ( ( to_row >= 0 and to_col >= 0 ) and ( to_row <= 7 and to_col <= 7 ) ) : 
			if ( ( ( abs( from_row - to_row ) == 1 and abs( to_col - from_col ) == 2 ) or
				( abs( from_row - to_row ) == 2 and abs( to_col - from_col ) == 1 ) ) and
				not ( (from_col==to_col) and (to_row==from_row) ) ):
				return True
			else:
				return False
			return False


class EmptyPiece(Piece):

	def __init__(self, piece_color_in = defines.piece_color_undefined, piece_type_in = defines.nada):
		self.set_color(piece_color_in)
		self.set_type(piece_type_in)
		
	def is_legal(self, from_row, from_col, to_row, to_col):   # const
		return True

#endif /* piece_hpp */
