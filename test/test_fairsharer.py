from src.fairsharer import fair_sharer


def test_fair_sharer_one_iteration():
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert result == [100, 800, 900, 0]


def test_fair_sharer_two_iterations():
    result = fair_sharer([0, 1000, 800, 0], 2)
    assert result == [100, 890, 720, 90]