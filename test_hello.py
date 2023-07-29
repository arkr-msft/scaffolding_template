from hello import more_hello, more_good_bye


def test_more_hello():
    assert "hi" == more_hello()


def test_more_good_bye():
    assert "bye" == more_good_bye()
