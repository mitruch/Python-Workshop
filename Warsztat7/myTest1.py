from zad01_flatten import flatten


def test_empty_list():
    
    result =  flatten([])

    assert result == []