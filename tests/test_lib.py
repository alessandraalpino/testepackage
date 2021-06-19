from testepackage.lib import try_me


def test_lib():
    assert try_me(1, 2) == 3
