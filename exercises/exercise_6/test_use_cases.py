import pytest

from exercises.exercise_6.use_cases import get_professor


@pytest.mark.django_db()
def test_get_professor():
    assert "SCAN TABLE" not in get_professor("joe").explain()
    assert 0 == 1
