import pytest

def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)

def test_a1():
    with pytest.raises(Exception) as excinfo:
        assert 2>=9
    print(str(excinfo))