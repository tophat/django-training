import pytest

from exercises.exercise_4.use_cases import add_new_professors


@pytest.mark.django_db()
def test_(django_assert_num_queries):
    with django_assert_num_queries(1):
        add_new_professors([
            ("Steve", "Pezos"),
            ("Charlies", "Xavier"),
            ("Samuel", "Oak")
        ])
