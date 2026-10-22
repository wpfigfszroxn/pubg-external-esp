# Contributing to pubg-external-esp

This repository is an **educational research project** demonstrating how
external process memory reading, overlay rendering and plugin-based
architecture work on Windows. It is not intended for use in live matches
and any use violates PUBG's Terms of Service.

## Ground rules

1. Everything you submit must be educational: no anti-cheat bypasses,
   no HWID spoofers, no kernel drivers, no obfuscation.
2. Keep the plugin host contract stable (`core/contracts.py`).
3. New features go into `plugins/` as an extension module — do not fork
   the host.
4. Run `pytest` before opening a PR.

## Adding a plugin

1. Drop a module into `plugins/` that subclasses `PluginBase`.
2. Register it in `plugins/registry.py`.
3. Add a smoke test under `tests/`.

## Style

- Python 3.11+, type hints everywhere.
- `ruff` + `black` defaults.
- No external network calls from the host.