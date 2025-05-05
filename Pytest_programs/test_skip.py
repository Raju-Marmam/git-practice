import pytest

num = 1
def check_t(num=0):
    res=num+5
    return res
print(check_t())

def test_a1():
    assert type(num)==int
@pytest.mark.skip(reason='num equals to 10')
def test_a2():
    assert num==10

@pytest.mark.skipif(check_t(1)==6,reason='default value is 1')
def test_a3():
    assert check_t(num)==0