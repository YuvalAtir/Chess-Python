#!/usr/bin/python3
# ChessPy by Yuval Atir

from chessboardTk import Chessboard # chessboard is the class imported from module(file) chessboardTk
from tkinter import Tk



#__version__ = '0.3.4'


def main():

    root = Tk()    
    gui = Chessboard(root)    
    root.mainloop()

        
if __name__ == "__main__": main()
