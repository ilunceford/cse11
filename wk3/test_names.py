from wk3.names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Joseph", "Anderson") == "Andereson;Joseph"
    assert make_full_name("Joseph", "Smith") == "Smith;Joseph"
    

def test_extract_family_name(full_name):
    assert extract_family_name("Anderson; Joseph") == "Anderson"
    assert extract_family_name("Smith; Joseph") == "Smith"

def test_extract_given_name():
    assert extract_given_name("Anderson; Joseph") == "Joseph"
    assert extract_given_name("Smith; Joseph") == "Smith"



    

pytest.main(["-v ", "--tb=line", "-rN", __file__])