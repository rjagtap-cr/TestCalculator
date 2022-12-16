import pytest

from other_functionality import Student, Student2


@pytest.fixture
def dummy_student(scope="module"):
    return Student("Virat", 30, "CSE")


@pytest.fixture(params=[28, 32], ids=["ineligible", "eligible"])
def dummy_student2(request):
    return Student2("Virat", 30, "CSE", request.param)


@pytest.fixture
def dummy_student_factory():
    def make_dummy_student(name, age, branch, _credits):
        return Student2(name, age, branch, _credits)
    return make_dummy_student


