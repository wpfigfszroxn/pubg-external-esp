"""Offset table loaded from a JSON dump."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

_OFFSET_PATH = Path(__file__).resolve().parent.parent / "offsets" / "current.json"


@dataclass
class Offsets:
    actor_list: int = 0x0
    actor_count: int = 0x0
    local_player: int = 0x0
    position: int = 0x0
    health: int = 0x0
    team_id: int = 0x0

    @classmethod
    def load(cls, path: Path = _OFFSET_PATH) -> "Offsets":
        if not path.exists():
            return cls()
        data = json.loads(path.read_text())
        return cls(
            actor_list=int(data.get("actor_list", 0), 0),
            actor_count=int(data.get("actor_count", 0), 0),
            local_player=int(data.get("local_player", 0), 0),
            position=int(data.get("position", 0), 0),
            health=int(data.get("health", 0), 0),
            team_id=int(data.get("team_id", 0), 0),
        )