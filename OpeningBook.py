import shelve
import sqlite3

class OpeningBook:

    def __init__(self):
        # booksql es una tabla de tres campos de texto, posicion, jugadas y valor
        self.booksql=sqlite3.connect('chess.book.sql')
        self.c=self.booksql.cursor()

    def __del__(self):
        self.booksql.close()

    def getMoves(self, fen):
        posicion=" ".join(fen.split()[:-1])
        self.c.execute('''select * from book
                    where posicion=\'%s\'''' % posicion)
        listado = {}
        for i in self.c:
            listado[str(i[1])]=str(i[2])
        return listado

    def addBoard(self, fen):
        pass

    def addMove(self, fen, move, val="",overwrite=False):
        posicion=" ".join(fen.split()[:-1])
        jugadas=self.getMoves(fen)
        if overwrite:
            self.c.execute('''update book set valor=\'%s\'
                    where posicion=\'%s\' and jugadas=\'%s\' ''' % (val,posicion,move))
        else:
            self.c.execute('''insert into book
                    values (\'%s\',\'%s\',\'%s\')''' % (posicion,move,val))
        self.booksql.commit()

