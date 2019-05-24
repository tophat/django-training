import pytest

from exercises.exercise_7.use_cases import get_professors


@pytest.mark.django_db()
def test_get_professors(django_assert_num_queries):
    with django_assert_num_queries(1):
        get_professors([1, 2, 23, 41])
