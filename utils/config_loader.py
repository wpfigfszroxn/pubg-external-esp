"""YAML config loader with local override support."""
from __future__ import annotations

from pathlib import Path

import yaml

_ROOT = Path(__file__).resolve().parent.parent


def load_config(name: str = "default") -> dict:
    base = _ROOT / "config" / f"{name}.yaml"
    local = _ROOT / "config" / "local.yaml"
    cfg = yaml.safe_load(base.read_text()) if base.exists() else {}
    if local.exists():
        cfg.update(yaml.safe_load(local.read_text()) or {})
    return cfg