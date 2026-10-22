"""Input simulation helpers for aim assist smoothing (educational)."""
from __future__ import annotations

import ctypes
import time

_user32 = ctypes.windll.user32


def move_mouse_relative(dx: int, dy: int) -> None:
    _user32.mouse_event(0x0001, dx, dy, 0, 0)


def smooth_move(dx: float, dy: float, smoothing: float, steps: int = 4) -> None:
    sx = dx * (1.0 - smoothing)
    sy = dy * (1.0 - smoothing)
    for _ in range(steps):
        move_mouse_relative(int(sx / steps), int(sy / steps))
        time.sleep(0.002)