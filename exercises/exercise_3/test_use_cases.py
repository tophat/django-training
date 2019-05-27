import pytest

from exercises.models import Textbook, Professor, Subject
from exercises.exercise_3.use_cases import remove_pii


@pytest.mark.django_db()
def test_remove_pii(django_assert_num_queries):
    expected_num_textbooks = 10
    for i in range(expected_num_textbooks):
        prof = Professor.objects.create(first_name=f"Jacob the {i}", last_name="Isaac")
        Textbook.objects.create(
            title=f"General Chemistry {i}",
            subject=Subject.objects.create(name="Chemistry"),
        ).authors.add(prof)

    with django_assert_num_queries(1):
        remove_pii()
