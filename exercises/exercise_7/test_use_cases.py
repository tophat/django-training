import pytest

from exercises.exercise_7.use_cases import get_professors
from exercises.models import Professor


@pytest.fixture
def profs():
    Professor.objects.create(first_name="freddie", last_name="mercury")
    Professor.objects.create(first_name="brian", last_name="may")
    Professor.objects.create(first_name="john", last_name="deacon")
    Professor.objects.create(first_name="roger", last_name="taylor")
    Professor.objects.create(first_name="charles", last_name="taylor")


@pytest.mark.django_db()
def test_get_professors(django_assert_num_queries, profs):
    prof_ids = [1, 2, 3, 4]
    with django_assert_num_queries(1):
        group = get_professors(prof_ids)
        assert len(group) == len(prof_ids)
        for prof, prof_id in zip(group, prof_ids):
            assert isinstance(prof, Professor)
            assert prof.id == prof_id
