"""ESP box overlay plugin — draws bounding boxes around entities."""
from __future__ import annotations

from core.contracts import Frame, HostContext


class EspBoxesPlugin:
    name = "esp_boxes"
    version = "1.3.0"

    def __init__(self) -> None:
        self._ctx: HostContext | None = None
        self._max_dist = 400.0

    def on_load(self, ctx: HostContext) -> None:
        self._ctx = ctx
        cfg = ctx.config().get("features", {}).get("esp", {})
        self._max_dist = float(cfg.get("max_distance_m", 400))

    def on_frame(self, frame: Frame) -> None:
        if self._ctx is None or frame.local_player is None:
            return
        origin = frame.local_player.position
        for ent in frame.entities:
            if ent.team_id == frame.local_player.team_id:
                continue
            dist = origin.distance_to(ent.position)
            if dist > self._max_dist:
                continue
            color = (0, 255, 0) if ent.is_visible else (255, 0, 0)
            self._ctx.draw_box(0, 0, 60, 120, color)

    def on_unload(self) -> None:
        self._ctx = None


def create_plugin() -> EspBoxesPlugin:
    return EspBoxesPlugin()