import pytest

from exercises.exercise_8.use_cases import update_professor_first_names
from exercises.models import Professor


@pytest.fixture
def profs():
    Professor.objects.create(first_name="freddie", last_name="mercury")
    Professor.objects.create(first_name="brian", last_name="may")
    Professor.objects.create(first_name="john", last_name="deacon")
    Professor.objects.create(first_name="roger", last_name="taylor")
    Professor.objects.create(first_name="charles", last_name="taylor")
    return Professor.objects.all()


@pytest.fixture
def new_first_names():
    return ["michael", "rose", "the", "boat", "ashore"]


@pytest.mark.django_db()
def test_get_professors(django_assert_num_queries, profs, new_first_names):
    prof_ids = [prof.id for prof in profs]
    first_name_updates = list(zip(prof_ids, new_first_names))

    with django_assert_num_queries(2):
        update_professor_first_names(first_name_updates)

    actual_first_names = []
    expected_first_names = []

    for prof_id, expected_first_name in first_name_updates:
        prof = Professor.objects.get(id=prof_id)
        actual_first_names.append(prof.first_name)
        expected_first_names.append(expected_first_name)

    assert actual_first_names == expected_first_names
