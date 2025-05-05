import sys
import pytest

@pytest.mark.xfail
def test_x1():
    ltrs = 'abcd'
    num=123
    assert ltrs+num == 'abcd123'

@pytest.mark.xfail(sys.platform=='win32',reason='runs only on windows')
def test_x2():
    s1='good morning'
    s2=' hyderabad'
    l1 = ['good', 'morning', 'hyderabad']
    assert ''.join(l1)==s1+s2

@pytest.mark.xfail(reason='out of the box')
def test_x3():
    letters='abcdefghijklm'
    assert letters[15]

def test_x4():
    num = 4
    assert num+5 ==9