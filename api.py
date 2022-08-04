import requests

API_URL = "http://go-chess-api.herokuapp.com"
IS_LEGAL_URL = API_URL + "/isLegal?"
BEST_MOVE_URL = API_URL + "/findBestMove?"


# sends a request to the engine to determine if the given move is legal
# move should be a string in the format e2e4, b7b8q, g1f3, etc.
def is_legal(move):
    args = {"FEN": f"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1 moves {move}"}
    r = requests.get(url=IS_LEGAL_URL, params=args)
    print(r.json())
    return True
