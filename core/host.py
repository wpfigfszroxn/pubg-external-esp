"""Plugin host: loads extensions, ticks them, feeds them frames."""
from __future__ import annotations

import logging
import time
from typing import Iterable

from core.contracts import Frame, HostContext, PluginBase
from services.memory_reader import MemoryReader
from services.entity_parser import EntityParser
from overlay.renderer import OverlayRenderer

log = logging.getLogger("host")


class Host(HostContext):
    def __init__(self, config: dict, plugins: Iterable[PluginBase]):
        self._config = config
        self._plugins = list(plugins)
        self._reader = MemoryReader(config["process"]["name"])
        self._parser = EntityParser(self._reader)
        self._renderer = OverlayRenderer(config["overlay"])
        self._tick = 0

    def config(self) -> dict:
        return self._config

    def log(self, msg: str) -> None:
        log.info(msg)

    def draw_box(self, x: int, y: int, w: int, h: int, color: tuple) -> None:
        self._renderer.queue_box(x, y, w, h, color)

    def _load_plugins(self) -> None:
        for plugin in self._plugins:
            plugin.on_load(self)
            log.info("loaded plugin %s v%s", plugin.name, plugin.version)

    def run(self) -> None:
        self._load_plugins()
        interval = self._config["process"]["poll_interval_ms"] / 1000.0
        try:
            while True:
                frame = self._parser.snapshot(self._tick)
                for plugin in self._plugins:
                    plugin.on_frame(frame)
                self._renderer.flush()
                self._tick += 1
                time.sleep(interval)
        except KeyboardInterrupt:
            self.log("shutdown requested")
        finally:
            for plugin in self._plugins:
                plugin.on_unload()