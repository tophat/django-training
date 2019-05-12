import pytest

from exercises.exercise_5.use_cases import update_professor_ages


@pytest.mark.django_db()
def test_(django_assert_num_queries):
    """
    hint: https://docs.djangoproject.com/en/2.2/ref/models/expressions/#f-expressions
    """
    with django_assert_num_queries(1):
        update_professor_ages()