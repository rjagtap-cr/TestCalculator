import json
import os
import pytest
from unittest import mock
from other_functionality import save_dict, get_topper, is_eligible_for_degree, guess_number, get_ip


def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, "test_save_dict.json")
    _dict = {'a': 1, 'b': 2}
    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    assert capsys.readouterr().out == "Dict saved in file\n"


def test_get_age(dummy_student):
    assert dummy_student.get_age() == 30


def test_get_credits(dummy_student):
    assert dummy_student.get_credits() == 0


def test_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5


def test_get_age_s2(dummy_student2):
    assert dummy_student2.get_age() == 30


@pytest.mark.skip(reason="The output does not relate to the input")
def test_get_credits_s2(dummy_student2):
    assert dummy_student2.get_credits() == 20


def test_get_topper(dummy_student_factory):
    students = [
        dummy_student_factory("Rohit", 34, "E&TC", 30),
        dummy_student_factory("Shikhar", 31, "Civil", 40),
        dummy_student_factory("Rahul", 33, "Electronics", 35),
        dummy_student_factory("Rishab", 28, "IT", 25)
    ]
    topper = get_topper(students)
    assert topper == students[1]


@pytest.mark.parametrize("_credits, expected", [(28, False), (32, True)])
def test_is_student_eligible_for_degree(dummy_student_factory, _credits, expected):
    assert is_eligible_for_degree(
        dummy_student_factory(name="Ram", age=25, branch="CSE", _credits=_credits)) is expected


@mock.patch("other_functionality.roll_dice")
def test_guess_number_pass(mock_roll_dice):
    mock_roll_dice.return_value = 3
    assert guess_number(3) == "You WON"
    mock_roll_dice.assert_called_once()


@mock.patch("other_functionality.roll_dice")
def test_guess_number_fail(mock_roll_dice):
    mock_roll_dice.return_value = 4
    assert guess_number(3) == "You LOST"
    mock_roll_dice.assert_called_once()


@pytest.mark.parametrize("_input, expected", [(3, "You WON"), (1, "You LOST"), (2, "You LOST"), (4, "You LOST"),
                                              (5, "You LOST"), (6, "You LOST")])
@mock.patch("other_functionality.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()


@pytest.mark.xfail(reason="This was going to fail")
def test_guess_number_original():
    assert guess_number(3) == "You WON"


@mock.patch("other_functionality.requests.get")
def test_get_ip(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="Mock response", **{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}})
    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_with("https://httpbin.org/ip")
