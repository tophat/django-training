import pytest

from exercises.exercise_5.use_cases import update_professor_ages


@pytest.mark.django_db()
def test_update_professor_ages(django_assert_num_queries):
    with django_assert_num_queries(1):
        update_professor_ages()