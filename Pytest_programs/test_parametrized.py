import pytest
import math

@pytest.mark.parametrize('user_id',[56,96,45,78,34])
def test_p1(user_id):
    assert user_id > 50

@pytest.mark.parametrize('ip,op',[(2,4),(3,27),(4,256)])
def test_p2(ip,op):
    assert (ip**ip)==op

data = [
    ([2,3,4],'sum',9),
    ([2,3,4],'prod',24)
]

@pytest.mark.parametrize('a,b,c',data)
def test_p3(a,b,c):
    if b=='sum':
        assert sum(a)==c
    if b=='prod':
        assert math.prod(a)==c