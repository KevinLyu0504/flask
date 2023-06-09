from flask import Flask, request, jsonify, render_template
from chess import Board
from chess_logic import get_best_move, get_analysis

app = Flask(__name__)
board = Board()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/AIAI')
def AIAI():
    return render_template('AIAI.html')


@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    fen = data['fen']
    user_move = data['move']

    best_move, new_fen = get_best_move(fen)

    # 获取棋盘分析
    analysis = get_analysis(new_fen)

    # 将最佳移动、新棋局fen和棋盘分析返回给前端
    return jsonify({'move': best_move, 'fen': new_fen, 'analysis': analysis})

@app.route('/ai_move', methods=['POST'])
def ai_move():
    data = request.get_json()
    fen = data['fen']

    best_move, new_fen = get_best_move(fen)

    # 获取棋盘分析
    analysis = get_analysis(new_fen)

    # 将最佳移动、新棋局fen和棋盘分析返回给前端
    return jsonify({'move': best_move, 'fen': new_fen, 'analysis': analysis})


if __name__ == '__main__':
    app.run(debug=True)


