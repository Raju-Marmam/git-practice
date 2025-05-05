import pytest

@pytest.fixture()
def setup_data():
    print('\n...fixture started ...')
    data = ['hyd','upl','ngl','sec']
    return data

def test_f1(setup_data):
    print(setup_data)
    assert setup_data[0]=='hyd'

def rev(lst):
    lst.reverse()
    return lst

def test_f2(setup_data):
    assert setup_data[::-1]==rev(setup_data)
