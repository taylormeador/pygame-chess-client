import requests

API_URL = "http://go-chess-api.herokuapp.com"
IS_LEGAL_URL = API_URL + "/isLegal?"
BEST_MOVE_URL = API_URL + "/findBestMove?"

# sends a request to the engine to determine if the given move is legal
def is_legal(move):
    args = {"FEN": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1 moves e2e4"}
    r = requests.get(url=IS_LEGAL_URL, params=args)
    data = r.json()
    print(data)
