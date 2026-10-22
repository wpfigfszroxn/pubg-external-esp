"""Skeleton ESP plugin — draws bone lines for visible enemies."""
from __future__ import annotations

from core.contracts import Frame, HostContext

BONE_PAIRS = [
    ("head", "neck"),
    ("neck", "pelvis"),
    ("pelvis", "l_knee"),
    ("pelvis", "r_knee"),
]


class SkeletonEspPlugin:
    name = "skeleton_esp"
    version = "0.9.1"

    def __init__(self) -> None:
        self._ctx: HostContext | None = None
        self._enabled = False

    def on_load(self, ctx: HostContext) -> None:
        self._ctx = ctx
        cfg = ctx.config().get("features", {}).get("esp", {})
        self._enabled = bool(cfg.get("skeleton", False))

    def on_frame(self, frame: Frame) -> None:
        if not self._enabled or self._ctx is None:
            return
        for ent in frame.entities:
            bones = ent.meta.get("bones")
            if not bones:
                continue
            for a, b in BONE_PAIRS:
                if a in bones and b in bones:
                    self._ctx.log(f"skeleton {ent.address:#x} {a}->{b}")

    def on_unload(self) -> None:
        self._ctx = None


def create_plugin() -> SkeletonEspPlugin:
    return SkeletonEspPlugin()