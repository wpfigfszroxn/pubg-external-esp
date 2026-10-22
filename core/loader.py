"""Discovers and instantiates plugins from the plugins package."""
from __future__ import annotations

import importlib
import pkgutil
from typing import List

from core.contracts import PluginBase


def discover_plugins() -> List[PluginBase]:
    import plugins as plugins_pkg

    instances: List[PluginBase] = []
    for mod_info in pkgutil.iter_modules(plugins_pkg.__path__):
        if mod_info.name.startswith("_") or mod_info.name == "registry":
            continue
        module = importlib.import_module(f"plugins.{mod_info.name}")
        factory = getattr(module, "create_plugin", None)
        if factory is None:
            continue
        plugin = factory()
        if isinstance(plugin, PluginBase) or hasattr(plugin, "on_frame"):
            instances.append(plugin)
    return instances