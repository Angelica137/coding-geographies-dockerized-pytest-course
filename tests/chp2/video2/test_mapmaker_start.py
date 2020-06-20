from scripts.chp2.video2.mapmaker_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_pount_generation():
    with pytest.raises(Exception) as exp:
        Point("Buenos Aires", 12.11386, -555.08269)
