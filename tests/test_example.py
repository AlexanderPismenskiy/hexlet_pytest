from example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''

#   poetry run pytest
#   poetry run pytest tests/test_example.py