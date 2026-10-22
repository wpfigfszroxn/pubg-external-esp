"""Entry point for the pubg-external-esp host."""
from __future__ import annotations

import logging

from core.host import Host
from core.loader import discover_plugins
from utils.config_loader import load_config
from utils.logger import setup_logging


def main() -> None:
    cfg = load_config()
    setup_logging(cfg.get("logging", {}).get("level", "INFO"),
                  cfg.get("logging", {}).get("file"))
    logging.getLogger("main").info("starting pubg-external-esp host")
    plugins = discover_plugins()
    logging.getLogger("main").info("discovered %d plugin(s)", len(plugins))
    Host(cfg, plugins).run()


if __name__ == "__main__":
    main()