"""Mutable host state shared across ticks."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from core.contracts import Entity


@dataclass
class HostState:
    tick: int = 0
    attached: bool = False
    entities: List[Entity] = field(default_factory=list)
    last_positions: Dict[int, tuple] = field(default_factory=dict)

    def remember(self, ent: Entity) -> None:
        self.last_positions[ent.address] = (
            ent.position.x,
            ent.position.y,
            ent.position.z,
        )