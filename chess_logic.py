import chess.engine

def get_best_move(fen):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish.exe")

    board = chess.Board(fen)

    if not board.is_checkmate() and not board.is_stalemate():
        print("Kelvin is thinking...")
        result = engine.play(board, chess.engine.Limit(time=2.0))
        best_move = result.move
        print(f"The best move calculated by the engine is: {best_move}")
    else:
        best_move = None

    engine.quit()

    if best_move:
        return chess.square_name(best_move.from_square) + chess.square_name(best_move.to_square), board.fen()
    else:
        return None, board.fen()