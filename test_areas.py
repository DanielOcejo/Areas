from areas import area_cuadrado

def test_areas():
    assert area_cuadrado(7) == 49
    assert area_cuadrado(0) == 0
    assert area_cuadrado(-7) == 49
    assert area_cuadrado(1.5) == 2.25

