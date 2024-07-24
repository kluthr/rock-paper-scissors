import json

from app.redis_client import redis_client


class RPSGame:
    """Handles playing of one RPS game and saving/updating results in Redis"""

    def __init__(self, data: dict):
        self.data = data
        self.redis_key = f"{self.data['name_1']}:{self.data['name_2']}"

    def play(self) -> dict:
        winner = self._determine_winner()
        results = self._update_history(winner)
        return results

    def _determine_winner(self) -> str:
        move_1 = self.data["move_1"]
        move_2 = self.data["move_2"]

        if move_1 == move_2:
            return None
        elif (
            (move_1 == "Rock" and move_2 == "Scissors")
            or (move_1 == "Paper" and move_2 == "Rock")
            or (move_1 == "Scissors" and move_2 == "Paper")
        ):
            return "player_1"
        elif (
            (move_1 == "Rock" and move_2 == "Paper")
            or (move_1 == "Paper" and move_2 == "Scissors")
            or (move_1 == "Scissors" and move_2 == "Rock")
        ):
            return "player_2"

    def _update_history(self, winner):
        history = redis_client.get(self.redis_key)
        data = {}
        if history:
            data = json.loads(history.decode("utf-8"))
        else:
            data = {
                "player_1": {
                    "name": self.data["name_1"],
                    "wins": 0,
                },
                "player_2": {
                    "name": self.data["name_2"],
                    "wins": 0,
                },
                "ties": 0,
            }
        winner_name = None
        if winner:
            data[winner]["wins"] += 1
            winner_name = data[winner]["name"]
        else:
            data["ties"] += 1
        redis_client.set(self.redis_key, json.dumps(data))
        return {"winner": winner_name, "history": data}
