from core.loader import discover_plugins


def test_discovers_plugins():
    plugins = discover_plugins()
    names = {p.name for p in plugins}
    assert "esp_boxes" in names
    assert "aimbot_fov" in names


def test_plugin_has_version():
    for p in discover_plugins():
        assert isinstance(p.version, str) and p.version
</final>