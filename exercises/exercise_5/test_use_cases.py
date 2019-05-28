import pytest

from exercises.exercise_5.use_cases import update_professor_ages
from exercises.models import Professor


@pytest.fixture
def ages():
    return [18, 24, 55]


@pytest.fixture
def profs(ages):
    for age in ages:
        Professor.objects.create(first_name="T", last_name="Mr", age=age)


@pytest.mark.django_db()
def test_update_professor_ages(django_assert_num_queries, profs, ages):
    with django_assert_num_queries(1):
        update_professor_ages()
    for age, prof in zip(ages, Professor.objects.all()):
        assert prof.age == age + 1
