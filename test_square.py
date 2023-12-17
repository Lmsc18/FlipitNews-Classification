from square import get_square

def test_get_square1():
    a=5
    resulta=get_square(a)
    assert resulta==25

def test_get_square2():
    b=9
    resulta=get_square(b)
    assert resulta==81