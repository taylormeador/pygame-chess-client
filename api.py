import requests
import globals

API_URL = "http://go-chess-api.herokuapp.com"
IS_LEGAL_URL = API_URL + "/isLegal?"
BEST_MOVE_URL = API_URL + "/bestMove?"


# sends a request to the engine to determine if the given move is legal
# move should be a string in the format e2e4, b7b8q, g1f3, etc.
def is_legal(FEN):
    args = {"FEN": FEN}
    r = requests.get(url=IS_LEGAL_URL, params=args)
    response = r.json()['FEN']
    print(f"API isLegal response: {response}")
    return response

# sends a request to the engine to determine the best move in the position
def best_move(FEN):
    args = {"FEN": FEN}
    r = requests.get(url=BEST_MOVE_URL, params=args)
    new_fen = r.json()['FEN']
    checkmate = r.json()['Checkmate']
    stalemate = r.json()['Stalemate']
    print(f"API bestMove response: {new_fen}, Checkmate: {checkmate}, Stalemate: {stalemate}")
    return r.json()
