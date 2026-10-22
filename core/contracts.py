"""Shared contracts between the host and plugin extensions."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, Sequence


@dataclass(frozen=True)
class Vec3:
    x: float
    y: float
    z: float

    def distance_to(self, other: "Vec3") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5


@dataclass
class Entity:
    """A single actor read from the target process."""
    address: int
    position: Vec3
    health: int = 100
    team_id: int = 0
    is_visible: bool = False
    meta: dict = field(default_factory=dict)


@dataclass
class Frame:
    """Snapshot handed to every plugin on each tick."""
    entities: Sequence[Entity]
    local_player: Entity | None
    tick: int


class PluginBase(Protocol):
    """Every extension module must implement this surface."""

    name: str
    version: str

    def on_load(self, ctx: "HostContext") -> None: ...
    def on_frame(self, frame: Frame) -> None: ...
    def on_unload(self) -> None: ...


class HostContext(Protocol):
    """Read-only view of the host exposed to plugins."""

    def config(self) -> dict: ...
    def log(self, msg: str) -> None: ...
    def draw_box(self, x: int, y: int, w: int, h: int, color: tuple) -> None: ...