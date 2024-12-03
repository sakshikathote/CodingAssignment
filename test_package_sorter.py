import pytest
from package_sorter import sort

def test_standard_package():
    assert sort(100, 100, 100, 5) == "STANDARD"

def test_bulky_package():
    assert sort(200, 100, 50, 10) == "SPECIAL"

def test_heavy_package():
    assert sort(100, 100, 100, 25) == "SPECIAL"

def test_rejected_package():
    assert sort(200, 200, 200, 25) == "REJECTED"

def test_edge_case_volume():
    assert sort(100, 100, 1000, 19.9) == "SPECIAL"

def test_edge_case_mass():
    assert sort(10, 10, 10, 20) == "SPECIAL"

if __name__ == "__main__":
    pytest.main()
