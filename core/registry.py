"""Static plugin registry used when auto-discovery is disabled."""
from __future__ import annotations

from typing import Dict, Type

from core.contracts import PluginBase

_REGISTRY: Dict[str, Type] = {}


def register(name: str):
    def _wrap(cls: Type) -> Type:
        _REGISTRY[name] = cls
        return cls
    return _wrap


def get_registered() -> Dict[str, Type]:
    return dict(_REGISTRY)