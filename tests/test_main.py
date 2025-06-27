from src.main import add
def test_add_function():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(1, 0) == 1
    assert add(1, 1) == 2
    assert add(1, 2) == 3
    assert add(1, 3) == 4
    assert add(1, 4) == 5
    assert add(1, 5) == 6