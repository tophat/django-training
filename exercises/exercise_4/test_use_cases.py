import pytest

from exercises.exercise_4.use_cases import add_new_professors
from exercises.models import Professor


@pytest.mark.django_db()
def test_add_new_professors(django_assert_num_queries):
    expected_names = [("Steve", "Pezos"), ("Charlies", "Xavier"), ("Samuel", "Oak")]
    with django_assert_num_queries(1):
        add_new_professors(expected_names)
    for names, prof in zip(expected_names, Professor.objects.all()):
        assert names[0] == prof.first_name
        assert names[1] == prof.last_name
