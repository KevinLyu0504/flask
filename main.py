from flask import Flask, request, jsonify, render_template
from chess import Board
from chess_logic import get_best_move

app = Flask(__name__)
board = Board()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    fen = data['fen']
    user_move = data['move']

    best_move, new_fen = get_best_move(fen)

    # 将最佳移动和新棋局fen返回给前端
    return jsonify({'move': best_move, 'fen': new_fen})

if __name__ == '__main__':
    app.run(debug=True)


