"""Walks the actor list and produces Frame snapshots."""
from __future__ import annotations

from typing import List

from core.contracts import Entity, Frame, Vec3
from services.memory_reader import MemoryReader
from services.offsets import Offsets


class EntityParser:
    def __init__(self, reader: MemoryReader):
        self._reader = reader
        self._offsets = Offsets.load()

    def _read_entity(self, address: int) -> Entity | None:
        try:
            x, y, z = self._reader.read_vec3(address + self._offsets.position)
            health = self._reader.read_int(address + self._offsets.health)
            team = self._reader.read_int(address + self._offsets.team_id)
        except Exception:
            return None
        return Entity(address=address, position=Vec3(x, y, z), health=health, team_id=team)

    def snapshot(self, tick: int) -> Frame:
        entities: List[Entity] = []
        base = self._reader.base_address
        if base == 0:
            return Frame(entities=[], local_player=None, tick=tick)

        actor_list = self._reader.read_int(base + self._offsets.actor_list)
        count = self._reader.read_int(base + self._offsets.actor_count)
        for i in range(min(count, 128)):
            ptr = self._reader.read_int(actor_list + i * 0x8)
            if ptr:
                ent = self._read_entity(ptr)
                if ent:
                    entities.append(ent)

        local = self._read_entity(base + self._offsets.local_player)
        return Frame(entities=entities, local_player=local, tick=tick)