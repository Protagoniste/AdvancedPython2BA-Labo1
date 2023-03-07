import pytest
import utils


def test_fact():
        assert utils.math.factorial(5) == 120
        assert utils.math.factorial(0) == 1
        with pytest.raises(ValueError):
            utils.fact(-1)

'''    assert utils.fact(0) == 1
    assert utils.fact(4) == 24
     '''

def test_roots():
    pass
    

def test_integrate():
    # À compléter...
    pass

