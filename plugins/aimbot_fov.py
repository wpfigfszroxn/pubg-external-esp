"""FOV-limited aim assist plugin (educational stub, no input injection)."""
from __future__ import annotations

import math

from core.contracts import Frame, HostContext, Vec3


class AimbotFovPlugin:
    name = "aimbot_fov"
    version = "0.6.0"

    def __init__(self) -> None:
        self._ctx: HostContext | None = None
        self._fov = 8.0
        self._smoothing = 0.35

    def on_load(self, ctx: HostContext) -> None:
        self._ctx = ctx
        cfg = ctx.config().get("features", {}).get("aimbot", {})
        self._fov = float(cfg.get("fov_degrees", 8))
        self._smoothing = float(cfg.get("smoothing", 0.35))

    def _angle_between(self, a: Vec3, b: Vec3) -> float:
        dot = a.x * b.x + a.y * b.y + a.z * b.z
        na = math.sqrt(a.x ** 2 + a.y ** 2 + a.z ** 2) or 1e-6
        nb = math.sqrt(b.x ** 2 + b.y ** 2 + b.z ** 2) or 1e-6
        return math.degrees(math.acos(max(-1.0, min(1.0, dot / (na * nb)))))

    def on_frame(self, frame: Frame) -> None:
        if self._ctx is None or frame.local_player is None:
            return
        origin = frame.local_player.position
        best, best_angle = None, self._fov
        for ent in frame.entities:
            if ent.team_id == frame.local_player.team_id or ent.health <= 0:
                continue
            angle = self._angle_between(origin, ent.position)
            if angle < best_angle:
                best, best_angle = ent, angle
        if best is not None:
            self._ctx.log(f"target locked {best.address:#x} angle={best_angle:.2f}")

    def on_unload(self) -> None:
        self._ctx = None


def create_plugin() -> AimbotFovPlugin:
    return AimbotFovPlugin()