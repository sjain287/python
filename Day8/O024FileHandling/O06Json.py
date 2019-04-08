import json

from pathlib import Path

players = [
    {"id": 101, "title": "sachin", "runs": 1500},
    {"id": 102, "title": "Rahul", "runs": 1000},
    {"id": 103, "title": "saurav", "runs": 2500}
]

data = json.dumps(players)
print(data)

Path("players.json").write_text(data)


data = Path("players.json").read_text()

players = json.loads(data)
print(players)
