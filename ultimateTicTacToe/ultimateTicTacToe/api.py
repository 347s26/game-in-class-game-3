from ninja import NinjaAPI
from ultimateTicTacToe.game.models import Game, Square, SubSquare

api = NinjaAPI()



@api.get("/games/{game_id}")
def get_game(request, game_id: str):
    game = Game.objects.get(id=game_id)
    squares = []
    for square in game.squares.all():
        sub_squares = [
            {
                "position": ss.position,
                "claimed_by": ss.claimed_by
            }
            for ss in square.sub_squares.all()
        ]
        squares.append({
            "position": square.position,
            "claimed_by": square.claimed_by,
            "sub_squares": sub_squares
        })
    
    return {
        "id": str(game.id),
        "state": game.state,
        "current_player": game.current_player,
        "squares": squares
    }

@api.post("/games")
def create_game(request):
    game = Game.objects.create()
    for i in range(9):
        square = Square.objects.create(game=game, position=i)
        for j in range(9):
            SubSquare.objects.create(square=square, position=j)
    return {"id": str(game.id)}