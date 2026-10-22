"""Thin wrapper around pymem for external process reads."""
from __future__ import annotations

import logging
from typing import Optional

import pymem

log = logging.getLogger("memory")


class MemoryReader:
    def __init__(self, process_name: str):
        self._name = process_name
        self._pm: Optional[pymem.Pymem] = None

    def attach(self) -> bool:
        try:
            self._pm = pymem.Pymem(self._name)
            log.info("attached to %s (pid=%s)", self._name, self._pm.process_id)
            return True
        except pymem.exception.ProcessNotFound:
            log.warning("process %s not found", self._name)
            return False

    def read_int(self, address: int) -> int:
        if self._pm is None:
            raise RuntimeError("not attached")
        return self._pm.read_int(address)

    def read_float(self, address: int) -> float:
        if self._pm is None:
            raise RuntimeError("not attached")
        return self._pm.read_float(address)

    def read_vec3(self, address: int) -> tuple[float, float, float]:
        if self._pm is None:
            raise RuntimeError("not attached")
        return (
            self._pm.read_float(address),
            self._pm.read_float(address + 4),
            self._pm.read_float(address + 8),
        )

    @property
    def base_address(self) -> int:
        if self._pm is None:
            return 0
        return self._pm.base_address