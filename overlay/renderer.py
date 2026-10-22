"""Pyglet-backed transparent overlay renderer."""
from __future__ import annotations

from typing import List, Tuple

import pyglet


class OverlayRenderer:
    def __init__(self, cfg: dict):
        self._width = cfg.get("width", 1920)
        self._height = cfg.get("height", 1080)
        self._fps = cfg.get("fps_cap", 144)
        self._queue: List[Tuple[int, int, int, int, tuple]] = []
        self._window = pyglet.window.Window(
            width=self._width,
            height=self._height,
            caption="pubg-external-esp",
            style=pyglet.window.Window.WINDOW_STYLE_OVERLAY,
        )
        self._batch = pyglet.graphics.Batch()

    def queue_box(self, x: int, y: int, w: int, h: int, color: tuple) -> None:
        self._queue.append((x, y, w, h, color))

    def flush(self) -> None:
        self._batch = pyglet.graphics.Batch()
        for x, y, w, h, color in self._queue:
            pyglet.shapes.Box(x, y, w, h, color=color, batch=self._batch)
        self._queue.clear()

    def draw(self) -> None:
        self._window.clear()
        self._batch.draw()