from core.contracts import Entity, Vec3


def test_distance_zero():
    a = Vec3(0.0, 0.0, 0.0)
    assert a.distance_to(a) == 0.0


def test_distance_3d():
    a = Vec3(0.0, 0.0, 0.0)
    b = Vec3(3.0, 4.0, 0.0)
    assert a.distance_to(b) == 5.0


def test_entity_defaults():
    e = Entity(address=0x1000, position=Vec3(1, 2, 3))
    assert e.health == 100
    assert e.team_id == 0
    assert e.is_visible is False