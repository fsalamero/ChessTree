#! /usr/bin/env python

from ChessBoard import ChessBoard

import pilasengine

import virtkeyboard
import OpeningBook

TCASILLA = 80

pilas = pilasengine.iniciar(titulo='ChessBoard Client',
                            ancho=1024, alto=TCASILLA * 8)

tCasilla = 80

class Pieza(pilasengine.actores.Actor):

    def iniciar(self, tipo="p", color=0, fila=0, columna=0):



def mainLoop(self):

    pieces = {}
    chess = ChessBoard()
    board = chess.getBoard()
    turn = chess.getTurn()

    libro_activo = True
    libro_overwrite = False
    board_white = True

    book=OpeningBook.OpeningBook()

    letra=pygame.font.Font(None, 40)

    # load all images
    pieces = [{}, {}]
    pieces[0]["r"] = pilas.actores.Actor("./img/br.png")
    pieces[0]["n"] = pilas.actores.Actor("./img/bn.png")
    pieces[0]["b"] = pilas.actores.Actor("./img/bb.png")
    pieces[0]["k"] = pilas.actores.Actor("./img/bk.png")
    pieces[0]["q"] = pilas.actores.Actor("./img/bq.png")
    pieces[0]["p"] = pilas.actores.Actor("./img/bp.png")
    pieces[0]["R"] = pilas.actores.Actor("./img/wr.png")
    pieces[0]["N"] = pilas.actores.Actor("./img/wn.png")
    pieces[0]["B"] = pilas.actores.Actor("./img/wb.png")
    pieces[0]["K"] = pilas.actores.Actor("./img/wk.png")
    pieces[0]["Q"] = pilas.actores.Actor("./img/wq.png")
    pieces[0]["P"] = pilas.actores.Actor("./img/wp.png")
    pieces[0]["."] = pilas.actores.Actor("./img/w.png")
    pieces[1]["r"] = pilas.actores.Actor("./img/br.png")
    pieces[1]["n"] = pilas.actores.Actor("./img/bn.png")
    pieces[1]["b"] = pilas.actores.Actor("./img/bb.png")
    pieces[1]["k"] = pilas.actores.Actor("./img/bk.png")
    pieces[1]["q"] = pilas.actores.Actor("./img/bq.png")
    pieces[1]["p"] = pilas.actores.Actor("./img/bp.png")
    pieces[1]["R"] = pilas.actores.Actor("./img/wr.png")
    pieces[1]["N"] = pilas.actores.Actor("./img/wn.png")
    pieces[1]["B"] = pilas.actores.Actor("./img/wb.png")
    pieces[1]["K"] = pilas.actores.Actor("./img/wk.png")
    pieces[1]["Q"] = pilas.actores.Actor("./img/wq.png")
    pieces[1]["P"] = pilas.actores.Actor("./img/wp.png")
    pieces[1]["."] = pilas.actores.Actor("./img/b.png")

    clock = pygame.time.Clock()

    posRect = pygame.Rect(0,0,self.tCasilla,self.tCasilla)
    rectangulo = pygame.Rect(self.tCasilla*8+5,0,315,self.tCasilla*8)
    informacion = pygame.Rect(self.tCasilla*8+5,380,315,100)

    mousePos = [-1, -1]
    markPos = [-1, -1]
    validMoves = []

    gameResults = ["", "WHITE WINS!", "BLACK WINS!", "STALEMATE",
                        "DRAW BY THE FIFTHY MOVES RULE",
                        "DRAW BY THE THREE REPETITION RULE"]

    letra_libro_activo = letra.render("Libro Activo", 1, (255, 255, 255))
    letra_libro_overwrite = letra.render("(Sobreescribir)", 1, (255, 255, 255))

    while 1:
        clock.tick(10)

        # Obtener la pos actual
        tablero = chess.getFEN()

        # Escribir el n de jugada
        num_jugada = str(chess.getCurrentMove() / 2 + 1)
        if turn:
            num_jugada = num_jugada + ". ..., "
        else:
            num_jugada = num_jugada + ". "
        letra_num_jugada = letra.render(num_jugada, 1, (255, 255, 255))
        screen.blit(letra_num_jugada, (self.tCasilla*8+20, 30))

        # Obtener las jugadas almacenadas
        jugadas_teoricas = book.getMoves(tablero)

        # Si hay jugadas almacenadas, escrcribirlas
        if jugadas_teoricas is not None:
            num_jugadas = len(jugadas_teoricas)
            contador = 0
            for jugada in jugadas_teoricas:
                posx = self.tCasilla * 8 + 20 + 150 * (contador % 2)
                posy = 100 + 40 * (contador // 2)
                texto_jugada = letra.render(jugada +
                        jugadas_teoricas[jugada], 1, (255, 255, 255))
                screen.blit(texto_jugada, (posx, posy))
                contador += 1

        # Si libro activo o activada sobreescritura, escribirlo
        if libro_activo:
            screen.blit(letra_libro_activo, (self.tCasilla*8+20, 400))
            if libro_overwrite:
                screen.blit(letra_libro_overwrite, (self.tCasilla*8+20, 450))
        else:
            pygame.draw.rect(screen, (0, 0, 0), informacion)

        # Bucle de eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # La tecla ESC sale del programa
                    return
                elif event.key == K_LEFT or event.key == K_o:
                    # La tecla LEFT retrocede una jugada
                    chess.undo()
                    pygame.draw.rect(screen, (0, 0, 0), rectangulo)
                elif event.key == K_RIGHT or event.key == K_p:
                    # La tecla RIGHT avanza una jugada
                    chess.redo()
                    pygame.draw.rect(screen, (0, 0, 0), rectangulo)
                elif event.key == K_UP or event.key == K_a:
                    # La tecla UP conmuta entre libro activado y desactivado
                    libro_activo = not libro_activo
                elif event.key == K_DOWN or event.key == K_s:
                    # La tecla DOWN conmuta el estado de sobreescritura
                    libro_overwrite = not libro_overwrite
                elif event.unicode in ("f","F"):
                    # La tecla F inprime la pos actual
                    print chess.getFEN()
                elif event.unicode in ("t","T"):
                    # ?
                    #mykeys = virtkeyboard.VirtualKeyboard()
                    #print mykeys.run(screen, "Nfxh4+")
                    # Invierte el tablero
                    board_white = not board_white
                elif event.unicode in ("a","A"):
                    # La tecla A imprime la lista de jugadas (AN)
                    an = chess.getAllTextMoves(chess.AN)
                    if an:
                        print "AN: " + ", ".join(an)
                elif event.unicode in ("s","S"):
                    # La tecla S imprime la lista de jugadas (SAN)
                    san = chess.getAllTextMoves(chess.SAN)
                    if san:
                        print "SAN: " + ", ".join(san)
                elif event.unicode in ("l","L"):
                    # La tecla L imprime la lista de jugadas (LAN)
                    lan = chess.getAllTextMoves(chess.LAN)
                    if lan:
                        print "LAN: " + ", ".join(lan)

                board = chess.getBoard()
                turn = chess.getTurn()
                markPos[0] = -1
                validMoves = []

            if not chess.isGameOver():
                if event.type == MOUSEMOTION:
                    mx = event.pos[0]
                    my = event.pos[1]
                    mousePos[0] = mx/self.tCasilla
                    mousePos[1] = my/self.tCasilla
                    if not board_white:
                        mousePos[0] = 7 - mousePos[0]
                        mousePos[1] = 7 - mousePos[1]
                elif event.type == MOUSEBUTTONDOWN:
                    if mousePos[0] >= 0 and mousePos[0] <= 7:
                        if markPos[0] == mousePos[0] and markPos[1] == mousePos[1]:
                            markPos[0] = -1
                            validMoves = []
                        else:
                            if (turn==ChessBoard.WHITE and board[mousePos[1]][mousePos[0]].isupper()) or \
                               (turn==ChessBoard.BLACK and board[mousePos[1]][mousePos[0]].islower()):
                                markPos[0] = mousePos[0]
                                markPos[1] = mousePos[1]
                                validMoves = chess.getValidMoves(tuple(markPos))

                            else:
                                if markPos[0] != -1:
                                    res = chess.addMove(markPos,mousePos)
                                    if not res and chess.getReason() == chess.MUST_SET_PROMOTION:
                                        chess.setPromotion(chess.QUEEN)
                                        res = chess.addMove(markPos,mousePos)
                                    if res:
                                        jugada = chess.getLastTextMove(chess.SAN)
                                        # Almacenar la jugada si es nueva o si activado el modo OVERWRITE
                                        if libro_activo:
                                            if libro_overwrite or jugadas_teoricas == None or not jugadas_teoricas.has_key(jugada):
                                                teclado = virtkeyboard.VirtualKeyboard()
                                                valoracion = teclado.run(screen, jugada)
                                                book.addMove(tablero, jugada, valoracion,libro_overwrite)
                                        board = chess.getBoard()
                                        turn = chess.getTurn()
                                        markPos[0] = -1
                                        validMoves = []
                                        pygame.draw.rect(screen, (0, 0, 0), rectangulo)

        if chess.isGameOver():
            pygame.display.set_caption("Game Over! (Reason:%s)" % gameResults[chess.getGameResult()])
            validMove = []
            markPos[0] = -1
            markPos[1] = -1
        else:
            pygame.display.set_caption('ChessBoard Client')

        y = 0
        for rank in board:
            x = 0
            for p in rank:
                screen.blit(pieces[(x+y)%2]["."],(x*self.tCasilla,y*self.tCasilla))
                if board_white:
                    screen.blit(pieces[(x+y)%2][p],(x*self.tCasilla,y*self.tCasilla))
                else:
                    screen.blit(pieces[(x+y)%2][p],((7-x)*self.tCasilla,(7-y)*self.tCasilla))
                x+=1
            y+=1

        if markPos[0] != -1:
            if board_white:
                mP0 = markPos[0]
                mP1 = markPos[1]
            else:
                mP0 = 7 - markPos[0]
                mP1 = 7 - markPos[1]
            posRect.left = mP0*self.tCasilla
            posRect.top = mP1*self.tCasilla
            pygame.draw.rect(screen, (255,255,0),posRect, 4)

        for v in validMoves:
            if board_white:
                v0 = v[0]
                v1 = v[1]
            else:
                v0 = 7 - v[0]
                v1 = 7 - v[1]
            posRect.left = v0*self.tCasilla
            posRect.top = v1*self.tCasilla
            pygame.draw.rect(screen, (255,255,0),posRect, 4)

        pygame.display.flip()

pilas.ejecutar()

