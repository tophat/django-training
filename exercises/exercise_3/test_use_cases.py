import pytest

from exercises.models import Textbook, Professor, Subject
from exercises.exercise_3.use_cases import remove_pii


@pytest.fixture
def textbooks():
    expected_num_textbooks = 3
    for i in range(expected_num_textbooks):
        prof = Professor.objects.create(first_name=f"Jacob the {i}", last_name="Isaac")
        Textbook.objects.create(
            title=f"General Chemistry {i}",
            subject=Subject.objects.create(name="Chemistry"),
        ).authors.add(prof)


@pytest.mark.django_db()
def test_remove_pii(django_assert_num_queries, textbooks):
    with django_assert_num_queries(1):
        remove_pii()
    for prof in Professor.objects.all():
        assert prof.first_name == "REDACTED"
        assert prof.last_name == "REDACTED"
