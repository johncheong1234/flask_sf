from flask import Flask
from stockfish import Stockfish

app = Flask(__name__)

@app.route("/")
def hello_world():
    stockfish = Stockfish("/usr/local/bin/stockfish")
    stockfish.set_position(["e2e4", "e7e6"])
    return stockfish.get_best_move()

if __name__ == '__main__':
    app.run(host='0.0.0.0')