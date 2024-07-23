from redis_client import redis_client


def play(data) -> dict:
    try:
        winner = _determine_winner(data)
        redis_client.incr(winner)
        count = int(redis_client.get(winner).decode("utf-8"))
        return {"winner": winner, "wins": count}
    except Exception as e:
        return {"winner": "It's a tie!", "wins": None}


def _determine_winner(data: dict) -> str:
    move_1 = data["move_1"]
    move_2 = data["move_2"]

    if move_1 == move_2:
        raise Exception("Tie!")
    elif (
        (move_1 == "Rock" and move_2 == "Scissors")
        or (move_1 == "Paper" and move_2 == "Rock")
        or (move_1 == "Scissors" and move_2 == "Paper")
    ):
        return data["name_1"]
    elif (
        (move_1 == "Rock" and move_2 == "Paper")
        or (move_1 == "Paper" and move_2 == "Scissors")
        or (move_1 == "Scissors" and move_2 == "Rock")
    ):
        return data["name_2"]
