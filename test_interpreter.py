from core import run_single_instance


def test_addition():
    code = ['1', '1', '+']
    assert run_single_instance(code) == '2'

def test_subtraction():
    code = ['3', '2', '-']
    assert run_single_instance(code) == '1'
