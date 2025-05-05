import pytest
pytestmark=[pytest.mark.mt]

@pytest.mark.addt
def test_s1():
    num = 9/4
    s1='i am learning python '
    assert str(num)=='2.25'
    assert s1+str(num) =='i am learning python 2.25'

@pytest.mark.mytest
@pytest.mark.addt
def test_s2():
    letters='abcdefgh'
    assert len(letters)==8

@pytest.mark.addt
def test_s3():
    letters='abcd'
    assert letters[-1]=='d'

@pytest.mark.mytest
def test_s4():
    abc = "abcdefghijklmnopqrstuvwxyz"
    assert abc[4:]=="efghijklmnopqrstuvwxyz"
