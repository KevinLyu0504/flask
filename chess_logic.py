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

def get_analysis(fen):
    engine = chess.engine.SimpleEngine.popen_uci('stockfish/stockfish.exe')
    board = chess.Board(fen)
    info = engine.analyse(board, chess.engine.Limit(time=2.0))

    score = None
    mate = None

    # Score could be either in "mate" or "cp" (centipawns)
    if info['score'].relative.is_mate():
        mate = info['score'].relative.mate()
    else:
        score = info['score'].relative.score()

    # Convert each move in principal variation to UCI string
    pv = [move.uci() for move in info['pv']]

    pv_string = ''
    for i in range(len(pv)):
        if i % 2 == 0:
            pv_string += f'Black: {pv[i]}       '
        else:
            pv_string += f'White: {pv[i]}<br>'  # 新的一行开始于白方的走子

    engine.quit()

    # Return a dictionary containing the score, mate in move, depth, and principal variation.
    return {
        'score': score,
        'mate': mate,
        'depth': info['depth'],
        'pv': pv_string,
    }